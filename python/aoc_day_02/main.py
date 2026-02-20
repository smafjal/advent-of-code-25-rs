def input():
    ranges = []
    with open("input.txt") as r:
        line = r.read()
        parts = line.strip().split(",")
        for p in parts:
            ranges.append((p.split("-")))
    return ranges

def isRepeat1(x):
    xstr = str(x)
    l = len(xstr)
    if 2 * xstr[:l//2] == xstr:
        return True

    return False

def isRepeat2(x):
    xstr = str(x)
    l = len(xstr)
    for r in range(2, len(xstr) + 1):
        if r * xstr[:l//r] == xstr:
            return True
    return False

def sol(ranges):
    total = 0
    for (start, end) in ranges:
        start = int(start)
        end = int(end)
        for i in range(start, end+1):
            # if isRepeat1(i):
                # total += i
            if isRepeat2(i):
                total += i
    return total

def main():
    ranges = input()
    result = sol(ranges)
    print("Result: ", result)

    # isRepeat(919191)


if __name__ == "__main__":
    main()
