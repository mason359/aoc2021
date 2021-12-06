from aocutils import get_lines

from itertools import chain, combinations

def problem1():
    horz, vert, _, _ = parse_lines()
    return count_intersections(horz + vert)

def problem2():
    horz, vert, neg, pos = parse_lines()
    return count_intersections(horz + vert + neg + pos)

def parse_lines():
    endpoints = [[[int(num) for num in pair.split(',')] for pair in line.split(' -> ')] for line in get_lines(5)]
    horz = [((x1, y1), (x2, y2)) for ((x1, y1), (x2, y2)) in endpoints if y1 == y2]
    vert = [((x1, y1), (x2, y2)) for ((x1, y1), (x2, y2)) in endpoints if x1 == x2]
    neg = [((x1, y1), (x2, y2)) for ((x1, y1), (x2, y2)) in endpoints if (x1 > x2) != (y1 > y2) and x1 != x2 and y1 != y2]
    pos = [((x1, y1), (x2, y2)) for ((x1, y1), (x2, y2)) in endpoints if (x1 > x2) == (y1 > y2) and x1 != x2 and y1 != y2]
    horz = [set([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]) for [[x1, y1], [x2, y2]] in horz] 
    vert = [set([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]) for [[x1, y1], [x2, y2]] in vert]
    neg = [set(zip(range(min(x1, x2), max(x1, x2) + 1), reversed(range(min(y1, y2), max(y1, y2) + 1)))) for [[x1, y1], [x2, y2]] in neg]
    pos = [set(zip(range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1))) for [[x1, y1], [x2, y2]] in pos]
    return horz, vert, neg, pos

def count_intersections(lines):
    return len(set(chain.from_iterable(line1 & line2 for line1, line2 in combinations(lines, 2))))