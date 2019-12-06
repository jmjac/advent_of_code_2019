def part1(lst: list):
    return helper(lst)


def helper(lst: list):
    i = 0
    while lst[i] != 99:
        command = str(lst[i])
        opcode = int(command[-2:])
        A, B, C = 0, 0, 0

        if len(command) == 3:
            C = int(command[0])
        elif len(command) == 4:
            C = int(command[1])
            B = int(command[0])
        elif len(command) == 5:
            C = int(command[2])
            B = int(command[1])
            A = int(command[0])

        if opcode == 1:
            C = get_value(C, i + 1, lst)
            B = get_value(B, i + 2, lst)
            if A == 0:
                lst[lst[i + 3]] = C + B
            else:
                lst[lst[lst + 3]] = C + B
            i += 4
        elif opcode == 2:
            C = get_value(C, i + 1, lst)
            B = get_value(B, i + 2, lst)
            A = get_value(A, i + 3, lst)
            if A == 0:
                lst[lst[i + 3]] = C * B
            else:
                lst[lst[lst + 3]] = C * B
            i += 4
        elif opcode == 3:
            lst[lst[i + 1]] = int(input())
            i += 2
        elif opcode == 4:
            C = get_value(C, i + 1, lst)
            print(C)
            i += 2
        elif opcode == 5:
            C = get_value(C, i + 1, lst)
            B = get_value(B, i + 2, lst)
            if C != 0:
                i = B
            else:
                i += 3
        elif opcode == 6:
            C = get_value(C, i + 1, lst)
            B = get_value(B, i + 2, lst)
            if C == 0:
                i = B
            else:
                i += 3
        elif opcode == 7:
            C = get_value(C, i + 1, lst)
            B = get_value(B, i + 2, lst)
            if C < B:
                val = 1
            else:
                val = 0

            if A == 0:
                lst[lst[i + 3]] = val
            else:
                lst[lst[lst + 3]] = val
            i += 4
        elif opcode == 8:
            C = get_value(C, i + 1, lst)
            B = get_value(B, i + 2, lst)
            if C == B:
                val = 1
            else:
                val = 0

            if A == 0:
                lst[lst[i + 3]] = val
            else:
                lst[lst[lst + 3]] = val

            i += 4
        else:
            return -1

    return


def get_value(mode, input, lst):
    if (mode == 0):
        return lst[lst[input]]
    else:
        return lst[input]


with open("input.txt", "r") as file:
    lst = list(map(int, file.readline().split(',')))

print(part1(lst))
