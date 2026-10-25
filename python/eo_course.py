"""Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Teaching tools for the four-week Eyes in the Sky extension.
Synthetic examples are deliberately separate from live observations.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import warnings

import numpy as np
import pandas as pd

AUTHOR = "Adrian Dunkley"
CREDIT = "Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona."


def normalized_difference(a, b):
    """Compute an index; undefined denominators and missing values stay NaN."""
    a, b = np.broadcast_arrays(np.asarray(a, float), np.asarray(b, float))
    out = np.full(a.shape, np.nan)
    valid = np.isfinite(a) & np.isfinite(b) & (np.abs(a + b) > 1e-12)
    np.divide(a - b, a + b, out=out, where=valid)
    return out


def reflectance(dn, scale, offset, nodata=0):
    """Apply metadata calibration once; mask nodata before applying offsets."""
    raw = np.asarray(dn, float)
    return np.where(np.isfinite(raw) & (raw != nodata), raw * scale + offset, np.nan)


def clear_mask(scl, land_only=False):
    """Conservative course policy; SCL class numbers are categorical labels."""
    return np.isin(scl, [4, 5] if land_only else [4, 5, 6])


def median_composite(stack, valid, min_observations=2):
    """Return median and support count, preserving insufficient coverage as NaN."""
    stack, valid = np.asarray(stack, float), np.asarray(valid, bool)
    if stack.ndim != 3 or stack.shape != valid.shape:
        raise ValueError("Expected matching (time, row, column) arrays.")
    if min_observations < 1:
        raise ValueError("min_observations must be positive.")
    masked = np.where(valid & np.isfinite(stack), stack, np.nan)
    count = np.isfinite(masked).sum(axis=0)
    # All-missing pixels are intentionally retained and reported via count.
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="All-NaN slice encountered")
        median = np.nanmedian(masked, axis=0)
    return np.where(count >= min_observations, median, np.nan), count


def synthetic_scene(seed=42, size=60, visits=6):
    """Invented reflectance/SCL arrays, not satellite measurements of Jamaica."""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[:size, :size]
    vegetation = (xx > size // 3) & (yy > size // 4)
    water = xx < size // 8
    red = np.where(vegetation, .10, .23) + rng.normal(0, .012, (visits, size, size))
    nir = np.where(vegetation, .47, .27) + rng.normal(0, .015, (visits, size, size))
    red[:, water], nir[:, water] = .07, .025
    scl = np.broadcast_to(np.where(water, 6, np.where(vegetation, 4, 5)), red.shape).copy()
    cloudy = rng.random(red.shape) < .22
    scl[cloudy] = 9
    red[cloudy], nir[cloudy] = .75, .76
    scl[:, :3, :3] = 0  # always unknown, never zero vegetation
    return {"red": red, "nir": nir, "scl": scl, "vegetation": vegetation,
            "kind": "synthetic", "seed": seed}


def changed_area(before, after, threshold=-.2, pixel_metres=20, eligible=None):
    """Candidate loss over jointly observed eligible projected pixels."""
    before, after = np.asarray(before, float), np.asarray(after, float)
    if before.shape != after.shape or pixel_metres <= 0:
        raise ValueError("Match shapes and use positive projected pixel spacing.")
    observed = np.isfinite(before) & np.isfinite(after)
    eligibility = np.ones(before.shape, dtype=bool)
    if eligible is not None:
        if np.shape(eligible) != before.shape:
            raise ValueError("Eligibility mask must match the images.")
        eligibility = np.asarray(eligible, bool)
    valid = observed & eligibility
    delta = np.where(valid, after - before, np.nan)
    ha = pixel_metres ** 2 / 10_000
    return {"threshold": float(threshold), "candidate_ha": float(((delta < threshold) & valid).sum() * ha),
            "observed_ha": float(valid.sum() * ha),
            "unknown_ha": float((eligibility & ~observed).sum() * ha),
            "excluded_ha": float((~eligibility).sum() * ha), "delta": delta}


def block_bootstrap_mean(image, block=10, repeats=500, seed=42):
    """Resample equally sized spatial block means; teaching interval only.

    The image must tile exactly. Vary block size; dependence between blocks,
    cloud missingness and systematic calibration error remain unmodelled.
    """
    image = np.asarray(image, float)
    if image.ndim != 2 or block < 1 or any(n % block for n in image.shape):
        raise ValueError("Use a 2D image with dimensions divisible by block.")
    means = []
    for r in range(0, image.shape[0], block):
        for c in range(0, image.shape[1], block):
            a = image[r:r+block, c:c+block]
            if np.isfinite(a).all():
                means.append(a.mean())
    if len(means) < 2 or repeats < 2:
        raise ValueError("Need at least two fully observed blocks and repeats.")
    means = np.array(means)
    draws = np.random.default_rng(seed).choice(means, (repeats, len(means)), replace=True).mean(axis=1)
    return np.quantile(draws, [.025, .975])


def synthetic_temperature(seed=42, days=1461):
    """Invented daily mean temperature with seasonality and serial dependence."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2020-01-01", periods=days, freq="D")
    noise = rng.normal(0, .6, days)
    for i in range(1, days):
        noise[i] += .65 * noise[i-1]
    return pd.Series(27 + 1.8 * np.sin(2*np.pi*np.arange(days)/365.25)
                     + .0003*np.arange(days) + noise, index=dates, name="T2M")


