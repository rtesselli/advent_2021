import numpy as np


def parse():
    lines = np.loadtxt('data/input_11.txt', dtype=str)
    return np.array(
        [
            list(line)
            for line in lines
        ],
        dtype=int
    )


def mask(matrix, row, col):
    mask = np.zeros_like(matrix, dtype=bool)
    mask[max(row - 1, 0): min(row + 2, matrix.shape[0]), max(col - 1, 0): min(col + 2, matrix.shape[1])] = True
    mask[row, col] = False
    return mask


def simulate(matrix: np.ndarray, steps):
    def step():
        nonlocal matrix
        matrix = (matrix + 1) % 10
        to_flash = {tuple(row) for row in np.argwhere(matrix == 0)}
        flashed = set()
        while to_flash:
            row, col = to_flash.pop()
            matrix[mask(matrix, row, col)] += 1
            matrix[mask(matrix, row, col)] %= 10
            flashed = flashed.union({(row, col)})
            new_to_flash = {tuple(row) for row in np.argwhere(matrix == 0)}
            to_flash = to_flash.union(new_to_flash)
            to_flash = to_flash - flashed
        for row, col in flashed:
            matrix[row, col] = 0
        return len(flashed)

    return sum(step() for _ in range(steps))


def find_all_flashed(matrix):
    def step():
        nonlocal matrix
        matrix = (matrix + 1) % 10
        to_flash = {tuple(row) for row in np.argwhere(matrix == 0)}
        flashed = set()
        while to_flash:
            row, col = to_flash.pop()
            matrix[mask(matrix, row, col)] += 1
            matrix[mask(matrix, row, col)] %= 10
            flashed = flashed.union({(row, col)})
            new_to_flash = {tuple(row) for row in np.argwhere(matrix == 0)}
            to_flash = to_flash.union(new_to_flash)
            to_flash = to_flash - flashed
        for row, col in flashed:
            matrix[row, col] = 0
        return len(flashed) == matrix.size

    step_number = 0
    while True:
        if step():
            return step_number + 1
        step_number += 1


def main():
    matrix = parse()
    flashes = simulate(matrix, 100)
    print(flashes)
    step = find_all_flashed(matrix)
    print(step)


if __name__ == '__main__':
    main()
