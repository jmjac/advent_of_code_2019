def part1(low: int, top: int) -> int:
    count = 0
    for password in range(low, top):
        password = str(password)
        double = False

        for j in range(1, 6):
            if password[j] == password[j - 1]:
                double = True
            if password[j] < password[j - 1]:
                break
        else:
            if double:
                count += 1
    return count


def part2(low: int, top: int) -> int:
    count = 0
    for password in range(low, top):
        password = str(password)
        chars = {password[0]: 1}

        for j in range(1, 6):
            if password[j] in chars:
                chars[password[j]] += 1
            else:
                chars[password[j]] = 1
            if password[j] < password[j - 1]:
                break
        else:
            if 2 in chars.values():
                count += 1
    return count


low = 156218
top = 652527

print(part1(low, top))
print(part2(low, top))
