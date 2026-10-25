"""Prepared by Adrian Dunkley, Physicist, Climate Studies Group, Mona.

Explicit fallback for plain-Python course cells on hosts without kernel sockets.
This runner does not emulate IPython magics or claim Jupyter-kernel validation.
"""
from pathlib import Path
import base64
import contextlib
import io
import sys
import nbformat
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

path = Path(sys.argv[1])
root = Path(__file__).resolve().parents[1]
notebook = nbformat.read(path, as_version=4)
figdir = root/'outputs/figures'/path.stem
figdir.mkdir(parents=True, exist_ok=True)
namespace = {'__name__': '__main__'}
counter = 0
for i, cell in enumerate(notebook.cells):
    if cell.cell_type != 'code':
        continue
    cell.outputs = []
    def display(value):
        cell.outputs.append(nbformat.v4.new_output('display_data', data={'text/plain': repr(value)}))
    def show(*args, **kwargs):
        global counter
        for number in plt.get_fignums():
            figure = plt.figure(number)
            buffer = io.BytesIO(); figure.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
            counter += 1
            (figdir/f'figure_{counter:02d}.png').write_bytes(buffer.getvalue())
            cell.outputs.append(nbformat.v4.new_output('display_data', data={
                'image/png': base64.b64encode(buffer.getvalue()).decode(), 'text/plain': 'Teaching figure'}))
        plt.close('all')
    namespace['display'] = display
    plt.show = show
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
        exec(compile(cell.source, f'{path.name}:cell{i}', 'exec'), namespace)
    if stream.getvalue():
        cell.outputs.insert(0, nbformat.v4.new_output('stream', name='stdout', text=stream.getvalue()))
    cell.execution_count = sum(c.cell_type == 'code' for c in notebook.cells[:i+1])
notebook.metadata['execution_note'] = 'Executed as plain Python in an isolated process; not a Jupyter kernel.'
nbformat.write(notebook, root/'outputs/executed'/path.name)
