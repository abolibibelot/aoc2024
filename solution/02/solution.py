from collections import Counter


def read_file(file_path):
    return open(file_path, "r").read().splitlines()


test = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def sign(x):
    return -1 if x < 0 else 1


def with_hole(row):
    return [row[0:i] + row[i + 1 :] for i in range(len(row))]


def is_safe(row):
    diff = [x - y for x, y in zip(row, row[1:])]
    if len(diff) < 2:
        return False
    row_sign = sign(diff[0])
    safe = all([(sign(d) == row_sign and abs(d) > 0 and abs(d) < 4) for d in diff])
    return safe


def part1():
    data = read_file("data/02.txt")

    # data = test.splitlines()
    res = 0
    for l in data:
        if not l.strip():
            continue
        row = [int(x) for x in l.split()]
        safe = is_safe(row)
        res += 1 if safe else 0

    print(res)


def part2():
    data = read_file("data/02.txt")

    # data = test.splitlines()
    res = 0
    for l in data:
        if not l.strip():
            continue
        row = [int(x) for x in l.split()]
        if is_safe(row):
            res += 1
        else:
            if any([is_safe(r) for r in with_hole(row)]):
                res += 1
    print(res)


# part1()
part2()
