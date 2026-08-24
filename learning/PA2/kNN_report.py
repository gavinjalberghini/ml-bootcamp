# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib>=3.8",
# ]
# ///
"""PA2: subclass PA6.ScaledKNN. Add baseline, metrics, and plots.

matplotlib is declared in this file's script header. `uv run kNN_report.py`
installs it into a script environment. You do not need a project venv.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

LEARNING = Path(__file__).resolve().parent.parent
if str(LEARNING) not in sys.path:
    sys.path.insert(0, str(LEARNING))

from load_assignment import import_pa

PA6 = import_pa('PA6')


class ReportingKNN(PA6.ScaledKNN):
    """Scaled kNN plus evaluation helpers used by PA2, PA3, PA5, and PA7."""

    def majority_baseline(self, labels):
        """Leave-one-out majority (or global majority). Return (y_true, y_pred)."""
        raise NotImplementedError('a classifier that does not look at features')

    def metrics_report(self, y_true, y_pred) -> dict:
        """Accuracy, macro/weighted P/R/F1, per-class P/R/F1/sensitivity/specificity."""
        raise NotImplementedError

    def peak_memory_bytes(self) -> int:
        raise NotImplementedError('resource.getrusage or /proc/self/status')

    def write_figures(self, outdir: Path, y_true, y_pred, baseline_pred) -> list:
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
    model = ReportingKNN(k=args.k, distance=args.distance, p=args.p, normalize=args.normalize)
    started = time.perf_counter()
    features, labels = model.read_arff(args.data)
    y_true, y_pred = model.leave_one_out(features, labels)
    _, y_base = model.majority_baseline(labels)
    knn_metrics = model.metrics_report(y_true, y_pred)
    base_metrics = model.metrics_report(y_true, y_base)
    figures = model.write_figures(Path(args.output).parent, y_true, y_pred, y_base)
    elapsed = time.perf_counter() - started
    Path(args.output).write_text(
        '\n'.join(
            [
                '# PA2 report',
                '',
                f'- data: {args.data}',
                f'- k: {args.k}',
                f'- distance: {args.distance}',
                f'- normalize: {args.normalize}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- peak_memory: {model.peak_memory_bytes()}',
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
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
