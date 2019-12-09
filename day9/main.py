def vm(lst: list, user_input: list = [], loop_mode: bool = False, i: int = 0):
    results = []
    relative = 0
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

        C = get_value(C, i + 1, lst, relative)
        B = get_value(B, i + 2, lst, relative)
        A = get_value(A, i + 3, lst, relative)

        if opcode == 1:
            lst[A] = lst[C] + lst[B]
            i += 4
        elif opcode == 2:
            lst[A] = lst[C] * lst[B]
            i += 4
        elif opcode == 3:

            if user_input:
                inpt = user_input.pop(0)
            else:
                inpt = int(input())
            lst[C] = inpt
            i += 2
        elif opcode == 4:
            if loop_mode:
                return i + 2, lst, lst[C]
            else:
                print(lst[C])
            results.append(lst[C])
            i += 2
        elif opcode == 5:
            if lst[C] != 0:
                i = lst[B]
            else:
                i += 3
        elif opcode == 6:
            if lst[C] == 0:
                i = lst[B]
            else:
                i += 3
        elif opcode == 7:
            if lst[C] < lst[B]:
                val = 1
            else:
                val = 0
            lst[A] = val
            i += 4
        elif opcode == 8:

            if lst[C] == lst[B]:
                val = 1
            else:
                val = 0

            lst[A] = val
            i += 4
        elif opcode == 9:
            relative += lst[C]
            i += 2
        else:
            return -1
    return "Finished"


def get_value(mode, input, lst, relative):
    if mode == 0:
        return lst[input]
    elif mode == 1:
        return input
    elif mode == 2:
        return lst[input] + relative


def part1(lst):
    return vm(lst, user_input=[1])


def part2(lst):
    return vm(lst, user_input=[2])


with open("input.txt", "r") as file:
    lst = list(map(int, file.readline().split(',')))

lst = lst + [0 for i in range(100000)]

print(part1(lst.copy()))
print(part2(lst.copy()))
