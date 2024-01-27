def parse():
    with open('data/input_10.txt', 'r') as f:
        lines = f.readlines()
    return list(map(str.strip, lines))


open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

close_to_open = {v: k for k, v in open_to_close.items()}


def find_corrupted(lines):
    def find_in_line(line):
        stack = []
        for bracket in line:
            if bracket in open_to_close.keys():
                stack.append(bracket)
            else:
                last_open_bracket = stack.pop()
                if last_open_bracket != close_to_open[bracket]:
                    return bracket

    errors = []
    not_corrupted = []
    for line in lines:
        line_errors = find_in_line(line)
        if line_errors:
            errors.append(line_errors)
        else:
            not_corrupted.append(line)
    return errors, not_corrupted


def score_errors(errors):
    close_to_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    return sum(close_to_score[bracket] for bracket in errors)


def autocomplete(lines):
    def autocomplete_line(line):
        stack = []
        for bracket in line:
            if bracket in open_to_close.keys():
                stack.append(bracket)
            else:
                stack.pop()
        return "".join(open_to_close[bracket] for bracket in reversed(stack))

    return [autocomplete_line(line) for line in lines]


def autocomplete_scores(completions):
    def score_completion(completion):
        close_to_score = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }
        out = 0
        for bracket in completion:
            out *= 5
            out += close_to_score[bracket]
        return out

    scores = sorted(score_completion(completion) for completion in completions)
    return scores[len(scores) // 2]


def main():
    lines = parse()
    errors, not_corrupted = find_corrupted(lines)
    print(score_errors(errors))
    completions = autocomplete(not_corrupted)
    score = autocomplete_scores(completions)
    print(score)


if __name__ == '__main__':
    main()
