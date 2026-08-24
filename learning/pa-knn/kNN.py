# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""pa-knn: leave-one-out multiclass kNN. Stdlib only.

Later assignments import this module and subclass `KNN`. Keep the class name
and the method signatures. Fill in the TODOs; do not rename the class.
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path


class KNN:
    """Unscaled kNN. `distance` is 1=euclidean, 2=manhattan, 3=minkowski."""

    def __init__(self, k: int = 3, distance: int = 1, p: float = 3.0):
        if k < 1:
            raise ValueError('k must be >= 1')
        if distance not in (1, 2, 3):
            raise ValueError('distance must be 1, 2, or 3')
        self.k = k
        self.distance = distance
        self.p = p

    def read_arff(self, path: str):
        """Return (features, labels). Last column is the class, not a feature."""
        # sudo (not Python — rewrite this yourself):
        #   open the file
        #   ignore comment lines and header lines
        #   after the data marker, split each row
        #   last field -> label; other fields -> numbers
        #   give back (all number-rows, all labels)
        raise NotImplementedError('parse the ARFF file')

    def dist(self, a, b) -> float:
        # sudo:
        #   if metric is "straight line": root of summed squared gaps
        #   if metric is "city block": sum of absolute gaps
        #   if metric is "minkowski": (sum of |gap|^p) raised to 1/p
        raise NotImplementedError('euclidean / manhattan / minkowski')

    def vote(self, neighbor_labels: list) -> str:
        """Majority label. Document a deterministic tie-break in your report."""
        # sudo:
        #   count how often each label appears
        #   pick the most common
        #   if two labels tie, pick by a rule you can explain (and write down)
        raise NotImplementedError('majority vote')

    def predict_one(self, query, pool_x, pool_y) -> str:
        """Predict `query` from `pool_x` / `pool_y`. Query is not in the pool."""
        # sudo:
        #   score how far query is from every pool row
        #   keep the k closest rows
        #   vote among those rows' labels
        raise NotImplementedError('k nearest neighbors, then vote')

    def leave_one_out(self, features, labels):
        """For each row i, predict from all rows except i. Return (y_true, y_pred)."""
        # sudo:
        #   for each index i
        #       pool := every row except i
        #       pred := predict_one(row i, pool)
        #   give back (true labels, predicted labels)
        raise NotImplementedError('leave-one-out — exclude the query row')

    def confusion_matrix(self, y_true, y_pred):
        # sudo:
        #   list every class that appears
        #   make a grid: rows = truth, columns = guess
        #   increment the cell for each pair (truth, guess)
        raise NotImplementedError('labeled multiclass confusion matrix')

    def stretch_cosine(self, a, b) -> float:
        """Optional stretch. Later tickets never call this. Leave unimplemented if you skip it."""
        # sudo:
        #   cosine is about angle, not length
        #   think "how aligned" not "how far"
        raise NotImplementedError('optional stretch — skip unless you want the challenge')

    def write_report(self, path: str, settings: dict, elapsed: float, matrix) -> None:
        dest = Path(path)
        dest.parent.mkdir(parents=True, exist_ok=True)
        lines = [f'# {type(self).__name__}', '', '## Settings', '']
        for key, value in settings.items():
            lines.append(f'- **{key}:** {value}')
        lines.extend(
            [
                '',
                '## Elapsed time',
                '',
                f'{elapsed:.4f} s',
                '',
                '## Confusion matrix',
                '',
                str(matrix),
                '',
                '## Discussion',
                '',
                '(tie-break rule and any notes)',
                '',
            ]
        )
        dest.write_text('\n'.join(lines))


def parse_args():
    parser = argparse.ArgumentParser(description='pa-knn leave-one-out kNN')
    parser.add_argument('data', help='ARFF path')
    parser.add_argument('--distance', type=int, default=1, choices=(1, 2, 3), help='1=euclidean, 2=manhattan, 3=minkowski')
    parser.add_argument('--k', type=int, default=3)
    parser.add_argument('--p', type=float, default=3.0, help='Minkowski exponent')
    parser.add_argument('--output', default='output_knn.md')
    return parser.parse_args()


def main():
    args = parse_args()
    model = KNN(k=args.k, distance=args.distance, p=args.p)
    started = time.perf_counter()
    features, labels = model.read_arff(args.data)
    y_true, y_pred = model.leave_one_out(features, labels)
    matrix = model.confusion_matrix(y_true, y_pred)
    elapsed = time.perf_counter() - started
    model.write_report(
        args.output,
        {'data': args.data, 'k': args.k, 'distance': args.distance, 'p': args.p},
        elapsed,
        matrix,
    )
    print(f'wrote {args.output} in {elapsed:.4f}s')


if __name__ == '__main__':
    main()
