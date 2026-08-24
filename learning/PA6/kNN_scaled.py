#!/usr/bin/env python3
"""PA6: leave-one-out kNN with --normalize and --task. Copy forward from PA1."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def read_arff(path: str):
    raise NotImplementedError('copy read_arff from PA1 or reimplement')


def recode_labels(labels, task: str, source_path: str):
    """multiclass: unchanged. binary: see the PA6 ticket for the mapping rules."""
    raise NotImplementedError('binary recode for small vs wine files')


def scale_pair(query, pool, mode: str):
    """Fit scaler on pool only; return (scaled_query, scaled_pool)."""
    raise NotImplementedError('none / zscore / minmax without the query in the fit')


def knn_loo(features, labels, k: int, metric: int, p: float, normalize: str):
    raise NotImplementedError('leave-one-out with per-query scaling')


def confusion_matrix(y_true, y_pred):
    raise NotImplementedError


def write_report(path: str, settings: dict, elapsed: float, matrix) -> None:
    dest = Path(path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    lines = ['# PA6 scaled kNN', '', '## Settings', '']
    for key, value in settings.items():
        lines.append(f'- **{key}:** {value}')
    lines.extend(['', f'## Elapsed time', '', f'{elapsed:.4f} s', '', '## Confusion matrix', '', str(matrix), '', '## Comparison', '', '(write the PA6 comparisons here)', ''])
    dest.write_text('\n'.join(lines))


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
    started = time.perf_counter()
    features, labels = read_arff(args.data)
    labels = recode_labels(labels, args.task, args.data)
    y_true, y_pred = knn_loo(features, labels, args.k, args.distance, args.p, args.normalize)
    matrix = confusion_matrix(y_true, y_pred)
    elapsed = time.perf_counter() - started
    write_report(
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
