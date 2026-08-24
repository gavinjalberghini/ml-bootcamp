#!/usr/bin/env python3
"""PA1: leave-one-out multiclass kNN. Stdlib only. Fill in the TODOs."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def read_arff(path: str):
    """Return (features, labels). Last column is the class; do not use it as a feature."""
    raise NotImplementedError('parse the ARFF file')


def distance(a, b, metric: int, p: float) -> float:
    """metric 1=euclidean, 2=manhattan, 3=minkowski."""
    raise NotImplementedError('euclidean / manhattan / minkowski')


def knn_loo(features, labels, k: int, metric: int, p: float):
    """Predict each row from the other rows only. Return (y_true, y_pred)."""
    raise NotImplementedError('leave-one-out kNN — exclude the query row')


def confusion_matrix(y_true, y_pred):
    """Return a labeled matrix structure you can write to markdown."""
    raise NotImplementedError('multiclass confusion matrix')


def write_report(path: str, settings: dict, elapsed: float, matrix) -> None:
    dest = Path(path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        '# PA1 kNN',
        '',
        '## Settings',
        '',
    ]
    for key, value in settings.items():
        lines.append(f'- **{key}:** {value}')
    lines.extend(['', f'## Elapsed time', '', f'{elapsed:.4f} s', '', '## Confusion matrix', '', str(matrix), ''])
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
    started = time.perf_counter()
    features, labels = read_arff(args.data)
    y_true, y_pred = knn_loo(features, labels, args.k, args.distance, args.p)
    matrix = confusion_matrix(y_true, y_pred)
    elapsed = time.perf_counter() - started
    write_report(
        args.output,
        {
            'data': args.data,
            'k': args.k,
            'distance': args.distance,
            'p': args.p,
        },
        elapsed,
        matrix,
    )
    print(f'wrote {args.output} in {elapsed:.4f}s')


if __name__ == '__main__':
    main()
