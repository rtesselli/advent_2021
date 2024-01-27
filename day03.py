from typing import Callable
import numpy as np
import pandas as pd


def parse():
    all_bits = np.loadtxt('data/input_03.txt', dtype=str)
    return pd.DataFrame(
        [
            list(map(int, bits))
            for bits in all_bits
        ],
        dtype=bool
    )


def more_1s(values):
    return np.count_nonzero(values) >= len(values) / 2


def maximize(matrix: pd.DataFrame):
    counts = matrix.sum(axis=0)
    occurrences = len(matrix)
    return np.where(counts > occurrences / 2, 1, 0)


def minimize(matrix: pd.DataFrame):
    return 1 - maximize(matrix)


def bits_to_int(bits):
    return int("".join(map(str, bits)), 2)


def max_condition(values: pd.Series) -> pd.Series:
    return values == 1 if more_1s(values) else values == 0


def min_condition(values: pd.Series) -> pd.Series:
    return ~max_condition(values)


def find_row(data: pd.DataFrame, criteria: Callable):
    if data.empty:
        return
    selected = criteria(data.iloc[:, 0])
    if selected.sum() == 1:
        return selected.idxmax()
    return find_row(data.loc[selected, :].iloc[:, 1:], criteria)


def main():
    data = parse()
    maximized = maximize(data)
    minimized = minimize(data)
    print(bits_to_int(maximized) * bits_to_int(minimized))
    max_id = find_row(data, max_condition)
    min_id = find_row(data, min_condition)
    print(bits_to_int(data.loc[max_id, :].astype(int)) * bits_to_int(data.loc[min_id, :].astype(int)))


if __name__ == '__main__':
    main()
