from more_itertools import windowed, pairwise


def parse(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return list(map(int, lines))


def count_increases(numbers):
    return sum(next_number > number for number, next_number in pairwise(numbers))


def count_windowed_increases(numbers):
    aggregated = list(map(sum, (windowed(numbers, 3))))
    return count_increases(aggregated)


def main():
    numbers = parse('data/input_01.txt')
    print(count_increases(numbers))
    print(count_windowed_increases(numbers))


if __name__ == '__main__':
    main()
