from collections import Counter
from more_itertools import pairwise


def parse():
    with open('data/input_06.txt', 'r') as f:
        line = f.readline()
    return list(map(int, line.split(',')))


def simulate(state, days):
    counts = Counter(state)
    for _ in range(days):
        newborns = counts[0]
        for day_set, next_day_set in pairwise(range(9)):
            counts[day_set] = counts[next_day_set]
        counts[8] = newborns
        counts[6] += newborns
    return sum(counts.values())


def main():
    state = parse()
    total = simulate(state, days=80)
    print(total)
    state = parse()
    total = simulate(state, days=256)
    print(total)


if __name__ == '__main__':
    main()
