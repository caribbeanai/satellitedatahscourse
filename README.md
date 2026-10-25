# Eyes in the Sky: Satellite Data Analysis for Jamaica

**Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.**

Satellite-data teaching materials for Jamaican students, with the original one-day workshop and an additional four-week course. Students investigate vegetation, open water, candidate storm change, solar resources and temperature, then learn to document data quality, quantify sensitivity and evaluate forecasts.

## Start here

| Programme | Materials |
|---|---|
| Original workshop | [Four student notebooks](notebooks/), with marked learner tasks |
| Team challenges | [Storm Bill, Solar Scout and Green Score](challenges/) |
| Additional four weeks | [Course guide, lectures, notebooks, assignments and instructor answers](extension-4-weeks/) |
| Original assessment | [Assessment information](final-assessment/) |

The extension follows this sequence:

| Week | Main question | New laboratory |
|---|---|---|
| 1 | Which pixels can you trust? | [05: Quality and measurement](extension-4-weeks/notebooks/05_quality_and_measurement.ipynb) |
| 2 | Does the change survive different choices? | [06: Change and uncertainty](extension-4-weeks/notebooks/06_change_and_uncertainty.ipynb) |
| 3 | Would the forecast work at issue time? | [07: Forecasts and validation](extension-4-weeks/notebooks/07_forecasts_and_validation.ipynb) |
| 4 | What decision does the evidence support? | [08: Capstone and reproducibility](extension-4-weeks/notebooks/08_capstone_and_reproducibility.ipynb) |

Allow one three-hour class plus approximately three hours of independent work each week. The course guide explains learning outcomes, prerequisites and submissions. Lecture notes include equations, diagrams, worked examples and classroom prompts.

## Run the materials

Use Python 3.11 or 3.12. From a local checkout:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m jupyterlab
```

On Windows activate with `.venv\Scripts\activate`. [Colab links and setup guidance](extension-4-weeks/README.md) are provided for the four new labs. Their default examples use explicitly synthetic teaching data and run without live requests after installation. Each includes an independent investigation; students must do more than rerun the example.

Optional Sentinel-2 and NASA POWER sections retrieve observations and preserve metadata. They raise errors when acquisition fails. Their outputs must be labelled separately from synthetic examples. The original workshop notebooks need learners to complete the marked gaps and use live services.

## Code, data and validation

[Reusable Python tools](python/eo_course.py) handle calibration, masks, support counts, area, change sensitivity, calendar-aware lags, chronological model comparisons and provenance. [Sources](extension-4-weeks/SOURCES.md) link the primary product and software documentation. The MIT licence applies to original course code/text; provider datasets and third-party packages retain their own terms.

```bash
python -m pytest -q
python scripts/validate_extension.py
```

The validation command runs the new default labs in separate Jupyter kernels. On restricted hosts without kernel sockets, use the explicitly labelled fallback `python scripts/validate_extension.py --plain-python`, which executes plain-Python cells in separate processes. [GitHub Actions](.github/workflows/course-checks.yml) checks tests and notebooks after pushes. [Release review](extension-4-weeks/REVIEW.md) and [validation record](extension-4-weeks/VALIDATION.md) explain what was checked and what still requires live-data verification.

Index thresholds identify candidate spectral patterns. They do not independently establish crop loss, causal storm damage, compensation, public access to green space or operational forecast skill. The extension teaches the additional evidence those interpretations need.

## Original workshop links

- [Course page](https://adriandunkley.net/courses/eyes-in-the-sky-high-school.html)
- [Original assessment page](https://adriandunkley.net/courses/eyes-in-the-sky-high-school-exam.html)

## Citation and licence

Use [CITATION.cff](CITATION.cff) to credit Adrian Dunkley. Original materials remain under the [MIT licence](LICENSE).
