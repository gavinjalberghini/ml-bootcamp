# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""PA4: subclass PA6.ScaledKNN. Override distance work with array ops.

To use a GPU, add this line to the `dependencies` list above, then rerun
`uv run knn_gpu.py`:

    "cupy-cuda12x[ctk]>=13.0",

Leave the list empty to develop the vectorized CPU path first.
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

PA2 = import_pa('PA2')
PA6 = import_pa('PA6')


class GpuKNN(PA6.ScaledKNN):
    """Same leave-one-out protocol; distances computed as an array, not a pair loop."""

    def array_module(self):
        """Return cupy if it imports, else numpy. numpy is not required if you stay stdlib+lists."""
        raise NotImplementedError

    def pairwise_distances(self, queries, pool, xp):
        """Vectorized distances using xp. No Python loop over every pair."""
        raise NotImplementedError

    def leave_one_out(self, features, labels):
        raise NotImplementedError('use pairwise_distances; still exclude the query row')


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
    model = GpuKNN(k=args.k, normalize=args.normalize)
    features, labels = model.read_arff(args.data)
    y_true, y_pred = model.leave_one_out(features, labels)
    reporter = PA2.ReportingKNN(k=args.k, normalize=args.normalize)
    elapsed = time.perf_counter() - started
    Path(args.output).write_text(
        '\n'.join(
            [
                '# PA4 GPU kNN',
                '',
                f'- data: {args.data}',
                f'- k: {args.k}',
                f'- normalize: {args.normalize}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- metrics: {reporter.metrics_report(y_true, y_pred)}',
                '',
            ]
        )
    )
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
