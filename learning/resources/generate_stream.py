# uv run learning/resources/generate_stream.py learning/resources/data/small.arff \
#     --output learning/resources/data/small_stream.arff
"""Build a drifting, imbalanced ARFF stream from a stationary dataset.

The generator keeps the same attributes and class values as the source file.
It resamples those instances (with light jitter) so the stream looks like the
data from the batch assignments, then applies a sudden real concept drift and
a change in class proportions at --drift.

This script is provided so you can inspect or regenerate the stream files.
Writing your own generator is optional, not required.
"""
import argparse
import math
import os
import random
from collections import Counter, defaultdict


def readArff(path):
    relation, attributes, comments = 'stream', [], []
    features, labels = [], []
    inData = False
    with open(path) as file:
        for raw in file:
            line = raw.strip()
            if not line:
                continue
            lower = line.lower()
            if lower.startswith('%'):
                if not inData:
                    comments.append(line)
                continue
            if lower.startswith('@relation'):
                relation = line.split(None, 1)[1].strip()
            elif lower.startswith('@attribute'):
                attributes.append(line)
            elif lower.startswith('@data'):
                inData = True
            elif inData and not lower.startswith('@'):
                values = line.split(',')
                features.append([float(v) for v in values[:-1]])
                labels.append(values[-1].strip())
    return relation, attributes, comments, features, labels


def classStats(features, labels):
    byClass = defaultdict(list)
    for feat, label in zip(features, labels):
        byClass[label].append(feat)
    counts = Counter(labels)
    dim = len(features[0])
    means, stds = [], []
    n = len(features)
    for j in range(dim):
        col = [row[j] for row in features]
        mean = sum(col) / n
        var = sum((x - mean) ** 2 for x in col) / n
        means.append(mean)
        stds.append(math.sqrt(var))
    return byClass, counts, means, stds


def defaultLabelMap(classes):
    """Swap the two most frequent classes, and the next two if they exist."""
    mapping = {label: label for label in classes}
    if len(classes) >= 2:
        mapping[classes[0]], mapping[classes[1]] = classes[1], classes[0]
    if len(classes) >= 4:
        mapping[classes[2]], mapping[classes[3]] = classes[3], classes[2]
    return mapping


def empiricalWeights(classes, counts):
    total = sum(counts[c] for c in classes)
    return {c: counts[c] / total for c in classes}


def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f'{n}{suffix}'


def shiftedWeights(classes, counts, minCommon=10):
    """Invert frequency among common classes so the old majority becomes rare.

    Classes with fewer than minCommon source examples keep their original
    share. Boosting those would just repeat two or three rows and stop
    looking like the dataset from PA1-PA4.
    """
    empirical = empiricalWeights(classes, counts)
    common = [c for c in classes if counts[c] >= minCommon]
    if len(common) < 2:
        return empirical
    inv = {c: 1.0 / counts[c] for c in common}
    invTotal = sum(inv.values())
    rareShare = sum(empirical[c] for c in classes if c not in common)
    commonShare = 1.0 - rareShare
    out = {}
    for c in classes:
        if c in common:
            out[c] = commonShare * (inv[c] / invTotal)
        else:
            out[c] = empirical[c]
    return out


def weightedChoice(weights, rng):
    pick = rng.random()
    running = 0.0
    items = list(weights.items())
    for label, weight in items[:-1]:
        running += weight
        if pick < running:
            return label
    return items[-1][0]


def jitterRow(row, stds, scale, rng):
    out = []
    for value, std in zip(row, stds):
        noise = rng.gauss(0.0, scale * std) if std > 0 else 0.0
        out.append(value + noise)
    return out


def formatWeightLine(weights, classes):
    return ', '.join(f'{c}={weights[c]:.4f}' for c in classes)


def formatMapLine(mapping, classes):
    return ', '.join(f'{c}->{mapping[c]}' for c in classes)


