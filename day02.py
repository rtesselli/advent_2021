def parse():
    with open('data/input_02.txt', 'r') as f:
        lines = f.readlines()
    return list(map(lambda x: x.split(' '), lines))


def follow(commands):
    horizontal, depth = 0, 0
    for command, step in commands:
        step = int(step)
        if command == 'forward':
            horizontal += step
        elif command == 'down':
            depth += step
        else:
            depth -= step
    return horizontal, depth


def follow_with_aim(commands):
    horizontal, depth, aim = 0, 0, 0
    for command, step in commands:
        step = int(step)
        if command == 'forward':
            horizontal += step
            depth += aim * step
        elif command == 'down':
            aim += step
        else:
            aim -= step
    return horizontal, depth


def main():
    commands = parse()
    horizontal, depth = follow(commands)
    print(horizontal * depth)
    horizontal, depth = follow_with_aim(commands)
    print(horizontal * depth)


if __name__ == '__main__':
    main()
