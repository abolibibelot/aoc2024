from collections import Counter


def read_file(file_path):
    return open(file_path, "r").read().splitlines()


test = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def part1():
    data = read_file("data/01.txt")

    # data = test.splitlines()
    xs = []
    ys = []
    for l in data:
        if l.strip():
            a, b = l.split()
            xs.append(int(a))
            ys.append(int(b))
    res = sum([abs(x - y) for x, y in zip(sorted(xs), sorted(ys))])
    print(res)


def part2():
    data = read_file("data/01.txt")

    # data = test.splitlines()
    xs = []
    ys = []
    for l in data:
        if l.strip():
            a, b = l.split()
            xs.append(int(a))
            ys.append(int(b))
    counter = Counter(ys)
    res = sum([x * counter.get(x, 0) for x in xs])
    print(res)


part1()
part2()
