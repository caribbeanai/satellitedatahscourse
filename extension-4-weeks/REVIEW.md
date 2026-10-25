# Review and release notes

Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Reviewed 25 October 2026. Baseline: `0cfbecd081b9987f7d3511dc28d5c640502e66c9` on `main`. Both visible branches were inspected; the other points to the merged challenge commit. Four original student notebooks and three challenges were reviewed. The extension adds four weeks after that workshop.

| Finding | Correction |
|---|---|
| GDAL certificate verification disabled | Removed unsafe setting from all seven original notebooks; verified HTTPS remains the default |
| Calibration assumed division by 10,000 | Apply item-level scale/offset once and stop when metadata is missing; mask nodata |
| Geographic grid reported area from nominal metres | Use shared UTM grid, transform-based projected pixel area and a size cap |
| Clear-pixel policy included uncertain classes | Conservative accepted SCL classes are explicitly 4, 5 and 6 |
| Composite could partly append a failed scene | Read every requested band before appending any |
| All warnings were suppressed | Removed blanket suppression; new code locally handles only expected all-missing-median warnings |
| Assertions required an expected scientific sign | Check finite output instead of forcing warming or negative change |
| GIF timing used milliseconds where seconds are required | Convert milliseconds to seconds |
| Spectral change could be read as verified damage | Added a visible interpretation note in every original notebook and independent-validation lessons |
| Role absent from some credits | Added Physicist in notebook credits/metadata and new code/lectures |

## Validation boundaries

The validation runner supports fresh Jupyter kernels and an explicitly labelled isolated-process fallback. Local validation used the fallback because this host blocks kernel network-interface discovery. Numerical tests cover calibration, missingness, support, area, calendar lags and provenance. Original learner gaps remain intentional; shared toolkit cells are syntax-checked and exercised with local synthetic rasters. These checks do not complete the original student tasks or establish their historical results.

Optional live Sentinel-2/POWER requests are separate. No observed-data validation run is claimed without an explicit run record. Historical event dates, loss values, green-space benchmarks, electricity comparisons and local climate conclusions in inherited prose still need source-specific verification before use in research or a formal answer key. The extension teaches these limits rather than certifying every inherited assertion.

Commit identity uses Adrian Dunkley's established repository-owner identity. Existing history and third-party credits remain intact.