def writeStream(path, relation, attributes, metaLines, rows):
    with open(path, 'w') as file:
        for line in metaLines:
            file.write(line + '\n')
        file.write(f'@relation {relation}\n')
        for attr in attributes:
            file.write(attr + '\n')
        file.write('@data\n')
        for feat, label in rows:
            file.write(','.join(f'{v:.6g}' for v in feat) + f',{label}\n')


def parseArgs():
    parser = argparse.ArgumentParser(description='Generate a drifting ARFF stream from a stationary ARFF dataset')
    parser.add_argument('source', help='source ARFF (small.arff, medium.arff, or large.arff)')
    parser.add_argument('--output', required=True, help='destination ARFF path')
    parser.add_argument('--length', type=int, default=800, help='number of stream instances')
    parser.add_argument('--drift', type=int, default=400, help='first post-drift instance index (0-based). 0 disables drift')
    parser.add_argument('--seed', type=int, default=5, help='RNG seed')
    parser.add_argument('--jitter', type=float, default=0.05, help='jitter as a fraction of each feature std')
    parser.add_argument('--no-label-swap', action='store_true', help='keep original labels after the drift point')
    parser.add_argument('--no-reweight', action='store_true', help='keep original class proportions after the drift point')
    return parser.parse_args()


def main():
    args = parseArgs()
    if args.length < 1:
        raise SystemExit('--length must be at least 1')
    if args.drift < 0 or args.drift > args.length:
        raise SystemExit('--drift must be in [0, length]')

    relation, attributes, _, features, labels = readArff(args.source)
    byClass, counts, _means, stds = classStats(features, labels)
    classes = [c for c, _ in counts.most_common()]
    minCommon = max(10, int(0.05 * len(labels)))
    preWeights = empiricalWeights(classes, counts)
    postWeights = preWeights if args.no_reweight else shiftedWeights(classes, counts, minCommon=minCommon)
    labelMap = {c: c for c in classes} if args.no_label_swap else defaultLabelMap(classes)
    rng = random.Random(args.seed)

    rows = []
    for i in range(args.length):
        drifted = args.drift and i >= args.drift
        weights = postWeights if drifted else preWeights
        label = weightedChoice(weights, rng)
        sourceRow = rng.choice(byClass[label])
        feat = jitterRow(sourceRow, stds, args.jitter, rng)
        outLabel = labelMap[label] if drifted else label
        rows.append((feat, outLabel))

    postCounts = Counter(label for _, label in rows[args.drift:])
    preCounts = Counter(label for _, label in rows[:args.drift or args.length])
    streamRelation = relation if relation.endswith('_stream') else f'{relation}_stream'
    sourceName = os.path.basename(args.source)
    metaLines = [
        f'% drifting stream generated from {sourceName}',
        f'% seed: {args.seed}',
        f'% length: {args.length}',
        f'% sudden drift begins at instance {args.drift} (0-based; the {ordinal(args.drift + 1)} @data row)' if args.drift else '% no concept drift',
        f'% pre-drift class weights: {formatWeightLine(preWeights, classes)}',
        f'% post-drift class weights: {formatWeightLine(postWeights, classes)}',
        f'% post-drift label map: {formatMapLine(labelMap, classes)}',
        f'% pre-drift realized counts: {dict(sorted(preCounts.items()))}',
        f'% post-drift realized counts: {dict(sorted(postCounts.items()))}',
        '% jitter is gaussian noise at --jitter * feature std; class values match the source file',
        '% class codes are categories (see learning/resources/data/README.md); do not use them as features',
    ]
    writeStream(args.output, streamRelation, attributes, metaLines, rows)
    print(f'wrote {args.length} instances to {args.output}')
    print(f'drift index: {args.drift}')
    print(f'pre-drift counts: {dict(sorted(preCounts.items()))}')
    print(f'post-drift counts: {dict(sorted(postCounts.items()))}')
    print(f'label map: {formatMapLine(labelMap, classes)}')


if __name__ == '__main__':
    main()
