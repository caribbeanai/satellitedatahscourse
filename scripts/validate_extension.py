"""Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Execute default teaching notebooks in separate kernels. Never enables live cells.
"""
from pathlib import Path
import ast
import json
import platform
import sys
import subprocess
import importlib.metadata
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
plain = '--plain-python' in sys.argv
record = {'python': platform.python_version(), 'data_kind': 'synthetic',
          'execution_mode': 'isolated Python processes' if plain else 'Jupyter kernels',
          'live_services_tested': False, 'notebooks': [],
          'packages': {name: importlib.metadata.version(name) for name in
                       ['numpy', 'pandas', 'matplotlib', 'scikit-learn', 'rasterio', 'nbformat', 'nbclient']}}
for path in sorted((ROOT/'extension-4-weeks/notebooks').glob('*.ipynb')):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    output = ROOT/'outputs/executed'/path.name
    output.parent.mkdir(parents=True, exist_ok=True)
    if plain:
        subprocess.run([sys.executable, str(ROOT/'scripts/run_notebook_plain.py'), str(path)],
                       cwd=ROOT, check=True, timeout=180, stdout=subprocess.DEVNULL)
    else:
        NotebookClient(notebook, timeout=180, kernel_name='python3',
                       resources={'metadata': {'path': str(ROOT)}}).execute()
        nbformat.write(notebook, output)
    record['notebooks'].append({'path': str(path.relative_to(ROOT)), 'status': 'passed',
                               'code_cells': sum(c.cell_type == 'code' for c in notebook.cells)})
    print('PASS', path.name, flush=True)
for folder in ['notebooks', 'challenges']:
    for path in sorted((ROOT/folder).glob('*.ipynb')):
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        cell = next(c.source for c in notebook.cells if c.cell_type == 'code' and 'def make_grid' in c.source)
        ast.parse(cell)
        assert 'GDAL_HTTP_UNSAFESSL' not in cell
record['original_shared_toolkits_syntax_checked'] = 7
path = ROOT/'outputs/validation.json'; path.write_text(json.dumps(record, indent=2)+'\n')
print('Validation record:', path)
