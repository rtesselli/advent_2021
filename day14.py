from more_itertools import pairwise
from collections import Counter


def parse():
    with open('data/input_14.txt', 'r') as f:
        all_lines = " ".join(f.readlines())
    sequence, rules = all_lines.split("\n \n")
    rules = dict([
        rule.strip().split(' -> ')
        for rule in rules.split('\n')
    ])
    return sequence, rules


def expand(sequence, rules, steps):
    def step(sequence):
        new_chars = [rules[first + second] for first, second in pairwise(sequence)]
        out = []
        for old, new in zip(sequence, new_chars):
            out += [old, new]
        out += sequence[-1]
        return "".join(out)

    for _ in range(steps):
        sequence = step(sequence)
    return sequence


def expand2(sequence, rules, steps):
    bigrams = Counter("".join(pair) for pair in pairwise(sequence))
    new_bigrams = Counter()
    for _ in range(steps):
        new_bigrams = Counter()
        for (left, right), count in bigrams.items():
            new_bigrams += Counter({left + rules["".join((left, right))]: count})
            new_bigrams += Counter({rules["".join((left, right))] + right: count})
        bigrams = Counter(new_bigrams)
    return new_bigrams


def score(sequence):
    counts = Counter(sequence)
    max_ = max(v for v in counts.values())
    min_ = min(v for v in counts.values())
    return max_ - min_


def score2(bigrams):
    counter = Counter(list(bigrams.keys())[0][0])
    for bigram, count in bigrams.items():
        counter += Counter({bigram[1]: count})

    return max(v for v in counter.values()) - min(v for v in counter.values())


def main():
    sequence, rules = parse()
    expanded = expand(sequence, rules, 4)
    print(score(expanded))


def main2():
    sequence, rules = parse()
    bigrams = expand2(sequence, rules, 40)
    print(score2(bigrams))


if __name__ == '__main__':
    main2()
