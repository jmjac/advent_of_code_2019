from typing import Dict, List


def orbit_depth(center, bodies, orbit_numer, orbits):
    orbits[center] = orbit_numer
    for body in bodies.get(center, []):
        orbit_depth(body, bodies, orbit_numer + 1, orbits)


def get_orbits(pairs: List[str]) -> (Dict[str, int], Dict[str, str], str):
    bodies = {}
    seen = set()
    for pair in pairs:
        body, orbit = pair.split(")")
        seen.add(orbit)
        if body in bodies:
            bodies[body].append(orbit)
        else:
            bodies[body] = [orbit]

    center = (bodies.keys() - seen).pop()
    orbits = {}
    orbit_depth(center, bodies, 0, orbits)
    return orbits, bodies, center


def path_from_center(center, search, bodies):
    path = []
    while search != center:
        for body in bodies:
            if search in bodies[body]:
                search = body
                path.append(body)
    return path[::-1]


def part1(pairs: List[str]) -> int:
    return sum(get_orbits(pairs)[0].values())


def part2(pairs: List[str]) -> int:
    _, bodies, center = get_orbits(pairs)

    path_SAN = path_from_center(center, "SAN", bodies)
    path_YOU = path_from_center(center, "YOU", bodies)

    shared_planet = -1
    for i in range(len(path_YOU)):
        if path_SAN[i] != path_YOU[i]:
            shared_planet = i
            break

    return len(path_YOU[shared_planet:]) + len(path_SAN[shared_planet:])


with open("input.txt", "r") as file:
    lst = {i.replace("\n", "") for i in file.readlines()}

print(part1(lst))
print(part2(lst))
