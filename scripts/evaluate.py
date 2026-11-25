#!/usr/bin/env python3
"""Run a small reproducible retrieval/refusal benchmark against the seeded demo."""

import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import main


IN_SCOPE = [
    ("My cotton leaves are turning yellow.", "cotton"),
    ("How often should I irrigate soybean?", "soybean"),
    ("What is the recommended fertilizer for paddy?", "paddy"),
    ("What government schemes are available for farmers?", "government schemes"),
]
OUT_OF_SCOPE = [
    "What is the weather for cotton today?",
    "What are today's mandi prices for soybean?",
    "How do I repair a tractor engine?",
]


def main_eval():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "evaluation.db"
        with patch.object(main, "DB_PATH", db_path):
            main.initialize_db()
            client = TestClient(main.app)
            retrieved = []
            for question, expected_topic in IN_SCOPE:
                response = client.post(
                    "/api/ask", json={"question": question, "language": "en"}
                )
                payload = response.json()
                retrieved.append({
                    "question": question,
                    "expected_topic": expected_topic,
                    "matched": payload["matched"],
                    "topic_match": expected_topic in payload.get("source", "").lower(),
                    "citation_present": bool(payload.get("source") and payload.get("publication_date")),
                })
            refusals = []
            for question in OUT_OF_SCOPE:
                response = client.post(
                    "/api/ask", json={"question": question, "language": "en"}
                )
                refusals.append({"question": question, "refused": not response.json()["matched"]})

            approved = client.get("/api/admin/records?status=approved").json()
            report = {
                "benchmark": "seeded demonstration questions; deterministic lexical retrieval",
                "retrieval_accuracy": sum(item["topic_match"] for item in retrieved) / len(retrieved),
                "retrieval_recall": sum(item["matched"] for item in retrieved) / len(retrieved),
                "citation_coverage": sum(item["citation_present"] for item in retrieved) / len(retrieved),
                "out_of_scope_refusal_rate": sum(item["refused"] for item in refusals) / len(refusals),
                "seeded_records_with_all_three_answers": sum(
                    bool(record["answer_en"] and record["answer_hi"] and record["answer_mr"])
                    for record in approved
                ) / max(1, len(approved)),
                "tested_models": [],
                "speech_accuracy": None,
                "translation_quality": None,
                "faithfulness_human_score": None,
                "pilot_findings": None,
                "retrieval_cases": retrieved,
                "refusal_cases": refusals,
                "limitations": [
                    "Synthetic, tiny benchmark; not representative of farmer questions.",
                    "Citation coverage measures metadata presence, not source validity.",
                    "Language-field coverage is not translation-quality evaluation.",
                    "No speech recognizer, translation model, or generative model was benchmarked.",
                    "No field pilot or human faithfulness review has been conducted.",
                ],
            }
            print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main_eval()
