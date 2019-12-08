def vm(lst: list, user_input: list = [], loop_mode: bool = False, i: int = 0):
    results = []
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
            if A == 0:
                lst[lst[i + 3]] = C * B
            else:
                lst[lst[lst + 3]] = C * B
            i += 4
        elif opcode == 3:
            if user_input:
                lst[lst[i + 1]] = user_input.pop(0)
            else:
                lst[lst[i + 1]] = int(input())
            i += 2
        elif opcode == 4:
            C = get_value(C, i + 1, lst)
            if loop_mode:
                return i + 2, lst, C
            results.append(C)
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
    return results[-1]


def part1(lst):
    best = 0
    for A in range(5):
        for B in range(5):
            for C in range(5):
                for D in range(5):
                    for E in range(5):
                        if A in {B, C, D, E} or B in {C, D, E} or C in {D, E} or D in {E}:
                            continue
                        A_r = vm(lst.copy(), [A, 0], False)
                        B_r = vm(lst.copy(), [B, A_r], False)
                        C_r = vm(lst.copy(), [C, B_r], False)
                        D_r = vm(lst.copy(), [D, C_r], False)
                        E_r = vm(lst.copy(), [E, D_r], False)
                        if E_r > best:
                            best = E_r
    return best


def part2(lst):
    best = 0
    for A in range(5, 10):
        for B in range(5, 10):
            for C in range(5, 10):
                for D in range(5, 10):
                    for E in range(5, 10):
                        if A in {B, C, D, E} or B in {C, D, E} or C in {D, E} or D in {E}:
                            continue
                        A_i, A_lst, A_r = vm(lst.copy(), [A, 0], True, 0)
                        B_i, B_lst, B_r = vm(lst.copy(), [B, A_r], True, 0)
                        C_i, C_lst, C_r = vm(lst.copy(), [C, B_r], True, 0)
                        D_i, D_lst, D_r = vm(lst.copy(), [D, C_r], True, 0)
                        E_i, E_lst, E_r = vm(lst.copy(), [E, D_r], True, 0)
                        while True:
                            try:
                                A_i, A_lst, A_r = vm(A_lst, [E_r], True, A_i)
                                B_i, B_lst, B_r = vm(B_lst, [A_r], True, B_i)
                                C_i, C_lst, C_r = vm(C_lst, [B_r], True, C_i)
                                D_i, D_lst, D_r = vm(D_lst, [C_r], True, D_i)
                                E_i, E_lst, E_r = vm(E_lst, [D_r], True, E_i)
                            except:
                                if E_r > best:
                                    best = E_r
                                break
    return best


def get_value(mode, input, lst):
    if mode == 0:
        return lst[lst[input]]
    else:
        return lst[input]


with open("input.txt", "r") as file:
    lst = list(map(int, file.readline().split(',')))

print(part1(lst.copy()))
print(part2(lst.copy()))
