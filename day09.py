import numpy as np
import scipy.ndimage


def parse():
    rows = np.loadtxt('data/input_09.txt', dtype=str)
    return np.array(
        [
            list(map(int, row))
            for row in rows
        ],
        dtype=int
    )


def find_mins(matrix):
    idxs = (
            (matrix < scipy.ndimage.shift(matrix, (1, 0), cval=10)) &
            (matrix < scipy.ndimage.shift(matrix, (-1, 0), cval=10)) &
            (matrix < scipy.ndimage.shift(matrix, (0, 1), cval=10)) &
            (matrix < scipy.ndimage.shift(matrix, (0, -1), cval=10))
    )
    return matrix[idxs], np.argwhere(idxs)


def find_basins(matrix, min_coordinates):
    def find_basin_size(matrix, visited, row, col, curr_size):
        def is_to_visit(row, col):
            if row < 0 or col < 0:
                return False
            if row >= matrix.shape[0] or col >= matrix.shape[1]:
                return False
            return matrix[row, col] != 9 and not visited[row, col]

        curr = matrix[row, col]
        left = matrix[row, col - 1] if col - 1 >= 0 else 9
        right = matrix[row, col + 1] if col + 1 < matrix.shape[1] else 9
        down = matrix[row + 1, col] if row + 1 < matrix.shape[0] else 9
        up = matrix[row - 1, col] if row - 1 >= 0 else 9
        visited[row, col] = True
        if not (is_to_visit(row, col - 1) or is_to_visit(row, col + 1) or is_to_visit(row + 1, col) or is_to_visit(
                row - 1, col)):
            return 1 + curr_size
        increments = 0
        if curr < left and is_to_visit(row, col - 1):
            increments += find_basin_size(matrix, visited, row, col - 1, curr_size)
        if curr < right and is_to_visit(row, col + 1):
            increments += find_basin_size(matrix, visited, row, col + 1, curr_size)
        if curr < down and is_to_visit(row + 1, col):
            increments += find_basin_size(matrix, visited, row + 1, col, curr_size)
        if curr < up and is_to_visit(row - 1, col):
            increments += find_basin_size(matrix, visited, row - 1, col, curr_size)
        return 1 + increments

    return [find_basin_size(matrix, np.zeros_like(matrix, dtype=bool), row, col, 0) for row, col in min_coordinates]


def main():
    matrix = parse()
    mins, coordinates = find_mins(matrix)
    print(np.sum(mins + 1))
    basin_sizes = find_basins(matrix, coordinates)
    print(np.prod(sorted(basin_sizes, reverse=True)[:3]))


if __name__ == '__main__':
    main()
