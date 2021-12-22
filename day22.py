from aocutils import get_lines

from dataclasses import dataclass
from functools import reduce

def problem1():
    return reboot(small_region=True)

def problem2():
    return reboot()

def reboot(small_region=False):
    cubes = parse_input(small_region)
    regions = []
    total_on = 0
    for cube in cubes:
        total_on += run_step(cube, regions)
    print(len(regions))
    return total_on

def run_step(cube, regions):
    total_on = 0
    for i in range(len(regions)):
        if intersection := intersect(regions[i], cube):
            regions.append(intersection)
            total_on += intersection.volume()
    if cube.on:
        total_on += cube.volume()
        regions.append(cube)
    return total_on

def intersect(cube1, cube2):
    mins = tuple(max(min1, min2) for min1, min2 in zip(cube1.lower, cube2.lower))
    maxs = tuple(min(max1, max2) for max1, max2 in zip(cube1.upper, cube2.upper))
    if all(mini <= maxi for mini, maxi in zip(mins, maxs)):
        return Cube(mins, maxs, not cube1.on)

def parse_input(small_region):
    cubes = []
    for line in get_lines(22):
        action, rest = line.split()
        mins, maxs = [], []
        bounds = [0] * 3
        bounds[0], rest = rest[2:].split(',y=')
        bounds[1:] = rest.split(',z=')
        for bound in bounds:
            mini, maxi = bound.split('..')
            mins.append(int(mini))
            maxs.append(int(maxi))
        if small_region and any(abs(mini) > 50 or abs(maxi) > 50 for mini, maxi in zip(mins, maxs)):
            break
        cubes.append(Cube(tuple(mins), tuple(maxs), action == 'on'))
    return cubes

@dataclass
class Cube:
    lower: tuple
    upper: tuple
    on: bool

    def volume(self):
        return reduce(lambda v, i: v * (self.upper[i] + 1 - self.lower[i]), range(3), 1) * (1 if self.on else -1)