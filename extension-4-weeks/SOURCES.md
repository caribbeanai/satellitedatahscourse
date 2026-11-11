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

## Physics labs

Checked on 11 November 2026. The lab parameters and worked results are generated in the notebooks.

| Primary source | Where it is used |
|---|---|
| [NIST, Radiance Temperature Calibrations](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication250-43.pdf) and [CODATA constants](https://physics.nist.gov/cuu/Constants/) | Lab 09 uses Planck radiance at one wavelength and its inverse, with SI constants. |
| [NOAA NESDIS, ABI channel summary](https://www.nesdis.noaa.gov/our-satellites/currently-flying/goes-east-west/abi-scan-mode-information-and-channel-summary) | Lab 09 identifies the visible red and clean longwave window channels. |
| [USGS, Landsat Level-1 conversions](https://www.usgs.gov/landsat-missions/using-usgs-landsat-level-1-data-product) and [Collection 2 surface-temperature inputs](https://www.usgs.gov/landsat-missions/landsat-collection-2-atmospheric-auxiliary-data) | Lab 09 connects top-of-atmosphere brightness temperature to the separate surface-temperature retrieval. |
| [NASA, IMERG V07 technical documentation](https://gpm.nasa.gov/resources/documents/imerg-v07-technical-documentation) and [NASA Earthdata, half-hour accumulation clarification](https://forum.earthdata.nasa.gov/viewtopic.php?t=6779) | Labs 09–10 use the description of IMERG inputs, spatial grid and conversion of half-hourly rain rates to depths. |
| [USGS Water Science School, surface runoff](https://www.usgs.gov/water-science-school/science/surface-runoff-and-water-cycle) | Lab 10 relates runoff to ground conditions. The numerical runoff fractions are assumptions for the exercise. |
| [Randall J. LeVeque, University of Washington, 1-D advection notebook](https://faculty.washington.edu/rjl/classes/am574w2023/_static/advection_highres.html) | Lab 11 uses a periodic upwind update and Courant number. The lesson derives conservation for its stated boundary condition. |

## Rights

Original course text/code are credited to Adrian Dunkley under the existing MIT licence. Packages and satellite/climate products retain their own licences and attribution terms. The code licence does not relicense provider data. Inspect the collection's linked terms before redistributing imagery. This release supplies synthetic examples and acquisition instructions rather than bulk imagery copies.
