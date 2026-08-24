#!/usr/bin/env python3
"""PA3: bagged kNN plus a three-distance committee. Copy forward from PA6."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def read_arff(path: str):
    raise NotImplementedError


def bagged_loo(features, labels, k: int, metric: int, p: float, normalize: str, members: int, seed: int):
    """Return ensemble preds and per-member preds. Query row never in a bag."""
    raise NotImplementedError('bootstrap sample the leave-one-out pool')


def distance_committee_loo(features, labels, k: int, p: float, normalize: str):
    """Euclidean + Manhattan + Minkowski majority vote."""
    raise NotImplementedError


def single_loo(features, labels, k: int, metric: int, p: float, normalize: str):
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
    features, labels = read_arff(args.data)
    single = single_loo(features, labels, args.k, args.distance, args.p, args.normalize)
    bagged, members = bagged_loo(
        features, labels, args.k, args.distance, args.p, args.normalize, args.members, args.seed
    )
    committee = distance_committee_loo(features, labels, args.k, args.p, args.normalize)
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
                '',
                f'- single: {single}',
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
