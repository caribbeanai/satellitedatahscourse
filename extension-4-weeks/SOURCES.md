# Source register

Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Primary documentation checked on 25 October 2026. These references support methods and data handling; they do not establish Jamaican outcome measurements. Synthetic values come from the course generators.

| ID | Primary source | Course use |
|---|---|---|
| S1 | [ESA/Copernicus, Sentinel-2 products](https://sentiwiki.copernicus.eu/web/s2-products) | Processing levels, reflectance calibration and product metadata |
| S2 | [Element 84, Earth Search Sentinel-2 L2A metadata](https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a) | Collection identity, asset names and raster metadata; save selected item metadata too |
| S3 | [Rasterio, Resampling](https://rasterio.readthedocs.io/en/stable/topics/resampling.html) and [Reprojection](https://rasterio.readthedocs.io/en/stable/topics/reproject.html) | Grid alignment and interpolation; preserve categorical labels |
| S4 | [NASA POWER, Data questions](https://power.larc.nasa.gov/docs/faqs/data/) | Parameter-specific support, sources, units, quality and availability |
| S5 | [NASA POWER, Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/) | Daily query and response metadata |
| S6 | [scikit-learn, TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | Ordered splits and gaps; implementation still needs an availability contract |

The index arithmetic, projected area, difference of changes, MAE/RMSE and scenario equations are explained as course derivations. Block resampling is a limited teaching implementation, not a source-validated uncertainty model for Jamaican imagery.

## Rights

Original course text/code are credited to Adrian Dunkley under the existing MIT licence. Packages and satellite/climate products retain their own licences and attribution terms. The code licence does not relicense provider data. Inspect the collection's linked terms before redistributing imagery. This release supplies synthetic examples and acquisition instructions rather than bulk imagery copies.
