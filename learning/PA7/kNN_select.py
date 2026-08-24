#!/usr/bin/env python3
"""PA7: choose k on an 80% slice; score the 20% test set; record vote fractions."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def read_arff(path: str):
    raise NotImplementedError


def split(features, labels, seed: int, test_frac: float = 0.2):
    raise NotImplementedError('shuffle with seed, return train/test')


def loo_macro_f1(features, labels, k: int, metric: int, p: float, normalize: str) -> float:
    raise NotImplementedError


def predict_with_votes(train_x, train_y, query, k: int, metric: int, p: float, normalize: str):
    """Return (hard_label, vote_fraction_of_winner). Fit scaler on train only."""
    raise NotImplementedError


def parse_k_grid(text: str) -> list[int]:
    values = [int(part.strip()) for part in text.split(',') if part.strip()]
    if not values:
        raise SystemExit('--k-grid must list at least one integer')
    return values


def parse_args():
    parser = argparse.ArgumentParser(description='PA7 k selection and soft predictions')
    parser.add_argument('data')
    parser.add_argument('--k-grid', default='1,3,5,7,9')
    parser.add_argument('--distance', type=int, default=1, choices=(1, 2, 3))
    parser.add_argument('--p', type=float, default=3.0)
    parser.add_argument('--normalize', default='none', choices=('none', 'zscore', 'minmax'))
    parser.add_argument('--seed', type=int, default=5)
    parser.add_argument('--output', default='output_select.md')
    return parser.parse_args()


def main():
    args = parse_args()
    started = time.perf_counter()
    features, labels = read_arff(args.data)
    grid = parse_k_grid(args.k_grid)
    train_x, train_y, test_x, test_y = split(features, labels, args.seed)
    scores = {k: loo_macro_f1(train_x, train_y, k, args.distance, args.p, args.normalize) for k in grid}
    chosen = max(sorted(scores), key=lambda k: (scores[k], -k))
    preds, votes = [], []
    for query in test_x:
        label, frac = predict_with_votes(train_x, train_y, query, chosen, args.distance, args.p, args.normalize)
        preds.append(label)
        votes.append(frac)
    elapsed = time.perf_counter() - started
    Path(args.output).write_text(
        '\n'.join(
            [
                '# PA7 model selection',
                '',
                f'- data: {args.data}',
                f'- normalize: {args.normalize}',
                f'- k_grid: {grid}',
                f'- validation_macro_f1: {scores}',
                f'- chosen_k: {chosen}',
                f'- elapsed_s: {elapsed:.4f}',
                '',
                '## Test predictions',
                '',
                f'- n_test: {len(test_y)}',
                f'- vote_fractions: {votes[:5]} ...',
                '',
                '## Discussion',
                '',
                '(answer the PA7 closing questions)',
                '',
            ]
        )
    )
    print(f'wrote {args.output}; chosen k={chosen}')


if __name__ == '__main__':
    main()