def lagged_frame(series, available_lag_days=1):
    """Target at day t, inputs through t-lag; no future observations."""
    series = series.sort_index()
    if available_lag_days < 1 or series.index.has_duplicates:
        raise ValueError("Use a positive availability lag and unique daily dates.")
    expected = pd.date_range(series.index.min(), series.index.max(), freq="D")
    if not series.index.equals(expected):
        raise ValueError("Reindex to a complete daily calendar before making lags.")
    old = series.shift(available_lag_days)
    frame = pd.DataFrame({"target": series, "lag": old,
                          "mean7": old.rolling(7, min_periods=7).mean(),
                          "sin_doy": np.sin(2*np.pi*series.index.dayofyear/365.25),
                          "cos_doy": np.cos(2*np.pi*series.index.dayofyear/365.25)})
    return frame.dropna()


def evaluate_forecast(frame, train_end="2022-01-01", validation_end="2023-01-01"):
    """Fit on training only and evaluate fixed one-day models on later periods."""
    from sklearn.linear_model import Ridge
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    features = ["lag", "mean7", "sin_doy", "cos_doy"]
    train = frame.loc[frame.index < train_end]
    val = frame.loc[(frame.index >= train_end) & (frame.index < validation_end)]
    test = frame.loc[frame.index >= validation_end]
    if min(len(train), len(val), len(test)) < 10:
        raise ValueError("Each chronological partition needs at least 10 rows.")
    model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    model.fit(train[features], train.target)
    rows, predictions = [], {}
    for label, part in [("validation", val), ("test", test)]:
        predictions[label] = pd.DataFrame({"truth": part.target, "persistence": part.lag,
                                           "ridge": model.predict(part[features])})
        for name in ["persistence", "ridge"]:
            error = predictions[label][name] - part.target
            rows.append({"partition": label, "model": name, "n": len(part),
                         "mae_C": float(np.abs(error).mean()),
                         "rmse_C": float(np.sqrt((error**2).mean()))})
    return pd.DataFrame(rows), predictions


def parse_power_daily(payload):
    """Preserve missing days and parameter units; exclude API fill values."""
    block = payload["properties"]["parameter"]
    frame = pd.DataFrame(block, dtype=float)
    frame.index = pd.to_datetime(frame.index, format="%Y%m%d")
    fill = payload.get("header", {}).get("fill_value", -999)
    frame = frame.replace(fill, np.nan).sort_index()
    frame = frame.reindex(pd.date_range(frame.index.min(), frame.index.max(), freq="D"))
    frame.index.name = "date"
    frame.attrs["parameters"] = payload.get("parameters", {})
    return frame


