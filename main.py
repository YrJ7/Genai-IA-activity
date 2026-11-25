from __future__ import annotations

import os
import re
import sqlite3
import unicodedata
from contextlib import contextmanager
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
DB_PATH = Path(os.environ.get("SMARTKISAN_DB", ROOT / "data" / "smartkisan.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Krishi Voice | smartkisan", version="1.0.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


SEED_RECORDS = [
    {
        "title": "Yellowing cotton leaves",
        "category": "Crop health",
        "keywords": "cotton,leaves,yellow,yellowing,nitrogen,waterlogging,pest,कपास,कापूस,कापसाची,पत्ते,पाने,पीले,पिवळी",
        "answer_en": "Yellow leaves in cotton can be caused by several things, including waterlogging, nutrient shortage, or sucking pests. Check whether the soil is staying too wet and inspect the underside of leaves for insects. Avoid applying fertilizer or pesticide until the cause is clearer. If the symptoms spread, take a leaf sample to your nearest Krishi Vigyan Kendra (KVK) for identification.",
        "answer_hi": "कपास की पत्तियों का पीला होना जलभराव, पोषक तत्वों की कमी या रस चूसने वाले कीटों के कारण हो सकता है। देखें कि मिट्टी में पानी तो नहीं रुका है और पत्तियों के नीचे कीटों की जांच करें। कारण स्पष्ट होने तक उर्वरक या कीटनाशक न डालें। लक्षण बढ़ें तो पहचान के लिए पत्ती का नमूना नजदीकी कृषि विज्ञान केंद्र (KVK) में दिखाएं।",
        "answer_mr": "कापसाची पाने पिवळी पडण्याची कारणे पाणी साचणे, अन्नद्रव्यांची कमतरता किंवा रस शोषणारे कीड असू शकतात. जमिनीत पाणी साचले आहे का ते पाहा आणि पानांच्या खालच्या बाजूला कीड तपासा. कारण समजेपर्यंत खते किंवा कीटकनाशक वापरू नका. लक्षणे वाढल्यास पानाचा नमुना जवळच्या कृषी विज्ञान केंद्रात (KVK) दाखवा.",
        "source": "Demonstration guidance · cotton",
        "publication_date": "2025-06-15",
        "status": "approved",
    },
    {
        "title": "Soybean irrigation basics",
        "category": "Water management",
        "keywords": "soybean,irrigate,irrigation,water,watering,soil,flowering,pod,सोयाबीन,सोयाबीनला,सिंचाई,सिंचन,पानी,पाणी,शेंगा",
        "answer_en": "Soybean needs timely moisture, especially around flowering and pod development. Irrigation frequency depends on soil type, rainfall, and local conditions, so use soil moisture rather than a fixed calendar. Avoid standing water: provide drainage after heavy rain. These are general demonstration tips; ask your local agriculture officer for a field-specific schedule.",
        "answer_hi": "सोयाबीन में फूल आने और फलियां बनने के समय पर्याप्त नमी जरूरी है। सिंचाई का अंतराल मिट्टी, बारिश और स्थानीय परिस्थितियों पर निर्भर करता है, इसलिए निश्चित कैलेंडर के बजाय मिट्टी की नमी देखकर सिंचाई करें। खेत में पानी जमा न होने दें और तेज बारिश के बाद निकास रखें। ये सामान्य प्रदर्शन सुझाव हैं; खेत के अनुसार सलाह के लिए स्थानीय कृषि अधिकारी से पूछें।",
        "answer_mr": "सोयाबीनला फुलोरा आणि शेंगा भरण्याच्या काळात योग्य ओलावा आवश्यक असतो. सिंचनाचे अंतर माती, पाऊस आणि स्थानिक परिस्थितीवर अवलंबून असते; ठरावीक वेळापत्रकाऐवजी जमिनीतील ओलावा पाहून पाणी द्या. शेतात पाणी साचू देऊ नका आणि जोरदार पावसानंतर निचरा ठेवा. हे सामान्य प्रात्यक्षिक मार्गदर्शन आहे; शेतानुसार सल्ल्यासाठी स्थानिक कृषी अधिकाऱ्यांशी संपर्क करा.",
        "source": "Demonstration guidance · soybean",
        "publication_date": "2025-05-20",
        "status": "approved",
    },
    {
        "title": "Paddy nutrient management",
        "category": "Soil & nutrients",
        "keywords": "paddy,rice,fertilizer,fertiliser,nutrients,urea,nitrogen,धान,भात,भातासाठी,खाद,खत,उर्वरक,युरिया",
        "answer_en": "For paddy, base fertilizer decisions on a soil test and your local recommended dose. Split nitrogen applications rather than applying all urea at once, and apply at the right crop stages according to local guidance. Nutrient needs vary by variety, soil, and season, so do not treat a generic dose as a prescription. Your local KVK or agriculture department can provide a field-specific recommendation.",
        "answer_hi": "धान में खाद की मात्रा मिट्टी की जांच और स्थानीय अनुशंसित मात्रा के अनुसार तय करें। यूरिया/नाइट्रोजन एक बार में देने के बजाय फसल की अवस्थाओं के अनुसार विभाजित मात्रा में दें। जरूरत किस्म, मिट्टी और मौसम के अनुसार बदलती है, इसलिए सामान्य मात्रा को पक्का नुस्खा न मानें। खेत के लिए सही सिफारिश हेतु नजदीकी KVK या कृषि विभाग से संपर्क करें।",
        "answer_mr": "भातासाठी खताचे प्रमाण माती परीक्षण आणि स्थानिक शिफारशीनुसार ठरवा. युरिया/नत्र एकाच वेळी न देता पिकाच्या अवस्थेनुसार हप्त्यांत द्या. गरज जात, माती आणि हंगामानुसार बदलते, त्यामुळे सर्वसाधारण मात्रा म्हणजे निश्चित शिफारस असे समजू नका. शेतासाठी योग्य शिफारसीसाठी जवळच्या कृषी विज्ञान केंद्राशी किंवा कृषी विभागाशी संपर्क करा.",
        "source": "Demonstration guidance · paddy",
        "publication_date": "2025-04-10",
        "status": "approved",
    },
    {
        "title": "Government schemes for farmers",
        "category": "Government schemes",
        "keywords": "government,scheme,schemes,subsidy,farmer,benefit,pm,kisan,insurance,yojana,सरकारी,योजना,योजनाएं,किसान,किसानों,शेतकरी,शेतकऱ्यांसाठी,अनुदान,पीकविमा",
        "answer_en": "Farmers may be eligible for schemes such as PM-KISAN, the Pradhan Mantri Fasal Bima Yojana, and state-specific agriculture programs. Eligibility, enrollment windows, and benefits can change. Check current details through the official PM-KISAN or state agriculture portal, or visit your local agriculture office with your land and identity documents. This demo does not verify live eligibility or application status.",
        "answer_hi": "किसान PM-KISAN, प्रधानमंत्री फसल बीमा योजना और राज्य की कृषि योजनाओं के पात्र हो सकते हैं। पात्रता, आवेदन की अवधि और लाभ बदल सकते हैं। वर्तमान जानकारी आधिकारिक PM-KISAN या राज्य कृषि पोर्टल पर जांचें, अथवा भूमि और पहचान दस्तावेजों के साथ स्थानीय कृषि कार्यालय जाएं। यह डेमो वर्तमान पात्रता या आवेदन की स्थिति की पुष्टि नहीं करता।",
        "answer_mr": "शेतकरी PM-KISAN, प्रधानमंत्री पीक विमा योजना आणि राज्याच्या कृषी योजनांसाठी पात्र असू शकतात. पात्रता, अर्जाची मुदत आणि लाभ बदलू शकतात. सध्याची माहिती अधिकृत PM-KISAN किंवा राज्य कृषी पोर्टलवर तपासा, किंवा जमीन व ओळखपत्रांसह स्थानिक कृषी कार्यालयात भेट द्या. हा डेमो सध्याची पात्रता किंवा अर्जाची स्थिती तपासत नाही.",
        "source": "Demonstration guidance · government schemes",
        "publication_date": "2025-06-01",
        "status": "approved",
    },
]


@contextmanager
def db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()


def initialize_db() -> None:
    with db_connection() as db:
        db.execute(
            """CREATE TABLE IF NOT EXISTS knowledge (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                keywords TEXT NOT NULL DEFAULT '',
                answer_en TEXT NOT NULL,
                answer_hi TEXT NOT NULL DEFAULT '',
                answer_mr TEXT NOT NULL DEFAULT '',
                source TEXT NOT NULL,
                publication_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending'
                    CHECK(status IN ('pending', 'approved', 'rejected')),
                version INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )"""
        )
        columns = {row["name"] for row in db.execute("PRAGMA table_info(knowledge)")}
        if "version" not in columns:
            db.execute("ALTER TABLE knowledge ADD COLUMN version INTEGER NOT NULL DEFAULT 1")
        db.execute(
            """CREATE TABLE IF NOT EXISTS farmer_queries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                language TEXT NOT NULL DEFAULT 'en',
                answer TEXT NOT NULL,
                knowledge_id INTEGER,
                created_at TEXT NOT NULL,
                FOREIGN KEY(knowledge_id) REFERENCES knowledge(id)
            )"""
        )
        count = db.execute("SELECT COUNT(*) FROM knowledge").fetchone()[0]
        if count == 0:
            now = datetime.now(timezone.utc).isoformat()
            db.executemany(
                """INSERT INTO knowledge
                (title,category,keywords,answer_en,answer_hi,answer_mr,source,
                 publication_date,status,created_at,updated_at)
                VALUES (:title,:category,:keywords,:answer_en,:answer_hi,:answer_mr,
                        :source,:publication_date,:status,:now,:now)""",
                [{**record, "now": now} for record in SEED_RECORDS],
            )


initialize_db()


class AskRequest(BaseModel):
    question: str = Field(min_length=2, max_length=1000)
    language: str = Field(default="en", pattern="^(en|hi|mr)$")


class KnowledgeInput(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    category: str = Field(min_length=2, max_length=100)
    keywords: str = Field(default="", max_length=500)
    answer_en: str = Field(min_length=5, max_length=5000)
    answer_hi: str = Field(default="", max_length=5000)
    answer_mr: str = Field(default="", max_length=5000)
    source: str = Field(min_length=2, max_length=300)
    publication_date: str = Field(min_length=4, max_length=30)
    status: str = Field(default="pending", pattern="^(pending|approved|rejected)$")


STOPWORDS = {
    "a", "an", "and", "are", "about", "can", "for", "from", "how", "i", "is",
    "it", "my", "of", "often", "please", "the", "to", "what", "when", "where",
    "which", "with", "should", "available", "recommend", "recommended", "के",
    "की", "का", "में", "से", "और", "है", "हैं", "हो", "रहे", "क्या", "किस",
    "को", "लिए", "पर", "तक", "करें", "कितनी", "बार", "कौन", "सी", "आहे",
    "आणि", "काय", "किती", "कशी", "करावे", "साठी", "मध्ये", "माझ्या",
    "किती", "वेळा", "द्या", "कोणते", "कोणत्या", "जाते", "सुचवले", "उपलब्ध",
    "आहेत", "हैं", "अनुशंसित", "किसानों", "की", "कौन", "क्या", "हैं",
}


def searchable_terms(value: str) -> set[str]:
    terms: set[str] = set()
    current: list[str] = []
    for character in unicodedata.normalize("NFC", value.lower()):
        if unicodedata.category(character)[0] in {"L", "M"} and character != "_":
            current.append(character)
        elif current:
            terms.add("".join(current))
            current.clear()
    if current:
        terms.add("".join(current))
    return {term for term in terms if len(term) >= 2}


def record_dict(row: sqlite3.Row) -> dict[str, Any]:
    return dict(row)


def find_knowledge(question: str) -> sqlite3.Row | None:
    terms = searchable_terms(question) - STOPWORDS
    if not terms:
        return None
    with db_connection() as db:
        rows = db.execute(
            "SELECT * FROM knowledge WHERE status = 'approved'"
        ).fetchall()
    scored: list[tuple[float, float, sqlite3.Row]] = []
    for row in rows:
        title_terms = searchable_terms(row["title"])
        category_terms = searchable_terms(row["category"])
        keyword_terms = searchable_terms(row["keywords"])
        matched = set(terms) & (title_terms | category_terms | keyword_terms)
        if not matched:
            continue
        coverage = len(matched) / len(set(terms))
        if len(set(terms)) > 1 and coverage < 0.4:
            continue
        score = len(matched) + 2 * len(matched & title_terms) + len(matched & keyword_terms)
        scored.append((score, coverage, row))
    if not scored:
        return None
    scored.sort(key=lambda result: (result[0], result[1]), reverse=True)
    return scored[0][2]


FALLBACKS = {
    "en": "I don't have a verified answer for that question in the available demo knowledge yet. Please check with your local Krishi Vigyan Kendra (KVK) or agriculture officer before making a crop or input decision.",
    "hi": "उपलब्ध डेमो जानकारी में इस प्रश्न का सत्यापित उत्तर नहीं है। फसल या कृषि सामग्री से जुड़ा निर्णय लेने से पहले अपने नजदीकी कृषि विज्ञान केंद्र (KVK) या कृषि अधिकारी से सलाह लें।",
    "mr": "उपलब्ध डेमो माहितीत या प्रश्नाचे पडताळलेले उत्तर नाही. पिकाबाबत किंवा निविष्ठांबाबत निर्णय घेण्यापूर्वी जवळच्या कृषी विज्ञान केंद्राशी (KVK) किंवा कृषी अधिकाऱ्यांशी संपर्क करा.",
}

LIVE_INFORMATION_TERMS = re.compile(
    r"\b(weather|forecast|rain|temperature|market|mandi|price|prices|rate|rates|"
    r"today's|today|live)\b|मौसम|मौसम|बारिश|पाऊस|हवामान|बाजार|किंमत|भाव|दर",
    re.IGNORECASE,
)


@app.get("/")
def farmer_page():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/admin")
def admin_page():
    return FileResponse(STATIC_DIR / "admin.html")


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/ask")
def ask_farmer(payload: AskRequest):
    question = payload.question.strip()
    if len(question) < 2:
        raise HTTPException(status_code=422, detail="Please enter a question.")
    record = None if LIVE_INFORMATION_TERMS.search(question) else find_knowledge(question)
    if record:
        answer = record[f"answer_{payload.language}"] or record["answer_en"]
        meaningful_terms = searchable_terms(question) - STOPWORDS
        record_terms = searchable_terms(
            f"{record['title']} {record['category']} {record['keywords']}"
        )
        match_ratio = len(meaningful_terms & record_terms) / max(1, len(meaningful_terms))
        response = {
            "answer": answer,
            "source": record["source"],
            "publication_date": record["publication_date"],
            "confidence": "High" if match_ratio >= 0.7 else "Good",
            "knowledge_id": record["id"],
            "knowledge_version": record["version"],
            "matched": True,
            "demo": True,
        }
    else:
        response = {
            "answer": FALLBACKS[payload.language],
            "source": None,
            "publication_date": None,
            "confidence": "Not available",
            "knowledge_id": None,
            "matched": False,
            "demo": True,
        }
    with db_connection() as db:
        db.execute(
            """INSERT INTO farmer_queries (question,language,answer,knowledge_id,created_at)
               VALUES (?,?,?,?,?)""",
            (question, payload.language, response["answer"], response["knowledge_id"],
             datetime.now(timezone.utc).isoformat()),
        )
    return response


@app.get("/api/admin/stats")
def admin_stats():
    with db_connection() as db:
        counts = db.execute(
            """SELECT COUNT(*) AS total,
               SUM(CASE WHEN status='approved' THEN 1 ELSE 0 END) AS approved,
               SUM(CASE WHEN status='pending' THEN 1 ELSE 0 END) AS pending
               FROM knowledge"""
        ).fetchone()
        query_count = db.execute("SELECT COUNT(*) FROM farmer_queries").fetchone()[0]
        queries = db.execute(
            "SELECT id,question,created_at FROM farmer_queries ORDER BY id DESC LIMIT 8"
        ).fetchall()
    return {
        "total": counts["total"],
        "approved": counts["approved"] or 0,
        "pending": counts["pending"] or 0,
        "query_count": query_count,
        "queries": [dict(row) for row in queries],
    }


@app.get("/api/admin/records")
def list_records(
    search: str = Query(default="", max_length=200),
    status: str = Query(default="all", pattern="^(all|pending|approved|rejected)$"),
):
    sql = "SELECT * FROM knowledge WHERE 1=1"
    params: list[str] = []
    if status != "all":
        sql += " AND status=?"
        params.append(status)
    if search.strip():
        term = f"%{search.strip().lower()}%"
        sql += " AND (lower(title) LIKE ? OR lower(category) LIKE ? OR lower(source) LIKE ? OR lower(keywords) LIKE ?)"
        params.extend([term] * 4)
    sql += " ORDER BY CASE status WHEN 'pending' THEN 0 WHEN 'approved' THEN 1 ELSE 2 END, id DESC"
    with db_connection() as db:
        rows = db.execute(sql, params).fetchall()
    return [record_dict(row) for row in rows]


@app.post("/api/admin/records", status_code=201)
def create_record(payload: KnowledgeInput):
    now = datetime.now(timezone.utc).isoformat()
    values = payload.model_dump()
    with db_connection() as db:
        cursor = db.execute(
            """INSERT INTO knowledge
               (title,category,keywords,answer_en,answer_hi,answer_mr,source,
                publication_date,status,created_at,updated_at)
               VALUES (:title,:category,:keywords,:answer_en,:answer_hi,:answer_mr,:source,
                       :publication_date,:status,:now,:now)""",
            {**values, "now": now},
        )
        row = db.execute("SELECT * FROM knowledge WHERE id=?", (cursor.lastrowid,)).fetchone()
    return record_dict(row)


@app.put("/api/admin/records/{record_id}")
def update_record(record_id: int, payload: KnowledgeInput):
    values = payload.model_dump()
    values["updated_at"] = datetime.now(timezone.utc).isoformat()
    with db_connection() as db:
        cursor = db.execute(
            """UPDATE knowledge SET title=:title,category=:category,keywords=:keywords,
               answer_en=:answer_en,answer_hi=:answer_hi,answer_mr=:answer_mr,source=:source,
               publication_date=:publication_date,status=:status,version=version+1,
               updated_at=:updated_at
               WHERE id=:id""",
            {**values, "id": record_id},
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Knowledge record not found.")
        row = db.execute("SELECT * FROM knowledge WHERE id=?", (record_id,)).fetchone()
    return record_dict(row)


@app.patch("/api/admin/records/{record_id}/status")
def set_record_status(record_id: int, status: str = Query(pattern="^(approved|rejected|pending)$")):
    now = datetime.now(timezone.utc).isoformat()
    with db_connection() as db:
        cursor = db.execute(
            "UPDATE knowledge SET status=?,updated_at=? WHERE id=?",
            (status, now, record_id),
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Knowledge record not found.")
        row = db.execute("SELECT * FROM knowledge WHERE id=?", (record_id,)).fetchone()
    return record_dict(row)
