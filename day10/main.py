from _collections import defaultdict


def get_asteroids(lst):
    asteroids = []
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if lst[y][x] == "#":
                asteroids.append((y, x))
    return asteroids


def get_visible_asteroids(asteroids):
    visible = {}
    for y, x in asteroids:
        left = set()
        right = set()
        for y1, x1 in asteroids:
            if x == x1 and y == y1:
                continue

            if (x1 < x) or (x1 == x and y1 < y):
                side = left
            else:
                side = right
            if x1 == x:
                angle = float('inf')
            else:
                angle = (y1 - y) / (x1 - x)
            side.add(angle)
        visible[(y, x)] = len(left) + len(right)
    return visible


def part1(lst):
    asteroids = get_asteroids(lst)
    visible = get_visible_asteroids(asteroids)
    return max(visible.values())


def part2(lst):
    asteroids = get_asteroids(lst)
    visible = get_visible_asteroids(asteroids)
    for i in visible.keys():
        if visible[i] == max(visible.values()):
            y, x = i
            break

    asteroids_centered = [(y1 - y, x1 - x) for y1, x1 in asteroids]
    dist_l = defaultdict(list)
    dist_r = defaultdict(list)
    for y1, x1 in asteroids_centered:
        if x1 == 0 and y1 == 0:
            continue
        if x1 < 0:
            dist = dist_l
        else:
            dist = dist_r

        if x1 == 0:
            angle = y1 * float('inf')
        else:
            angle = y1 / x1

        dist[angle].append((y1, x1))

    for i in dist_r.keys():
        dist_r[i] = sorted(dist_r[i], key=lambda tupl: tupl[0] ** 2 + tupl[1] ** 2)
    for i in dist_l.keys():
        dist_l[i] = sorted(dist_l[i], key=lambda tupl: tupl[0] ** 2 + tupl[1] ** 2)

    vaporidez = []
    while any(dist_l.values()) or any(dist_r.values()):
        for i in sorted(dist_r.keys()):
            if dist_r[i]:
                vaporidez.append(dist_r[i].pop(0))
        for i in sorted(dist_l.keys()):
            if dist_l[i]:
                vaporidez.append(dist_l[i].pop(0))
    return (vaporidez[199][1] + x) * 100 + vaporidez[199][0] + y


with open("input.txt", 'r') as file:
    lst = [[j for j in i.replace("\n", "")] for i in file.readlines()]

print(part1(lst))
print(part2(lst))
