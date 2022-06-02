import numpy as np


def parse():
    with open('data/input_13.txt', 'r') as f:
        all_lines = " ".join(f.readlines())
    coordinates, instructions = all_lines.split("\n \n")
    coordinates = list(map(lambda pair: pair.strip().split(','), coordinates.split(' ')))
    coordinates = list(map(lambda pair: (int(pair[1]), int(pair[0])), coordinates))
    instructions = list(map(lambda line: line.removeprefix(' fold along ').split('='), instructions.split('\n')))
    instructions = list(map(lambda pair: (pair[0], int(pair[1])), instructions))
    return coordinates, instructions


def fill_matrix(coordinates):
    max_row = max(row for row, col in coordinates) + 1
    max_col = max(col for row, col in coordinates) + 1
    matrix = np.zeros((max_row, max_col), dtype=bool)
    for row, col in coordinates:
        matrix[row, col] = True
    return matrix


def fold(matrix, instructions):
    for axis, position in instructions:
        if axis == 'y':
            up = matrix[:position, :]
            down = matrix[position + 1:, :]
            down = np.flip(down, axis=0)
            down = np.pad(down, ((up.shape[0] - down.shape[0], 0), (0, 0)), )
            matrix = up + down
        if axis == 'x':
            left = matrix[:, :position]
            right = matrix[:, position + 1:]
            right = np.flip(right, axis=1)
            right = np.pad(right, ((0, 0), (left.shape[1] - right.shape[1], 0)))
            matrix = left + right
    return matrix


def main():
    coordinates, instructions = parse()
    matrix = fill_matrix(coordinates)
    folded = fold(matrix, instructions[:1])
    print(np.sum(folded))
    matrix = fill_matrix(coordinates)
    folded = fold(matrix, instructions)
    print(folded)


if __name__ == '__main__':
    main()
