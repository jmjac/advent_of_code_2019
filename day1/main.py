def fuel(a: int) -> int:
    return int(a / 3) - 2


def part1(lst: list):
    result = [fuel(i) for i in lst]
    return sum(result)


def part2(lst: list):
    result = []
    for i in lst:
        req = fuel(i)
        while req > 0:
            result.append(req)
            req = fuel(req)
    return sum(result)


lst = []
with open("input.txt", 'r') as file:
    for i in file.readlines():
        lst.append(int(i))

print(part1(lst))
print(part2(lst))
