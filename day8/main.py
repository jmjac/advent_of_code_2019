def part1(inp: str) -> int:
    width = 25
    height = 6
    layers = [[int(i) for i in inp[i:i + width * height]] for i in range(0, len(inp), width * height)]

    few_zeros = [sum([1 for k in layer if k == 0]) for layer in layers]
    ones = [1 for i in layers[few_zeros.index(min(few_zeros))] if i == 1]
    twoes = [1 for i in layers[few_zeros.index(min(few_zeros))] if i == 2]
    return sum(ones) * sum(twoes)


def part2(inp: str) -> None:
    width = 25
    height = 6
    layers = [[int(i) for i in inp[i:i + width * height]] for i in range(0, len(inp), width * height)]

    final_image = [[-1 for _ in range(width)] for _ in range(height)]
    for layer in layers:
        h = 0
        w = 0
        for j in layer:
            if j != 2 and final_image[h][w] == -1:
                final_image[h][w] = j
            w += 1
            if w == width:
                w = 0
                h += 1

    [print(" ".join(map(str, i))) for i in final_image]


with open("input.txt", "r") as file:
    lst = file.readline()

print(part1(lst))
print(part2(lst))
