from operator import itemgetter


def parse():
    def parse_line(line):
        left, right = line.split(' | ')
        return list(map(frozenset, left.split())), list(map(frozenset, right.split()))

    with open('data/input_08.txt', 'r') as f:
        lines = f.readlines()
    return list(map(parse_line, lines))


def count_simples(sequences):
    return sum(len(sequence) in {2, 4, 3, 7} for left, right in sequences for sequence in right)


def decode(sequences):
    def decode_one(sequences):
        def pair_number_sequence(number, sequence):
            sequence_to_number[sequence] = number
            number_to_sequence[number] = sequence

        sequence_to_number = {}
        number_to_sequence = {}
        for sequence in sequences:  # find numbers 1, 4, 7, 8
            if len(sequence) == 2:
                pair_number_sequence(1, sequence)
            elif len(sequence) == 4:
                pair_number_sequence(4, sequence)
            elif len(sequence) == 3:
                pair_number_sequence(7, sequence)
            elif len(sequence) == 7:
                pair_number_sequence(8, sequence)
        for sequence in sequences:  # find numbers 0, 6, 9
            if len(sequence) == 6:
                if not number_to_sequence[7] < sequence:
                    pair_number_sequence(6, sequence)
                elif number_to_sequence[4] < sequence:
                    pair_number_sequence(9, sequence)
                else:
                    pair_number_sequence(0, sequence)
        for sequence in sequences:  # find numbers 2, 3, 5
            if len(sequence) == 5:
                if sequence < number_to_sequence[6]:
                    pair_number_sequence(5, sequence)
                elif sequence < number_to_sequence[9]:
                    pair_number_sequence(3, sequence)
                else:
                    pair_number_sequence(2, sequence)
        return sequence_to_number

    sequences = list(map(itemgetter(0), sequences))
    return list(map(decode_one, sequences))


def score(sequences, all_sequence_to_number_maps):
    sequences = list(map(itemgetter(1), sequences))
    score = 0
    for sequence, sequence_to_number in zip(sequences, all_sequence_to_number_maps):
        number = "".join(str(sequence_to_number[set_]) for set_ in sequence)
        score += int(number)
    return score


def main():
    sequences = parse()
    print(count_simples(sequences))
    all_sequence_to_number_maps = decode(sequences)
    print(score(sequences, all_sequence_to_number_maps))


if __name__ == '__main__':
    main()
