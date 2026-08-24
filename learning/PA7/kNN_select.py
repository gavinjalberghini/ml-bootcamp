# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib>=3.8",
# ]
# ///
"""PA7: import PA6 for the model and PA2 for metrics. Do not copy those files."""
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


class SelectingKNN(PA6.ScaledKNN):
    """Hold out 20%, choose k on the rest, score the test slice, record vote fractions."""

    def split(self, features, labels, seed: int, test_frac: float = 0.2):
        raise NotImplementedError('shuffle with seed, return train_x, train_y, test_x, test_y')

    def predict_with_votes(self, query, pool_x, pool_y):
        """Return (hard_label, vote_fraction_of_winner). Scale using the pool only."""
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
    probe = SelectingKNN(k=1, distance=args.distance, p=args.p, normalize=args.normalize)
    features, labels = probe.read_arff(args.data)
    train_x, train_y, test_x, test_y = probe.split(features, labels, args.seed)
    reporter = PA2.ReportingKNN(k=1, distance=args.distance, p=args.p, normalize=args.normalize)
    grid = parse_k_grid(args.k_grid)
    scores = {}
    for k in grid:
        model = SelectingKNN(k=k, distance=args.distance, p=args.p, normalize=args.normalize)
        y_true, y_pred = model.leave_one_out(train_x, train_y)
        scores[k] = reporter.metrics_report(y_true, y_pred)
    # You choose k from scores[k]['macro_f1'] once that key exists.
    chosen = grid[0]
    final = SelectingKNN(k=chosen, distance=args.distance, p=args.p, normalize=args.normalize)
    preds, votes = [], []
    for query in test_x:
        label, frac = final.predict_with_votes(query, train_x, train_y)
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
                f'- validation_scores: {scores}',
                f'- chosen_k: {chosen}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- n_test: {len(test_y)}',
                f'- vote_fractions_head: {votes[:5]}',
                '',
                '## Discussion',
                '',
                '(answer the PA7 closing questions)',
                '',
            ]
        )
    )
    print(f'wrote {args.output}; placeholder chosen k={chosen}')


if __name__ == '__main__':
    main()
