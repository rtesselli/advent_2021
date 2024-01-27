import numpy as np


def parse():
    def parse_line(line):
        left, right = line.strip().split(' -> ')
        return tuple(map(int, left.split(','))), tuple(map(int, right.split(',')))

    with open('data/input_05.txt', 'r') as f:
        lines = f.readlines()
    return list(map(parse_line, lines))


def straight_only(command):
    (x1, y1), (x2, y2) = command
    return x1 == x2 or y1 == y2


def draw(commands):
    def step(a, b):
        return 1 if a <= b else -1

    max_x = max(max(x1, x2) for (x1, y1), (x2, y2) in commands)
    max_y = max(max(y1, y2) for (x1, y1), (x2, y2) in commands)
    matrix = np.full((max_y + 1, max_x + 1), 0, dtype=int)
    for (x1, y1), (x2, y2) in commands:
        matrix[np.arange(y1, y2 + step(y1, y2), step(y1, y2)), np.arange(x1, x2 + step(x1, x2), step(x1, x2))] += 1
    return matrix


def main():
    commands = parse()
    straight_commands = list(filter(straight_only, commands))
    final_map = draw(straight_commands)
    print((np.sum(final_map > 1)))
    final_map = draw(commands)
    print((np.sum(final_map > 1)))


if __name__ == '__main__':
    main()
