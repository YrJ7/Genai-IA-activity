# Deployment and Codespaces

## Local development

Requirements: Python 3.10+ and pip.

```bash
python -m pip install -r requirements.txt
bash scripts/start.sh
```

The script launches Uvicorn on `0.0.0.0:8000`. Open the farmer page at
`http://localhost:8000`, admin at `/admin`, and OpenAPI docs at `/docs`.

## GitHub Codespaces

`.devcontainer/devcontainer.json` forwards port 8000 and installs the Python
requirements. Start the server with `bash scripts/start.sh` if it is not already
running. In the **Ports** tab, choose **Open in Browser** for port 8000. Browser
microphone access requires the forwarded HTTPS URL and explicit permission.

## Data location and reset

By default, SQLite is stored in `data/smartkisan.db`. The first startup creates
the schema, migrates existing tables with the `version` column if needed, and
inserts four demo records only when the knowledge table is empty. Set
`SMARTKISAN_DB=/absolute/path/to/file.db` before starting to select another
database. Back up the database file before replacing it.

## Verification

```bash
python -m unittest discover -s tests -v
python scripts/evaluate.py
```

## Production caveats

This repository is a local academic prototype, not a production deployment
recipe. Before deployment, add admin authentication and authorization, HTTPS,
CSRF protection, rate limits, privacy/retention controls for farmer questions,
database backups, operational monitoring, content provenance and review
workflows, and a security review. Do not use the development server settings
for public production traffic.
