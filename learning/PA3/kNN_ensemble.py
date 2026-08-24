# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""PA3: bag PA6.ScaledKNN members. Score with PA2.ReportingKNN.metrics_report."""
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


class EnsembleKNN(PA6.ScaledKNN):
    """Bagged kNN plus a three-distance committee. Query row never in a bag."""

    def bagged_loo(self, features, labels, members: int, seed: int):
        """Return ensemble preds and per-member preds."""
        raise NotImplementedError('bootstrap sample the leave-one-out pool')

    def distance_committee_loo(self, features, labels):
        """Euclidean + Manhattan + Minkowski majority vote, each a ScaledKNN."""
        raise NotImplementedError


def parse_args():
    parser = argparse.ArgumentParser(description='PA3 kNN ensembles')
    parser.add_argument('data')
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--distance', type=int, default=1, choices=(1, 2, 3))
    parser.add_argument('--p', type=float, default=3.0)
    parser.add_argument('--normalize', default='none', choices=('none', 'zscore', 'minmax'))
    parser.add_argument('--members', type=int, default=5)
    parser.add_argument('--seed', type=int, default=5)
    parser.add_argument('--output', default='output_ensemble.md')
    return parser.parse_args()


def main():
    args = parse_args()
    started = time.perf_counter()
    model = EnsembleKNN(k=args.k, distance=args.distance, p=args.p, normalize=args.normalize)
    features, labels = model.read_arff(args.data)
    reporter = PA2.ReportingKNN(k=args.k, distance=args.distance, p=args.p, normalize=args.normalize)
    y_true, y_single = model.leave_one_out(features, labels)
    bagged, members = model.bagged_loo(features, labels, args.members, args.seed)
    committee = model.distance_committee_loo(features, labels)
    elapsed = time.perf_counter() - started
    Path(args.output).write_text(
        '\n'.join(
            [
                '# PA3 ensembles',
                '',
                f'- data: {args.data}',
                f'- k: {args.k}',
                f'- normalize: {args.normalize}',
                f'- members: {args.members}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- single: {reporter.metrics_report(y_true, y_single)}',
                f'- bagged: {bagged}',
                f'- members: {members}',
                f'- distance_committee: {committee}',
                '',
                '## Discussion',
                '',
                '(answer the PA3 closing questions)',
                '',
            ]
        )
    )
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
