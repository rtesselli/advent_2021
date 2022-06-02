def parse():
    with open('data/input_17.txt', 'r') as f:
        line = f.readline()
    line = line.removeprefix('target area: ')
    left, right = line.split(', ')
    xmin, xmax = left.split('=')[1].split('..')
    ymin, ymax = right.split('=')[1].split('..')
    return int(xmin), int(xmax), int(ymin), int(ymax)


def main():
    xmin, xmax, ymin, ymax = parse()
    print(xmin, xmax, ymin, ymax)


if __name__ == '__main__':
    main()
