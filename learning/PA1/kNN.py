# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""PA1: leave-one-out multiclass kNN. Stdlib only.

Later assignments import this module and subclass `KNN`. Keep the class name
and the method signatures. Fill in the TODOs; do not rename the class.
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path


class KNN:
    """Unscaled kNN. `distance` is 1=euclidean, 2=manhattan, 3=minkowski."""

    def __init__(self, k: int = 3, distance: int = 1, p: float = 3.0):
        if k < 1:
            raise ValueError('k must be >= 1')
        if distance not in (1, 2, 3):
            raise ValueError('distance must be 1, 2, or 3')
        self.k = k
        self.distance = distance
        self.p = p

    def read_arff(self, path: str):
        """Return (features, labels). Last column is the class, not a feature."""
        raise NotImplementedError('parse the ARFF file')

    def dist(self, a, b) -> float:
        raise NotImplementedError('euclidean / manhattan / minkowski')

    def vote(self, neighbor_labels: list) -> str:
        """Majority label. Document a deterministic tie-break in your report."""
        raise NotImplementedError('majority vote')

    def predict_one(self, query, pool_x, pool_y) -> str:
        """Predict `query` from `pool_x` / `pool_y`. Query is not in the pool."""
        raise NotImplementedError('k nearest neighbors, then vote')

    def leave_one_out(self, features, labels):
        """For each row i, predict from all rows except i. Return (y_true, y_pred)."""
        raise NotImplementedError('leave-one-out — exclude the query row')

    def confusion_matrix(self, y_true, y_pred):
        raise NotImplementedError('labeled multiclass confusion matrix')

    def write_report(self, path: str, settings: dict, elapsed: float, matrix) -> None:
        dest = Path(path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        lines = ['# PA1 kNN', '', '## Settings', '']
        for key, value in settings.items():
            lines.append(f'- **{key}:** {value}')
        lines.extend(['', '## Elapsed time', '', f'{elapsed:.4f} s', '', '## Confusion matrix', '', str(matrix), ''])
        dest.write_text('\n'.join(lines))


def parse_args():
    parser = argparse.ArgumentParser(description='PA1 leave-one-out kNN')
    parser.add_argument('data', help='ARFF path')
    parser.add_argument('--distance', type=int, default=1, choices=(1, 2, 3), help='1=euclidean, 2=manhattan, 3=minkowski')
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--p', type=float, default=3.0, help='Minkowski exponent')
    parser.add_argument('--output', default='output_knn.md')
    return parser.parse_args()


def main():
    args = parse_args()
    model = KNN(k=args.k, distance=args.distance, p=args.p)
    started = time.perf_counter()
    features, labels = model.read_arff(args.data)
    y_true, y_pred = model.leave_one_out(features, labels)
    matrix = model.confusion_matrix(y_true, y_pred)
    elapsed = time.perf_counter() - started
    model.write_report(
        args.output,
        {'data': args.data, 'k': args.k, 'distance': args.distance, 'p': args.p},
        elapsed,
        matrix,
    )
    print(f'wrote {args.output} in {elapsed:.4f}s')


if __name__ == '__main__':
    main()
