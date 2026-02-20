def input():
    moves = []
    with open("input.txt") as r:
        for line in r:
            line = line.strip()
            if len(line) == 0:
                continue
            d, n = line[0], line[1:]
            moves.append((d, int(n)))
    return moves

def output(result):
    with open("output.txt", "w") as w:
        w.write(str(result))

def password_part1(moves):
    position = 50
    password = 0
    for (d, n) in moves:
        if d == 'R':
            position += n
        else:
            position -= n
        position %= 100
        if position == 0:
            password += 1
    return password

def password_part2(moves):
    position = 50
    password = 0
    for (d, n) in moves:
        mul = 1
        if d == 'L':
            mul = -1

        for i in range(n):
            position += (mul * 1)
            position %= 100
            if position == 0:
                password += 1
    return password

def main():
    moves = input()
    # p = password_part1(moves)
    p = password_part2(moves)

    print("Result: ", p)
    output(p)

if __name__ == "__main__":
    main()
