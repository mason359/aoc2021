from aocutils import get_raw

from itertools import combinations

def problem1():
    scanners, diffs, locations = parse_input()
    beacons = align_scanners(scanners, diffs, locations)
    return len(beacons)

def problem2():
    scanners, diffs, locations = parse_input()
    align_scanners(scanners, diffs, locations)
    locations = locations.pop()
    furthest = max(combinations(locations, 2), key=lambda pair: sum(abs(i2 - i1) for i1, i2 in zip(*pair)))
    return calc_distance(*furthest)

def parse_input():
    scanners = [set((tuple(int(i) for i in line.split(',')) for line in scanner.split('\n')[1:])) for scanner in get_raw(19).strip().split('\n\n')]
    diffs = get_diffs(scanners)
    locations = [[(0, 0, 0)] for _ in range(len(scanners))]
    return scanners, diffs, locations

def calc_distance(l1, l2):
    return sum(abs(i2 - i1) for i1, i2 in zip(l1, l2))

def align_scanners(scanners, diffs, locations):
    while len(scanners) > 1:
        i = 0
        while i < len(scanners):
            j = i + 1
            while j < len(scanners):
                if scanners[i] is scanners[j] or len(diffs[i] & diffs[j]) < 12:
                    j += 1
                    continue
                combined, new_locations = try_align(scanners[i], scanners[j], locations[j])
                if combined:
                    scanners[i] = combined
                    diffs[i] = calc_diff(scanners[i])
                    locations[i] += new_locations
                    del scanners[j]
                    del diffs[j]
                    del locations[j]
                else:
                    j += 1
            i += 1
    return scanners[0]  

def try_align(scanner1, scanner2, locations):
    for type in range(2):
        for i in range(3):
            for sign in range(4):
                transform = get_transform(type, i, sign)
                for beacon2 in scanner2:
                    for beacon1 in scanner1:
                        offset = subtract(transform(beacon2), beacon1)
                        new_scanner2 = set(subtract(transform(beacon), offset) for beacon in scanner2)
                        overlap = scanner1 & new_scanner2
                        if len(overlap) >= 12:
                            new_locations = [subtract(transform(location), offset) for location in locations]
                            return scanner1 | new_scanner2, new_locations
    return None, None

def subtract(t2, t1):
    return tuple(i2 - i1 for i1, i2 in zip(t1, t2))

def get_diffs(scanners):
    diffs = []
    for scanner in scanners:
        diffs.append(calc_diff(scanner))
    return diffs

def calc_diff(scanner):
    diffs = set()
    beacons = list(scanner)
    for i in range(len(beacons)):
        for j in range(i + 1, len(beacons)):
            diffs.add(tuple(sorted(abs(i) for i in subtract(beacons[j], beacons[i]))))
    return diffs

def get_transform(type, i, sign):
    cycle = lambda x, y, z: [(x, y, z), (y, z, x), (z, x, y)][i]
    swap = lambda x, y, z: [(y, x, -z), (x, z, -y), (z, y, -x)][i]
    signs = lambda x, y, z: [(x, y, z), (-x, -y, z), (-x, y, -z), (x, -y, -z)][sign]
    transform = lambda beacon: signs(*[cycle, swap][type](*beacon))
    return transform