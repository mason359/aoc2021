from aocutils import get_lines

from collections import defaultdict

def problem1():
    map = parse_map()
    return count_paths(map, 'start', {'start'}, True)

def problem2():
    map = parse_map()
    return count_paths(map, 'start', {'start'}, False)

def parse_map():
    map = defaultdict(list)
    for line in get_lines(12):
        start, end = line.split('-')
        map[start].append(end)
        map[end].append(start)
    return map

def count_paths(map, curr, visited, has_returned):
    if curr == 'end':
        return 1
    paths = 0
    for cave in map[curr]:
        if cave.islower():
            if cave not in visited:
                paths += count_paths(map, cave, visited | {cave}, has_returned)
            elif not has_returned and cave != 'start':
                paths += count_paths(map, cave, visited, True)
        else:
            paths += count_paths(map, cave, visited, has_returned)
    return paths