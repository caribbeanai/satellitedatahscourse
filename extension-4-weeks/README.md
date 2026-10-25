# Eyes in the Sky: four-week extension

**Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.**

This course continues the original one-day Jamaican high-school workshop. Students who can run the four original notebooks now learn to defend a satellite measurement, test a change map, evaluate a forecast and explain a decision. The extension is suitable for senior secondary students with basic Python, and introductory university groups. It is an additional four weeks; the original workshop remains the prerequisite.

## Teaching schedule

Each week contains a three-hour class and approximately three hours of independent work. These are suggested teaching allocations, not recorded contact hours. Each class uses 45 minutes of lecture, 75 minutes of guided computing, 45 minutes of independent investigation and a 15-minute evidence discussion.

| Week | Lecture and laboratory | Student submission |
|---|---|---|
| 1 | [From light to a defensible measurement](lectures/01_measurement.md) · [Notebook 05](notebooks/05_quality_and_measurement.ipynb) | Data card, cloud-support map and calibrated NDVI comparison |
| 2 | [Change, controls and uncertainty](lectures/02_change.md) · [Notebook 06](notebooks/06_change_and_uncertainty.ipynb) | Threshold-sensitivity table, control comparison and cautious interpretation |
| 3 | [Forecasting without future information](lectures/03_forecasting.md) · [Notebook 07](notebooks/07_forecasts_and_validation.ipynb) | Chronological model comparison with availability-lag experiment |
| 4 | [From a map to a public decision](lectures/04_decisions.md) · [Notebook 08](notebooks/08_capstone_and_reproducibility.ipynb) | Reproducible capstone, provenance manifest and five-minute presentation |

[Assignments and marking rubric](ASSESSMENT.md) · [Instructor guide and worked answers](instructor/GUIDE.md) · [Verified sources](SOURCES.md) · [Review of the original materials](REVIEW.md).

## Run locally

From the repository root, use Python 3.11 or 3.12:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m jupyterlab
```

On Windows activate with `.venv\Scripts\activate`. Open a notebook in this folder and run its cells in order. Every default lesson runs on **explicitly synthetic teaching data**, with no network, credentials or downloads. The plotted numbers are not observations of Jamaica. Each lesson has complete worked examples followed by investigations where students edit parameters and explain the result. Independent assignments require additional work beyond running the examples.

To run on Colab, use the links below. The setup cell fetches this public repository only when the course module is absent. Review the code before running downloads.

| Laboratory | Open in Colab |
|---|---|
| 05 | [Data quality](https://colab.research.google.com/github/caribbeanai/satellitedatahscourse/blob/main/extension-4-weeks/notebooks/05_quality_and_measurement.ipynb) |
| 06 | [Change detection](https://colab.research.google.com/github/caribbeanai/satellitedatahscourse/blob/main/extension-4-weeks/notebooks/06_change_and_uncertainty.ipynb) |
| 07 | [Forecast validation](https://colab.research.google.com/github/caribbeanai/satellitedatahscourse/blob/main/extension-4-weeks/notebooks/07_forecasts_and_validation.ipynb) |
| 08 | [Capstone](https://colab.research.google.com/github/caribbeanai/satellitedatahscourse/blob/main/extension-4-weeks/notebooks/08_capstone_and_reproducibility.ipynb) |

## Move from demonstration to observations

Notebook 05 has an opt-in live Sentinel-2 search and small-area raster read. Notebook 07 has an opt-in NASA POWER request. Turn `RUN_LIVE` on deliberately. A failed request raises an error; it does not replace observed data with a synthetic result. Save the full response, selected item IDs, input dates, asset calibration, quality policy and retrieval time. Network availability and provider changes can affect live runs.

The `python/eo_course.py` module supplies calibrated indices, cloud masks, support counts, change areas, a spatial-block uncertainty demonstration, chronological forecasts and manifests. The original toolkit has also received certificate-verification, calibration and projected-grid corrections. Do not combine results produced under different calibration or quality policies without rerunning them.

## Completion criteria

Students submit all four assignments, achieve at least 60/100 overall and demonstrate the capstone from a fresh run. The instructor sets any institutional certification rules separately. These materials do not claim university endorsement, accreditation or completed operational validation.
