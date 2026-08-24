#!/usr/bin/env python3
"""PA5: prequential sliding-window kNN. Stdlib only for the model."""
from __future__ import annotations

import argparse
import time
from pathlib import Path


def read_arff(path: str):
    raise NotImplementedError


def predict_one(window_x, window_y, query, k: int, weighted: bool, normalize: str):
    """Predict using only the current window. Fit any scaler on the window."""
    raise NotImplementedError


def run_stream(features, labels, k: int, window: int, weighted: bool, normalize: str):
    """Prequential loop: predict, then append; drop the oldest when over window."""
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
    features, labels = read_arff(args.data)
    results = run_stream(features, labels, args.k, args.window, args.weighted_vote, args.normalize)
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
