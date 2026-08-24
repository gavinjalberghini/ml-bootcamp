"""Import an earlier assignment module without copying it.

Later tickets subclass or call the class you already wrote. Fix a bug in the
assignment that introduced it; every later script picks up the change the next
time it runs.

Usage (already wired in the PA6+ skeletons):

    from load_assignment import import_pa
    PA1 = import_pa('PA1')
    class ScaledKNN(PA1.KNN):
        ...

`uv run` on a later script does **not** inherit that earlier file's
`# /// script` dependencies. Re-declare any third-party package you still
call (for example matplotlib) in the current file's script header.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

LEARNING = Path(__file__).resolve().parent

# Assignment folder -> script that defines the public class / helpers.
SCRIPTS = {
    'PA1': LEARNING / 'PA1' / 'kNN.py',
    'PA2': LEARNING / 'PA2' / 'kNN_report.py',
    'PA3': LEARNING / 'PA3' / 'kNN_ensemble.py',
    'PA4': LEARNING / 'PA4' / 'knn_gpu.py',
    'PA5': LEARNING / 'PA5' / 'online_knn.py',
    'PA6': LEARNING / 'PA6' / 'kNN_scaled.py',
    'PA7': LEARNING / 'PA7' / 'kNN_select.py',
}


def import_pa(name: str):
    """Load `learning/<name>/...py` as a module. `name` is 'PA1', 'PA6', ..."""
    path = SCRIPTS.get(name)
    if path is None:
        raise KeyError(f'unknown assignment {name!r}; expected one of {sorted(SCRIPTS)}')
    if not path.is_file():
        raise FileNotFoundError(path)

    # Later scripts live in a sibling folder. Make this package importable
    # when they do `from load_assignment import import_pa`.
    learning_dir = str(LEARNING)
    if learning_dir not in sys.path:
        sys.path.insert(0, learning_dir)

    mod_name = f'learning_{name}'
    if mod_name in sys.modules:
        return sys.modules[mod_name]

    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f'cannot load {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = module
    spec.loader.exec_module(module)
    return module
