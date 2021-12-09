from aocutils import get_lines

from numpy import prod

NEIGHBORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def problem1():
    map = get_map()
    return sum(map[p[0]][p[1]] + 1 for p in get_low_points(map))

def problem2():
    map = get_map()
    points = get_low_points(map)
    return prod(sorted([get_basin_size(map, point) for point in points])[-3:])

def get_map():
    map = [[9] + [int(i) for i in line] + [9] for line in get_lines(9)]
    top = [[9] * len(map[0])]
    return top + map + top

def get_low_points(map):
    low_points = []
    for r in range(1, len(map) - 1):
        for c in range(1, len(map[0]) - 1):
            if all(map[r][c] < map[r + n[0]][c + n[1]] for n in NEIGHBORS):
                low_points.append((r, c))
    return low_points

def get_basin_size(map, start):
    visited = set()
    queue = [start]
    while queue:
        curr = queue.pop(0)
        if curr in visited:
            continue
        visited.add(curr)
        for n in NEIGHBORS:
            new = (curr[0] + n[0], curr[1] + n[1])
            if map[new[0]][new[1]] < 9:
                queue.append(new)
    return len(visited)