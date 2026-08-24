# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""PA6: subclass PA1.KNN. Add --normalize and --task. Do not copy PA1."""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

LEARNING = Path(__file__).resolve().parent.parent
if str(LEARNING) not in sys.path:
    sys.path.insert(0, str(LEARNING))

from load_assignment import import_pa

PA1 = import_pa('PA1')


class ScaledKNN(PA1.KNN):
    """PA1 kNN plus per-query scaling and optional binary label recoding."""

    def __init__(self, k: int = 3, distance: int = 1, p: float = 3.0, normalize: str = 'none', task: str = 'multiclass'):
        super().__init__(k=k, distance=distance, p=p)
        if normalize not in ('none', 'zscore', 'minmax'):
            raise ValueError('normalize must be none, zscore, or minmax')
        if task not in ('multiclass', 'binary'):
            raise ValueError('task must be multiclass or binary')
        self.normalize = normalize
        self.task = task

    def recode_labels(self, labels, source_path: str):
        """binary: see the PA6 ticket. multiclass: return labels unchanged."""
        raise NotImplementedError('binary recode for small vs wine files')

    def scale_pair(self, query, pool):
        """Fit scaler on `pool` only. Return (scaled_query, scaled_pool)."""
        raise NotImplementedError('none / zscore / minmax without the query in the fit')

    def predict_one(self, query, pool_x, pool_y) -> str:
        raise NotImplementedError('scale, then PA1.KNN.predict_one')


def parse_args():
    parser = argparse.ArgumentParser(description='PA6 normalized kNN')
    parser.add_argument('data')
    parser.add_argument('--distance', type=int, default=1, choices=(1, 2, 3))
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--p', type=float, default=3.0)
    parser.add_argument('--normalize', default='none', choices=('none', 'zscore', 'minmax'))
    parser.add_argument('--task', default='multiclass', choices=('multiclass', 'binary'))
    parser.add_argument('--output', default='output_scaled.md')
    return parser.parse_args()


def main():
    args = parse_args()
    model = ScaledKNN(k=args.k, distance=args.distance, p=args.p, normalize=args.normalize, task=args.task)
    started = time.perf_counter()
    features, labels = model.read_arff(args.data)
    labels = model.recode_labels(labels, args.data)
    y_true, y_pred = model.leave_one_out(features, labels)
    matrix = model.confusion_matrix(y_true, y_pred)
    elapsed = time.perf_counter() - started
    model.write_report(
        args.output,
        {
            'data': args.data,
            'k': args.k,
            'distance': args.distance,
            'p': args.p,
            'normalize': args.normalize,
            'task': args.task,
        },
        elapsed,
        matrix,
    )
    print(f'wrote {args.output} in {elapsed:.4f}s')


if __name__ == '__main__':
    main()
