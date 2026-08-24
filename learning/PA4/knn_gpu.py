#!/usr/bin/env python3
"""PA4: vectorized / GPU kNN. Array library allowed for distances; logic stays yours."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def gpu_available() -> bool:
    try:
        import cupy  # noqa: F401
        return True
    except Exception:
        return False


def read_arff(path: str):
    raise NotImplementedError


def pairwise_distances(queries, pool, xp):
    """Vectorized distances using xp (numpy or cupy). No Python pair loop."""
    raise NotImplementedError


def knn_loo(features, labels, k: int, normalize: str, use_gpu: bool):
    raise NotImplementedError('same protocol as PA1/PA6; array distances')


def parse_args():
    parser = argparse.ArgumentParser(description='PA4 GPU kNN')
    parser.add_argument('data')
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--normalize', default='none', choices=('none', 'zscore', 'minmax'))
    parser.add_argument('--output', default='output_gpu.md')
    return parser.parse_args()


def main():
    args = parse_args()
    started = time.perf_counter()
    features, labels = read_arff(args.data)
    used_gpu = gpu_available()
    y_true, y_pred, backend = knn_loo(features, labels, args.k, args.normalize, used_gpu)
    elapsed = time.perf_counter() - started
    Path(args.output).write_text(
        '\n'.join(
            [
                '# PA4 GPU kNN',
                '',
                f'- data: {args.data}',
                f'- k: {args.k}',
                f'- normalize: {args.normalize}',
                f'- gpu_available: {used_gpu}',
                f'- backend: {backend}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- preds: {y_pred}',
                '',
            ]
        )
    )
    print(f'wrote {args.output} backend={backend}')


if __name__ == '__main__':
    main()
