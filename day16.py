from typing import Tuple, List, Callable
import numpy as np

versions_sum = 0

type_to_fn = {
    0: sum,
    1: np.prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}


def parse():
    with open('data/input_16.txt', 'r') as f:
        return f.readline()


def hex_to_bin(hexadecimal: str) -> str:
    binary = str(bin(int(hexadecimal, 16)))[2:]
    return binary.zfill(len(binary) + (-len(binary) % 4))


def bin_to_int(binary: str) -> int:
    return int(binary, 2)


def cut(string: str, n: int) -> Tuple[str, str]:
    return string[:n], string[n:]


def parse_bits(binary: str, n: int) -> Tuple[int, str]:
    left, right = cut(binary, n)
    return bin_to_int(left), right


def parse_groups(binary: str, accumulated_bits: str) -> Tuple[int, str]:
    group_type, binary = parse_bits(binary, 1)
    if group_type == 0:
        group_bits, binary = cut(binary, 4)
        all_bits = accumulated_bits + group_bits
        return bin_to_int(all_bits), binary
    group_bits, binary = cut(binary, 4)
    return parse_groups(binary, accumulated_bits + group_bits)


def parse_literal(binary: str) -> Tuple[int, str]:
    return parse_groups(binary, '')


def parse_operands(binary: str, packets: int = None, bits: int = None) -> Tuple[List[int], str]:
    def parse_subpackets(binary: str, packets: int) -> Tuple[List[int], str]:
        if not packets:
            return [], binary
        value, binary = parse_packet(binary)
        rest_values, binary = parse_subpackets(binary, packets - 1)
        return [value] + rest_values, binary

    def parse_bits(binary: str, bits: int) -> Tuple[List[int], str]:
        if not bits:
            return [], binary
        value, rest_binary = parse_packet(binary)
        rest_values, binary = parse_bits(rest_binary, bits - (len(binary) - len(rest_binary)))
        return [value] + rest_values, binary

    if packets:
        return parse_subpackets(binary, packets)
    return parse_bits(binary, bits)


def parse_operator(binary: str, fn: Callable) -> Tuple[int, str]:
    length_type_id, binary = parse_bits(binary, 1)
    if length_type_id == 0:
        size, binary = parse_bits(binary, 15)
        values, binary = parse_operands(binary, bits=size)
    else:
        subpackets, binary = parse_bits(binary, 11)
        values, binary = parse_operands(binary, packets=subpackets)
    return fn(values), binary


def parse_packet(binary: str) -> Tuple[int, str]:
    version, binary = parse_bits(binary, 3)
    global versions_sum
    versions_sum += version
    type_id, binary = parse_bits(binary, 3)
    if type_id == 4:
        return parse_literal(binary)
    return parse_operator(binary, type_to_fn[type_id])


def main():
    hexadecimal = parse()
    binary = hex_to_bin(hexadecimal)
    value = parse_packet(binary)
    print(value)
    print(versions_sum)


if __name__ == '__main__':
    main()
