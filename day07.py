import numpy as np


def parse():
    with open('data/input_07.txt', 'r') as f:
        line = f.readline()
    return list(map(int, line.split(',')))


def int_sum(n):
    return n * (n + 1) // 2


def optimize(positions, progressive=False):
    positions = np.array(positions)
    delta_matrix = np.abs(positions[:, np.newaxis] - positions[np.newaxis, :])
    if progressive:
        delta_matrix = int_sum(delta_matrix)
    costs = delta_matrix.sum(axis=0)
    return costs.min()


def main():
    positions = parse()
    total_fuel = optimize(positions)
    print(total_fuel)
    total_fuel = optimize(positions, progressive=True)
    print(total_fuel)


if __name__ == '__main__':
    main()
