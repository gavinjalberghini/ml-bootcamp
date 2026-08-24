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
        # sudo:
        #   for each query row i
        #       pool := every row except i
        #       for each member
        #           draw a same-size pile from the pool, with repeats allowed
        #           ask ScaledKNN.predict_one on that pile
        #       ensemble guess := vote over members
        #   also keep each member's guesses so you can see if they disagree
        raise NotImplementedError('bootstrap sample the leave-one-out pool')

    def distance_committee_loo(self, features, labels):
        """Euclidean + Manhattan + Minkowski majority vote, each a ScaledKNN."""
        # sudo:
        #   three siblings, three notions of "near"
        #   each sibling sees the same leave-one-out pool
        #   final guess := vote of the three
        raise NotImplementedError

    def stretch_feature_subspace(self, features, labels, members: int, seed: int):
        """Optional stretch. Later tickets never call this."""
        # sudo:
        #   same bagging idea, but each member also sees only some of the columns
        raise NotImplementedError('optional stretch — skip unless you want the challenge')


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
