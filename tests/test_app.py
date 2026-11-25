import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient

import main


class ApplicationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database = Path(self.temp_dir.name) / "test.db"
        self.db_path_patch = patch.object(main, "DB_PATH", self.database)
        self.db_path_patch.start()
        main.initialize_db()
        self.client = TestClient(main.app)

    def tearDown(self):
        self.db_path_patch.stop()
        self.temp_dir.cleanup()

    def test_seeded_question_returns_citation_and_version(self):
        response = self.client.post(
            "/api/ask",
            json={"question": "My cotton leaves are turning yellow.", "language": "en"},
        )
        self.assertEqual(response.status_code, 200)
        answer = response.json()
        self.assertTrue(answer["matched"])
        self.assertEqual(answer["knowledge_version"], 1)
        self.assertIn("Demonstration guidance", answer["source"])
        self.assertTrue(answer["publication_date"])

    def test_seeded_topics_are_retrievable_in_hindi_and_marathi(self):
        examples = (
            ("मेरे कपास के पत्ते पीले हो रहे हैं", "hi"),
            ("माझ्या कापसाची पाने पिवळी पडत आहेत", "mr"),
            ("सोयाबीन में कितनी बार सिंचाई करें", "hi"),
            ("भातासाठी कोणते खत सुचवले जाते", "mr"),
            ("किसानों के लिए कौन सी सरकारी योजनाएं उपलब्ध हैं", "hi"),
        )
        for question, language in examples:
            with self.subTest(question=question):
                response = self.client.post(
                    "/api/ask", json={"question": question, "language": language}
                )
                self.assertTrue(response.json()["matched"])

    def test_live_information_and_unsupported_questions_fall_back(self):
        for question in ("What is the weather for cotton today?", "How do I repair a tractor?"):
            with self.subTest(question=question):
                response = self.client.post(
                    "/api/ask", json={"question": question, "language": "en"}
                )
                self.assertEqual(response.status_code, 200)
                self.assertFalse(response.json()["matched"])
                self.assertIsNone(response.json()["source"])

    def test_unapproved_records_are_not_retrieved_and_edits_increment_version(self):
        created = self.client.post(
            "/api/admin/records",
            json={
                "title": "Millet seed storage",
                "category": "Crop storage",
                "keywords": "millet, seed, storage",
                "answer_en": "Keep seed dry and protected from pests.",
                "answer_hi": "",
                "answer_mr": "",
                "source": "Demonstration guidance · millet",
                "publication_date": "2025-01-01",
                "status": "pending",
            },
        )
        record_id = created.json()["id"]
        response = self.client.post(
            "/api/ask", json={"question": "How do I store millet seed?", "language": "en"}
        )
        self.assertFalse(response.json()["matched"])

        approved = self.client.patch(
            f"/api/admin/records/{record_id}/status?status=approved"
        )
        self.assertEqual(approved.status_code, 200)
        retrieved = self.client.post(
            "/api/ask", json={"question": "How do I store millet seed?", "language": "en"}
        )
        self.assertTrue(retrieved.json()["matched"])
        self.assertEqual(retrieved.json()["knowledge_version"], 1)

        record = approved.json()
        record["answer_en"] = "Store the seed in a clean, dry, sealed container."
        updated = self.client.put(f"/api/admin/records/{record_id}", json=record)
        self.assertEqual(updated.json()["version"], 2)

    def test_query_count_is_not_limited_to_recent_query_list(self):
        for index in range(10):
            self.client.post(
                "/api/ask",
                json={"question": f"Unknown question number {index}", "language": "en"},
            )
        stats = self.client.get("/api/admin/stats").json()
        self.assertEqual(stats["query_count"], 10)
        self.assertEqual(len(stats["queries"]), 8)


if __name__ == "__main__":
    unittest.main()
