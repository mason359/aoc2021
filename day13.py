from aocutils import get_raw

from functools import reduce

def problem1():
    points, folds = parse_input()
    return len(set(folds[0](point) for point in points) - {None})

def problem2():
    points, folds = parse_input()
    points = set(reduce(lambda p, T: T(p), folds, point) for point in points)
    print_paper(points)

def parse_input():
    points, folds = get_raw(13).split('\n\n')
    points = [tuple(int(i) for i in point.split(',')) for point in points.splitlines()]
    folds = [get_transform(*line.split()[2].split('=')) for line in folds.splitlines()]
    return points, folds

def get_transform(axis, line):
    line = int(line)

    def fold(point):
        if point is None:
            return None
        if axis == 'x':
            return (reflect(line, point[0]), point[1])
        else:
            return (point[0], reflect(line, point[1]))

    return fold

def reflect(line, value):
    if value > line:
        return 2 * line - value
    elif value < line:
        return value

def print_paper(points):
    maxx = max(points, key=lambda p: p[0])[0]
    maxy = max(points, key=lambda p: p[1])[1]
    for y in range(maxy + 1):
        line = ''
        for x in range(maxx + 1):
            if (x, y) in points:
                line += '█'
            else:
                line += ' '
        print(line)