import numpy as np
import pandas as pd
import re
from typing import List
from more_itertools import sliced


def parse():
    with open('data/input_04.txt', 'r') as f:
        lines = f.readlines()
    numbers = list(map(int, lines.pop(0).split(',')))
    lines = list(map(str.strip, lines))
    lines = list(filter(bool, lines))
    lines = list(map(lambda x: re.split('\s+', x), lines))
    lines = list(map(lambda x: list(map(int, x)), lines))
    tables = [
        pd.DataFrame(rows, dtype=int)
        for rows in sliced(lines, 5)
    ]
    return numbers, tables


def call_number(number: int, tables: List[pd.DataFrame]):
    for table in tables:
        table[table == number] *= 1000


def check_wins(tables):
    winners = []
    for table in tables:
        if np.any(table.min(axis=0) >= 1000) or np.any(table.min(axis=1) >= 1000):
            table[table >= 1000] = 0
            winners.append(table.values.sum())
    return winners


def play(numbers, tables):
    for number in numbers:
        call_number(number, tables)
        winners = check_wins(tables)
        if winners:
            return winners[0] * number


def long_play(numbers, tables):
    total_tables = len(tables)
    for number in numbers:
        call_number(number, tables)
        winners = check_wins(tables)
        total_tables -= len(winners)
        if winners and total_tables == 1:
            return winners[0] * number


def main():
    numbers, tables = parse()
    print(play(numbers, tables))


def main2():
    numbers, tables = parse()
    print(long_play(numbers, tables))


if __name__ == '__main__':
    main2()
