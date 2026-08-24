# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""PA5: prequential window. Predict with PA6.ScaledKNN.predict_one; score with PA2."""
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


class OnlineKNN(PA6.ScaledKNN):
    """Sliding-window kNN. Memory is the last `window` labeled instances."""

    def __init__(self, k: int = 3, distance: int = 1, p: float = 3.0, normalize: str = 'none', window: int = 50, weighted_vote: bool = False):
        super().__init__(k=k, distance=distance, p=p, normalize=normalize)
        if window < 1:
            raise ValueError('window must be >= 1')
        self.window = window
        self.weighted_vote = weighted_vote

    def vote(self, neighbor_labels: list, neighbor_weights: list | None = None) -> str:
        raise NotImplementedError('uniform majority, or inverse-frequency weights when flagged')

    def run_stream(self, features, labels):
        """Prequential: predict, then append; drop the oldest when over window."""
        raise NotImplementedError


def parse_args():
    parser = argparse.ArgumentParser(description='PA5 online sliding-window kNN')
    parser.add_argument('data')
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--window', type=int, default=50)
    parser.add_argument('--normalize', default='none', choices=('none', 'zscore', 'minmax'))
    parser.add_argument('--weighted-vote', action='store_true', help='inverse class frequency in the window')
    parser.add_argument('--output', default='output_online.md')
    return parser.parse_args()


def main():
    args = parse_args()
    started = time.perf_counter()
    model = OnlineKNN(k=args.k, normalize=args.normalize, window=args.window, weighted_vote=args.weighted_vote)
    features, labels = model.read_arff(args.data)
    results = model.run_stream(features, labels)
    reporter = PA2.ReportingKNN(k=args.k, normalize=args.normalize)
    elapsed = time.perf_counter() - started
    Path(args.output).write_text(
        '\n'.join(
            [
                '# PA5 online kNN',
                '',
                f'- data: {args.data}',
                f'- k: {args.k}',
                f'- window: {args.window}',
                f'- normalize: {args.normalize}',
                f'- weighted_vote: {args.weighted_vote}',
                f'- elapsed_s: {elapsed:.4f}',
                f'- results: {results}',
                f'- reporter_ready: {reporter.__class__.__name__}',
                '',
                '## Discussion',
                '',
                '(window size, drift, weighted vs uniform — see the PA5 ticket)',
                '',
            ]
        )
    )
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
