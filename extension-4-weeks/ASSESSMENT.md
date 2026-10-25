# Assignments and marking

Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Each weekly submission includes a notebook, short report and small permitted outputs. The worked notebooks are starting points; an unchanged run does not meet the independent investigation requirement. Suggested report lengths are 600–900 words for weeks 1–3 and 1,200–1,800 words for the capstone, excluding code and references.

## Week 1. Can you trust the pixels? — 20 points

Define a study question and boundary. Compare raw-number and calibrated index calculations. Demonstrate how cloud policy and minimum observation count affect the estimate and unknown area. Provide a support-count figure and an area table. Save scene metadata for observations. If network access fails, complete an original synthetic missingness experiment and label it accordingly.

Award 5 points each for calibration/missing values, quality/coverage analysis, an independently varied experiment, and metadata/interpretation. A map without a denominator cannot receive full coverage marks.

## Week 2. Does the result survive different choices? — 20 points

Compute candidate-change hectares at three declared thresholds. Repeat with a changed effect and missingness pattern, or independently acquired observations and a justified control. Compare three spatial block sizes, retained block counts and excluded errors. Use reference-label precision/recall only when labels exist. For observed changes, propose an independent validation sample.

Award 5 points each for shared-validity/area calculations, threshold analysis, controls/validation reasoning, and uncertainty/limitations. Allow a null result or a change opposite to the initial expectation.

## Week 3. Would the forecast work at issue time? — 20 points

Write a forecast contract and compare persistence, fixed Ridge and a training-only monthly climatology. Use chronological train/validation/test boundaries. Run availability lags of one, three and seven days on common target dates. Save MAE, RMSE, sample sizes and a residual figure. State whether the target is a gridded product or an independent observation, and explain how you avoid tuning on the test period.

Award 5 points each for information/latency, chronological fitting, baseline/lag comparison, and interpretation/sources. A model need not win. Correct leakage before assigning methodology marks.

## Week 4. Reproducible community analysis — 40 points

Choose one track and extend it beyond the demonstration:

| Track | Required analysis | Claim boundary |
|---|---|---|
| Vegetation change and production scenario | Quality map, shared-valid area, three thresholds, control discussion and sourced or explicitly hypothetical cost inputs | Spectral change alone does not establish storm causation, crop loss or compensation |
| Solar-site comparison | Three sites, returned units/grid metadata, day-weighted energy scenario and sensitivity to panel/performance assumptions | Sunlight ranking alone does not establish planning, land or grid suitability |
| Vegetation per resident | Population source/date/boundary, cloud handling, area uncertainty and independent vegetation validation or a validation plan | Vegetation is not equivalent to accessible public green space |
| Product-based forecast | Availability contract, chronological baselines, delay sensitivity and separate event/station validation plan | Product agreement is not independent ground validation or warning readiness |

Submit a runnable notebook, data card, evidence ledger, output hashes, exact environment information, references, peer-review corrections and five-minute presentation. Preserve observed-input metadata and retrieval dates. Frame synthetic-only work as a method experiment and provide a real-data acquisition/validation plan.

Award 10 points for question/data, 10 for analysis/validation, 8 for fresh-run reproducibility/provenance, 7 for evidence/assumption boundaries, and 5 for presentation/peer review. Completion requires all four submissions, at least 60/100 overall and a fresh capstone run. Institutional certification rules remain separate.

## Data-card template

- **Question and intended decision:**
- **Data status:** synthetic / observed / mixed; identify every invented component.
- **Boundary and population:** coordinates, projection, dates and eligibility rule.
- **Inputs:** provider, product version, scene IDs/query, URLs and retrieval time.
- **Calibration and units:** scale, offset, nodata, units and conversions.
- **Quality:** rejected classes, support, missingness, validation and unknown area.
- **Method:** threshold/model, control/split dates, seed and sensitivity checks.
- **Outputs:** filenames, captions, hashes and rerun command.
- **Interpretation:** measurements, assumptions, uncertainty, limits and recommendation.
- **Rights and handling:** data terms, attribution and restricted inputs omitted.

## Peer review

Identify one reproducible claim, one missing source/assumption, one failure test and one revision. Record the environment and whether a fresh kernel was used. Explain numerical differences instead of forcing agreement with a preferred answer.
