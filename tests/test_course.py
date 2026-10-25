"""Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona."""
from pathlib import Path
import sys
import json
import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'python'))
import eo_course as eo


def test_calibration_offset_and_nodata():
    out = eo.reflectance([0, 2000, 6000], .0001, -.1)
    assert np.isnan(out[0])
    np.testing.assert_allclose(out[1:], [.1, .5])
    assert np.isclose(eo.normalized_difference(out[2], out[1]), 2/3)
    assert np.isnan(eo.normalized_difference(0, 0))


def test_composite_does_not_count_cloud_or_missing_data():
    stack = np.array([[[.5, .2]], [[.7, np.nan]], [[.9, .9]]])
    valid = np.array([[[True, False]], [[True, True]], [[False, False]]])
    median, support = eo.median_composite(stack, valid)
    np.testing.assert_array_equal(support, [[2, 0]])
    assert median[0, 0] == .6 and np.isnan(median[0, 1])
    np.testing.assert_array_equal(eo.clear_mask([0, 3, 4, 5, 6, 7, 9, 11]),
                                  [False, False, True, True, True, False, False, False])


def test_area_uses_shared_eligible_coverage():
    before = np.array([[.7, .7], [.7, np.nan]])
    after = np.array([[.3, np.nan], [.8, .1]])
    r = eo.changed_area(before, after)
    assert r['candidate_ha'] == .04
    assert r['observed_ha'] == .08
    assert r['unknown_ha'] == .08
    empty = eo.changed_area(before, np.full_like(before, np.nan))
    assert empty['observed_ha'] == 0 and empty['candidate_ha'] == 0
    restricted = eo.changed_area(before, after, eligible=[[True, True], [False, False]])
    assert restricted['observed_ha'] == .04 and restricted['unknown_ha'] == .04
    assert restricted['excluded_ha'] == .08


def test_calendar_lag_and_rolling_features_exclude_target():
    s = pd.Series(np.arange(30.), index=pd.date_range('2020-01-01', periods=30))
    frame = eo.lagged_frame(s, 3)
    day = frame.index[0]
    assert frame.loc[day, 'lag'] == s.loc[day-pd.Timedelta(days=3)]
    assert frame.loc[day, 'mean7'] == s.loc[day-pd.Timedelta(days=9):day-pd.Timedelta(days=3)].mean()
    with pytest.raises(ValueError):
        eo.lagged_frame(s.drop(s.index[5]))


def test_power_fill_values_and_missing_calendar_days():
    payload = {'header': {'fill_value': -999},
               'properties': {'parameter': {'T2M': {'20200101': 27, '20200103': -999}}},
               'parameters': {'T2M': {'units': 'C'}}}
    frame = eo.parse_power_daily(payload)
    assert len(frame) == 3 and frame.T2M.isna().sum() == 2
    assert frame.attrs['parameters']['T2M']['units'] == 'C'


def test_bootstrap_constant_and_invalid_tiling():
    np.testing.assert_allclose(eo.block_bootstrap_mean(np.ones((20, 20)), block=10), [1, 1])
    with pytest.raises(ValueError):
        eo.block_bootstrap_mean(np.ones((21, 20)), block=10)


def test_holdout_target_does_not_train_model():
    frame = eo.lagged_frame(eo.synthetic_temperature())
    _, first = eo.evaluate_forecast(frame)
    changed = frame.copy()
    changed.loc[changed.index >= '2023-01-01', 'target'] += 1000
    _, second = eo.evaluate_forecast(changed)
    # Features held fixed: test target changes must not change fitted predictions.
    np.testing.assert_allclose(first['test'].ridge, second['test'].ridge)


def test_manifest_hashes(tmp_path):
    p = tmp_path / 'result.csv'; p.write_text('value\n1\n')
    m = eo.write_manifest(tmp_path/'manifest.json', 'synthetic', {}, {'seed': 42}, [p])
    assert len(m['outputs']['result.csv']) == 64
    assert json.loads((tmp_path/'manifest.json').read_text())['data_kind'] == 'synthetic'


def test_stac_pagination_preserves_get_method(monkeypatch):
    import requests
    calls = []
    pages = [{'features': [{'id': 'a'}], 'links': [
        {'rel': 'next', 'href': 'https://example.test/next?token=x', 'method': 'GET'}]},
        {'features': [{'id': 'a'}, {'id': 'b'}], 'links': []}]
    class Response:
        def raise_for_status(self): pass
        def json(self): return pages.pop(0)
    def request(method, url, **kwargs):
        calls.append((method, kwargs)); return Response()
    monkeypatch.setattr(requests, 'request', request)
    assert [x['id'] for x in eo.search_sentinel([-77, 17, -76, 18], '2025-01-01', '2025-01-02')] == ['a', 'b']
    assert calls[1][0] == 'GET' and 'json' not in calls[1][1]


def test_live_reader_local_rasters(tmp_path):
    import rasterio
    from rasterio.transform import from_bounds
    bbox = [-76.82, 17.98, -76.81, 17.99]
    assets = {}
    for band, value in [('red', 2000), ('nir', 6000), ('scl', 4)]:
        path = tmp_path/f'{band}.tif'
        data = np.full((20, 20), value, dtype='uint16')
        with rasterio.open(path, 'w', driver='GTiff', width=20, height=20,
                           count=1, dtype='uint16', crs='EPSG:4326',
                           transform=from_bounds(*bbox, 20, 20), nodata=0) as dst:
            dst.write(data, 1)
        assets[band] = {'href': str(path), 'raster:bands': [
            {'scale': .0001, 'offset': -.1, 'nodata': 0}]}
    result = eo.read_sentinel_pair({'assets': assets}, bbox)
    assert result['crs'] == 'EPSG:32618'
    assert np.isclose(np.nanmedian(result['ndvi']), 2/3)
    assert abs(result['transform'].a) == 20


def test_original_shared_toolkit_uses_projected_grid():
    import nbformat
    # It has no live requests until the learner invokes an acquisition function.
    notebook = nbformat.read(ROOT/'notebooks/01_first_light_STUDENT.ipynb', as_version=4)
    code = next(c.source for c in notebook.cells if c.cell_type == 'code' and 'def make_grid' in c.source)
    namespace = {}; exec(compile(code, '<original toolkit>', 'exec'), namespace)
    grid = namespace['make_grid']([-76.82, 17.98, -76.81, 17.99], 20)
    assert grid['crs'] == 'EPSG:32618' and grid['pixel_hectares'] == .04
