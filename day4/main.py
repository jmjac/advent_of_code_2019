from typing import Dict, List


def get_combinations(low: int, top: int) -> List[Dict[str, int]]:
    combinations = []
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
            combinations.append(chars)
    return combinations


low = 156218
top = 652527

combinations = get_combinations(low, top)
part1 = sum([any(i >= 2 for i in comb.values()) for comb in get_combinations(low, top)])
part2 = sum([any(i == 2 for i in comb.values()) for comb in get_combinations(low, top)])

print(f"Part1: {part1}")
print(f"Part2: {part2}")
