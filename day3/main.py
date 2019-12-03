first_wire = ['R8', 'U5', 'L5', 'D3']
second_wire = ['U7', 'R6', 'D4', 'L4']


def wire_path(wire):
    history = {}
    x = 0
    y = 0
    count = 0

    dirs = {"R": 1,
            "L": -1,
            "U": 1,
            "D": -1}

    for i in wire:
        dir = i[0]
        mov = int(i[1:])
        for _ in range(mov):
            count += 1
            if dir in "RL":
                x += dirs[dir]
            else:
                y += dirs[dir]
            history[(x, y)] = count

    return history


def part1(first_wire, second_wire):
    hist_f = wire_path(first_wire)
    hist_s = wire_path(second_wire)
    inter = [abs(i[0]) + abs(i[1]) for i in hist_f.keys() if i in hist_s]

    return min(inter)


def part2(first_wire, second_wire):
    hist_f = wire_path(first_wire)
    hist_s = wire_path(second_wire)
    inter = [hist_f[i] + hist_s[i] for i in hist_f.keys() if i in hist_s]

    return min(inter)


# Test
first_wire = ['R8', 'U5', 'L5', 'D3']
second_wire = ['U7', 'R6', 'D4', 'L4']
assert (part1(first_wire, second_wire) == 6)
assert (part2(first_wire, second_wire) == 30)

with open("input.txt", 'r') as file:
    first_wire = [i for i in file.readline().split(',')]
    second_wire = [i for i in file.readline().split(',')]

print(part1(first_wire, second_wire))
print(part2(first_wire, second_wire))
