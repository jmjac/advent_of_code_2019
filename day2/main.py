with open("input.txt", 'r') as file:
    lst = [int(i) for i in file.readline().split(',')]


def part1(lst: list):
    lst[1] = 12
    lst[2] = 2

    return helper(lst)


def helper(lst: list):
    i = 0
    while lst[i] != 99:
        if lst[i] == 1:
            lst[lst[i + 3]] = lst[lst[i + 1]] + lst[lst[i + 2]]
        elif lst[i] == 2:
            lst[lst[i + 3]] = lst[lst[i + 1]] * lst[lst[i + 2]]
        else:
            return -1
        i += 4

    return lst[0]


def part2(lst):
    for i in range(1, 10000):
        for j in range(1, 10000):
            lst[1] = i
            lst[2] = j
            try:
                result = helper(lst.copy())
            except:
                continue
            if result == 19690720:
                return lst[1] * 100 + lst[2]


# lst = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
print(part1(lst.copy()))
print(part2(lst.copy()))
