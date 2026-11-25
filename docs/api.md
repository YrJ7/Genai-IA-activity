# API reference

FastAPI serves an interactive OpenAPI UI at `/docs` and an OpenAPI JSON document
at `/openapi.json`.

## `GET /api/health`

Returns `{"status":"ok"}` when the application process is available.

## `POST /api/ask`

Request:

```json
{"question":"My cotton leaves are turning yellow.","language":"en"}
```

`language` is one of `en`, `hi`, or `mr` and defaults to `en`. Question length
is 2–1000 characters.

Matched response:

```json
{
  "answer":"...",
  "source":"Demonstration guidance · cotton",
  "publication_date":"2025-06-15",
  "confidence":"High",
  "knowledge_id":1,
  "knowledge_version":1,
  "matched":true,
  "demo":true
}
```

`confidence` is a heuristic label based on lexical overlap, not a calibrated
probability. Unsupported and live-information requests return a localized
fallback, null source/date/record ID, `matched:false`, and `demo:true`. Every
accepted question and response is persisted in the query history.

## Admin endpoints

These endpoints are intentionally **unauthenticated** in this prototype. Do not
expose them to an untrusted network.

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/admin/stats` | Record counts and latest eight questions; `query_count` is the all-time query total. |
| `GET` | `/api/admin/records?search=&status=all` | Search and filter records. Status: `all`, `pending`, `approved`, `rejected`. |
| `POST` | `/api/admin/records` | Create a record. Defaults to pending review. |
| `PUT` | `/api/admin/records/{id}` | Edit a record and increment its content version. |
| `PATCH` | `/api/admin/records/{id}/status?status=approved` | Change review status. |

Knowledge payload fields: `title`, `category`, `keywords`, `answer_en`,
`answer_hi`, `answer_mr`, `source`, `publication_date` (ISO date), and `status`.
The English answer is required; localized answers are optional and fall back to
English when absent.

Example:

```bash
curl -s http://localhost:8000/api/health
curl -s -X POST http://localhost:8000/api/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"How often should I irrigate soybean?","language":"en"}'
```
