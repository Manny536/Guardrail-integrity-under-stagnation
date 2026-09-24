# Claim and implementation status

| Claim / artifact | Status | Evidence and remaining obligation |
|---|---|---|
| GIUS as the operational outcome sought through SIUS | Documented application relationship | [Contract](docs/local-preservation-contract.md); a named outcome is not proof of preservation |
| Local non-compensatory preservation condition | Documented mathematical contract | Explicit scope, three-valued checks, margin, coverage, role separation, useful-task control; not a Lean theorem |
| Mock trace generation, replay checker, receipts | IMPLEMENTED | [Benchmark](docs/benchmark-protocol.md), executable cases, mutation regressions, CI |
| Aggregate/local discrimination | Synthetic calibration | [Receipt](benchmarks/receipts/calibration.json); paired cases have the same aggregate with different local outcomes |
| Real-system GIUS effectiveness | OPEN | Calibrated observables, authenticated observations, independent evaluation, longitudinal traces owed |
| Navier–Stokes connection | STRUCTURAL ANALOGY | Published mathematical result and separate elementary concentration example; no theorem transfer |
| Agent finite-time singularity | OPEN | Meaningful dynamics, norm, scaling limit, and proof/empirical evidence owed |
| Finite-grain Del/curl | PROPOSED upstream | Separate KakeyaLogic ownership; this benchmark neither implements nor validates it |
| SIUT | Preserved sibling condition | Changed protected controls require SIUT or mixed scope |

The software calibration can pass while operational validity remains open. Each case receipt explicitly states its synthetic scope, unresolved external independent review, and lack of live-routing authority. A known failure cannot be averaged away, relabeled as missing, or erased by a later pass.

Publication check: run `python3 -m unittest discover -s tests -v` and `python3 -m benchmarks.run --output artifacts`. The latter succeeds only when every registered case matches its expected outcome. CI retains the generated traces and receipts for inspection.

## External-case registration, 2026-09-24

| Object | Status | Limit |
|---|---|---|
| [GIUS-CASE-HF-2026-001](docs/case-studies/hugging-face-2026.md) | REGISTERED EXTERNAL CASE STUDY · NON-VALIDATING | Candidate SIUS windows; known control changes SIUT/mixed |
| [GIUS-DIAG-BST-001](docs/boundary-search-transition.md) | PROPOSED DIAGNOSTIC | No validated detector or causal inference |
| Extended GIUS-BENCH-001 | SYNTHETIC CALIBRATION | Mock facts only; no incident replay |
| Operational validity and h calibration | OPEN | Independent evidence owed |
