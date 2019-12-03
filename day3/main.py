first_wire = ['R8', 'U5', 'L5', 'D3']
second_wire = ['U7', 'R6', 'D4', 'L4']


def wire_path(wire):
    path = {}
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
            path[(x, y)] = count

    return path


def part1(first_wire, second_wire):
    path_first = wire_path(first_wire)
    path_second = wire_path(second_wire)
    inter = [abs(i[0]) + abs(i[1]) for i in path_first.keys() if i in path_second]

    return min(inter)


def part2(first_wire, second_wire):
    path_first = wire_path(first_wire)
    path_second = wire_path(second_wire)
    inter = [path_first[i] + path_second[i] for i in path_first.keys() if i in path_second]

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
