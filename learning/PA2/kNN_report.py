#!/usr/bin/env python3
"""PA2: metrics, majority baseline, plots. Copy forward from PA6."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def read_arff(path: str):
    raise NotImplementedError('copy from PA1/PA6')


def knn_loo(features, labels, k: int, metric: int, p: float, normalize: str):
    raise NotImplementedError


def majority_baseline(labels):
    """Leave-one-out majority (or global majority). Return (y_true, y_pred)."""
    raise NotImplementedError('a classifier that does not look at features')


def metrics_report(y_true, y_pred):
    """Overall accuracy, macro/weighted P/R/F1, per-class P/R/F1/sensitivity/specificity."""
    raise NotImplementedError


def peak_memory_bytes() -> int:
    raise NotImplementedError('resource.getrusage or /proc/self/status')


def write_figures(outdir: Path, y_true, y_pred, baseline_pred) -> list[str]:
    """Confusion heatmap and per-class F1 bars. Return saved paths."""
    raise NotImplementedError('matplotlib')


def parse_args():
    parser = argparse.ArgumentParser(description='PA2 kNN report')
    parser.add_argument('data')
    parser.add_argument('--distance', type=int, default=1, choices=(1, 2, 3))
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--p', type=float, default=3.0)
    parser.add_argument('--normalize', default='none', choices=('none', 'zscore', 'minmax'))
    parser.add_argument('--output', default='output_report.md')
    return parser.parse_args()


def main():
    args = parse_args()
    started = time.perf_counter()
    features, labels = read_arff(args.data)
    y_true, y_pred = knn_loo(features, labels, args.k, args.distance, args.p, args.normalize)
    _, y_base = majority_baseline(labels)
    knn_metrics = metrics_report(y_true, y_pred)
    base_metrics = metrics_report(y_true, y_base)
    figures = write_figures(Path(args.output).parent, y_true, y_pred, y_base)
    elapsed = time.perf_counter() - started
    dest = Path(args.output)
    dest.write_text(
        '\n'.join(
            [
                '# PA2 report',
                '',
                f'- data: {args.data}',
                f'- k: {args.k}',
                f'- distance: {args.distance}',
                f'- normalize: {args.normalize}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- peak_memory: {peak_memory_bytes()}',
                f'- figures: {figures}',
                '',
                '## Majority baseline',
                '',
                str(base_metrics),
                '',
                '## kNN',
                '',
                str(knn_metrics),
                '',
                '## Discussion',
                '',
                '(answer the PA2 closing questions)',
                '',
            ]
        )
    )
    print(f'wrote {dest}')


if __name__ == '__main__':
    main()
