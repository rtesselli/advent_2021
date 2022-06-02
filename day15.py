import numpy as np
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


def parse():
    lines = np.loadtxt('data/input_15.txt', dtype=str)
    return np.array(
        [
            list(line)
            for line in lines
        ],
        dtype=int
    )


def expand_matrix(matrix):
    def increment(matrix):
        matrix += 1
        matrix %= 10
        matrix[matrix == 0] = 1
        return matrix

    orig_rows, orig_cols = matrix.shape
    out = np.empty((orig_rows * 5, orig_cols * 5))
    row_matrix = np.array(matrix)
    for row in range(5):
        matrix = np.array(row_matrix)
        for col in range(5):
            out[orig_rows * row: orig_rows * (row + 1), orig_cols * col: orig_cols * (col + 1)] = matrix
            matrix = increment(matrix)
        row_matrix = increment(row_matrix)
    return out


def pathfinder(matrix):
    grid = Grid(matrix=matrix)
    start = grid.node(0, 0)
    end = grid.node(matrix.shape[0] - 1, matrix.shape[1] - 1)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    return sum(matrix[row, col] for col, row in path) - matrix[0, 0]


def main():
    matrix = parse()
    print(pathfinder(matrix))
    matrix = expand_matrix(matrix)
    print(pathfinder(matrix))


if __name__ == '__main__':
    main()
