# Evaluation report

## Scope and reproducibility

This is a **smoke benchmark of the local demonstration retriever**, not a
clinical/agronomic validation, a model benchmark, or a farmer pilot. Reproduce
it with:

```bash
python scripts/evaluate.py
python -m unittest discover -s tests -v
```

The evaluator uses four fixed, seeded in-scope prompts and three fixed
out-of-scope prompts against a temporary SQLite database seeded by the
application. The metrics are descriptive for these seven examples only.

## Results

| Metric | Result | Definition |
|---|---:|---|
| In-scope topic accuracy | 4/4 (100%) | Returned source label contains the expected crop/topic. |
| In-scope retrieval recall | 4/4 (100%) | A record was returned for each of the four expected in-scope prompts. |
| Citation metadata coverage | 4/4 (100%) | Matched response included a source label and publication date. |
| Out-of-scope refusal rate | 3/3 (100%) | Weather, mandi prices, and tractor repair returned the safe fallback. |
| Seed answer-field coverage | 4/4 (100%) | Each seeded record has English, Hindi, and Marathi answer text. |
| Automated API tests | 5 passed | Tests include multilingual matching, refusal, approval gating, versioning, and query totals. |

These are benchmark counts, **not estimates of real-world performance**. The
test set is authored alongside the demo records, is very small, and does not
include adversarial, noisy, dialectal, misspelled, or field-collected questions.
Citation coverage means metadata exists; it does not validate the truth of the
guidance or the authority of the demonstration source.

## Speech, translation, faithfulness, model comparisons, and pilot

| Evaluation area | Finding |
|---|---|
| Speech recognition accuracy / WER | Not measured. Recognition uses the browser's native API; this repository has no labeled audio corpus or transcript benchmark. |
| Speech output quality | Not measured. Synthesis is delegated to browser/device voices; quality and voice availability vary. |
| Translation quality | Not measured. Seed answer fields exist in all three languages (4/4 records), but no bilingual human review or translation benchmark has been run. |
| Answer faithfulness | No human or independent source-grounded faithfulness score is available. The response is selected from a stored record, but the demonstration content itself is not verified. |
| Model benchmark comparison | No AI models were tested. There are no model calls or model dependencies; the deterministic lexical retriever is the sole system under test. |
| Farmer pilot findings | No pilot was conducted. No user study or participant findings are claimed. |

## Interpretation and next evaluation

The benchmark verifies that four happy-path prompts retrieve their intended
seed record, the three unsupported/live-data probes refuse, multilingual seed
answers can be retrieved, and citations are present in successful responses.
It does not validate agronomic correctness, translation equivalence, speech
recognition, calibrated confidence, or usefulness to farmers.

Before any real-world use, have agronomists validate each statement against
versioned official sources; conduct independent Hindi/Marathi review; test with
consented speakers across devices, accents, and field noise; report WER and
task-completion rates; score answer faithfulness and refusal appropriateness
with blinded human raters; compare retrieval/model baselines on a held-out,
expert-annotated corpus; and run an ethics-reviewed field pilot with consent,
privacy safeguards, and a documented protocol. Do not present future results
until measured.
