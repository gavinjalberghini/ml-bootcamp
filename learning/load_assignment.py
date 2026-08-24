"""Import an earlier assignment module without copying it.

Later tickets subclass or call the class you already wrote. Fix a bug in the
assignment that introduced it; every later script picks it up on the next run.

Usage (already wired in pa-scaled and later):

    from load_assignment import import_pa
    knn = import_pa('pa-knn')
    class ScaledKNN(knn.KNN):
        ...

`uv run` on a later script does **not** inherit that earlier file's
`# /// script` dependencies. Re-declare any third-party package you still
call (for example matplotlib) in the current file's script header.

Stretch methods (`stretch_*`) are never imported by later tickets.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

LEARNING = Path(__file__).resolve().parent

SCRIPTS = {
    'pa-knn': LEARNING / 'pa-knn' / 'kNN.py',
    'pa-scaled': LEARNING / 'pa-scaled' / 'kNN_scaled.py',
    'pa-metrics': LEARNING / 'pa-metrics' / 'kNN_report.py',
    'pa-selection': LEARNING / 'pa-selection' / 'kNN_select.py',
    'pa-ensemble': LEARNING / 'pa-ensemble' / 'kNN_ensemble.py',
    'pa-gpu': LEARNING / 'pa-gpu' / 'knn_gpu.py',
    'pa-online': LEARNING / 'pa-online' / 'online_knn.py',
}


def import_pa(name: str):
    """Load `learning/<name>/...py`. `name` is a slug: 'pa-knn', 'pa-scaled', ..."""
    path = SCRIPTS.get(name)
    if path is None:
        raise KeyError(f'unknown assignment {name!r}; expected one of {sorted(SCRIPTS)}')
    if not path.is_file():
        raise FileNotFoundError(path)

    learning_dir = str(LEARNING)
    if learning_dir not in sys.path:
        sys.path.insert(0, learning_dir)

    mod_name = f'learning_{name.replace("-", "_")}'
    if mod_name in sys.modules:
        return sys.modules[mod_name]

    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f'cannot load {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = module
    spec.loader.exec_module(module)
    return module
