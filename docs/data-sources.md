# Data-source register

## Seed data

The four records seeded by `main.py` cover cotton leaf yellowing, soybean
irrigation, paddy nutrient management, and farmer schemes. Their source labels
are explicitly **demonstration guidance**. They are authored examples, not
quotes or verified extracts from ICAR, a state agriculture department, or a
government scheme portal. The publication dates are illustrative record
metadata, not evidence that a source was published on those dates.

| Topic | Seed source label | Status | Intended use |
|---|---|---|---|
| Cotton symptoms | Demonstration guidance · cotton | Illustrative; not independently verified | Retrieval and safety-flow demo |
| Soybean irrigation | Demonstration guidance · soybean | Illustrative; not independently verified | Retrieval and safety-flow demo |
| Paddy nutrients | Demonstration guidance · paddy | Illustrative; not independently verified | Retrieval and safety-flow demo |
| Farmer schemes | Demonstration guidance · government schemes | Illustrative; scheme details and eligibility not verified | Retrieval and safe-referral demo |

## Source integration policy

The prototype has no external data ingestion. It does not retrieve live weather,
market/mandi prices, scheme eligibility, or current application windows. A future
maintained dataset should include, at minimum:

- issuing organization and direct source URL;
- publication/update date and retrieval timestamp;
- applicable state, district, crop, variety, and season;
- language and translation/reviewer identity;
- record version, approval state, reviewer, and supersession link;
- license/permission and a reproducible snapshot or checksum.

Candidate official source owners for future curation include ICAR and state
agriculture universities/departments for crop guidance, IMD for weather,
Agmarknet/eNAM for market data, and the relevant official scheme portal or
department for benefits and eligibility. These are **candidate sources only**:
no data from them is included, checked, or represented as current by this app.

## Content review requirements

Before any seed record is used for real farmer decisions, obtain a qualified
agronomist's review, cite the exact source passage, confirm local applicability,
translate and independently review each language, and record approval/version
metadata. Review time-sensitive content again before publication. Keep the
fallback path available when a source is missing, stale, or not applicable.
