# Validation record

Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Checked on 25 October 2026 with Python 3.12.14 on Linux. See the [machine-readable record](validation/numerical-run.json).

| Check | Result |
|---|---|
| Numerical and metadata regression tests | 11 passed |
| New laboratories | All four passed, including 23 code cells in total |
| Execution method | Separate Python processes using the explicit fallback runner |
| Figures | Seven generated teaching figures visually inspected; before/after comparisons use matched scales |
| Original shared toolkits | All seven parsed; representative projected-grid execution tested |
| Notebook structure | Validated with nbformat |
| Live provider retrieval | Not executed; opt-in Sentinel-2 and POWER paths remain distinct from default tests |
| Jupyter kernel startup on this host | Blocked by local network-interface restrictions; GitHub Actions is configured to test normal kernels |

Saved notebook outputs are synthetic worked examples. They are included so learners can inspect tables and figures before running code. The execution note identifies the isolated-process runner. No historical Jamaican measurement or disaster-loss result is certified by these tests. Rasterio produced dependency deprecation warnings; no numerical check failed.

## Text and scientific review

The four lectures were read for claim boundaries, units, terminology, classroom pacing and repetitive phrasing. [Editorial diagnostics](validation/editorial-diagnostics.json) are descriptive heuristics, not an authorship detector. Repeated author credits and recurring technical terms were retained deliberately. No matched reference corpus was supplied, so the diagnostics are not a calibrated comparison.

The original notebooks now show an interpretation note. Further live-data and event-specific verification is required before treating inherited workshop narratives as validated empirical findings. The [review](REVIEW.md) records this boundary and the technical corrections.

## Reproduce

```bash
python -m pip install -r requirements-lock.txt
python -m pytest -q
python scripts/validate_extension.py
```

If kernel sockets are unavailable, explicitly use `python scripts/validate_extension.py --plain-python`. The fallback executes the plain-Python lesson cells and saves rendered figures; it does not emulate IPython magics or claim Jupyter-kernel validation. Generated files are written under ignored `outputs/`.