def fetch_power_daily(lat, lon, start, end, parameters="T2M", community="AG"):
    """Explicit live request. Returns processed frame and full response metadata."""
    import requests
    response = requests.get("https://power.larc.nasa.gov/api/temporal/daily/point", params={
        "latitude": lat, "longitude": lon, "start": start, "end": end,
        "parameters": parameters, "community": community, "format": "JSON",
        "time-standard": "UTC"}, timeout=120)
    response.raise_for_status()
    payload = response.json()
    return parse_power_daily(payload), payload


def search_sentinel(bbox, start, end, max_pages=10):
    """Page the public STAC search, respecting GET/POST next-link semantics."""
    import requests
    url = "https://earth-search.aws.element84.com/v1/search"
    body = {"collections": ["sentinel-2-l2a"], "bbox": bbox,
            "datetime": f"{start}T00:00:00Z/{end}T23:59:59Z", "limit": 100}
    method, items, seen = "POST", [], set()
    for _ in range(max_pages):
        r = requests.request(method, url, **({"json": body} if method == "POST" else {}), timeout=90)
        r.raise_for_status()
        page = r.json()
        for item in page.get("features", []):
            if item["id"] not in seen:
                items.append(item); seen.add(item["id"])
        nxt = next((x for x in page.get("links", []) if x.get("rel") == "next"), None)
        if nxt is None:
            return items
        url, method = nxt["href"], nxt.get("method", "GET").upper()
        body = {**body, **nxt.get("body", {})} if nxt.get("merge") else nxt.get("body", {})
    raise RuntimeError("Search truncated at max_pages; reduce the dates or increase the cap.")


def read_sentinel_pair(item, bbox, metres=20):
    """Read cloud-masked NIR/red to a shared local UTM grid with metadata scaling."""
    if metres <= 0 or len(bbox) != 4 or bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
        raise ValueError("Use a valid west/south/east/north box and positive pixel size.")
    import rasterio
    from rasterio.enums import Resampling
    from rasterio.warp import transform_bounds
    from rasterio.vrt import WarpedVRT
    from rasterio.transform import from_origin
    zone = int(((bbox[0] + bbox[2])/2 + 180)//6) + 1
    crs = f"EPSG:{32600 + zone if (bbox[1]+bbox[3])/2 >= 0 else 32700 + zone}"
    w, s, e, n = transform_bounds("EPSG:4326", crs, *bbox)
    width, height = int(np.ceil((e-w)/metres)), int(np.ceil((n-s)/metres))
    if width*height > 1_000_000:
        raise ValueError("Choose a small area and positive pixel size; cap is one million pixels.")
    transform = from_origin(w, n, metres, metres)
    arrays = {}
    with rasterio.Env(AWS_NO_SIGN_REQUEST="YES", GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR"):
        for band in ["red", "nir", "scl"]:
            asset = item["assets"][band]
            meta = asset.get("raster:bands", [{}])[0]
            with rasterio.open(asset["href"]) as src:
                with WarpedVRT(src, crs=crs, transform=transform, width=width, height=height,
                               resampling=Resampling.nearest if band == "scl" else Resampling.bilinear) as vrt:
                    a = vrt.read(1, masked=True).astype(float).filled(np.nan)
            if band != "scl":
                if "scale" not in meta or "offset" not in meta:
                    raise ValueError("Asset lacks explicit reflectance scale/offset.")
                a = reflectance(a, meta["scale"], meta["offset"], meta.get("nodata", 0))
            arrays[band] = a
    arrays["ndvi"] = np.where(clear_mask(arrays["scl"]), normalized_difference(arrays["nir"], arrays["red"]), np.nan)
    arrays["crs"], arrays["transform"] = crs, transform
    return arrays


def write_manifest(path, kind, inputs, settings, outputs=()):
    """Write provenance with hashes of existing output files."""
    if kind not in {"synthetic", "observed", "mixed"}:
        raise ValueError("Declare synthetic, observed or mixed data.")
    path = Path(path)
    payload = {"prepared_by": CREDIT, "data_kind": kind,
               "created_utc": datetime.now(timezone.utc).isoformat(),
               "inputs": inputs, "settings": settings,
               "outputs": {os.path.relpath(Path(p).resolve(), path.parent.resolve()):
                           hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in outputs}}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2)+"\n")
    return payload
