from aocutils import get_raw

def problem1():
    crabs = sorted([int(pos) for pos in get_raw(7).split(',')])
    mid = len(crabs) // 2
    align = (crabs[mid - 1] + crabs[mid]) // 2
    return sum(abs(pos - align) for pos in crabs)

def problem2():
    crabs = [int(pos) for pos in get_raw(7).split(',')]
    calc_fuel = lambda align: sum(abs(pos - align) * (abs(pos - align) + 1) / 2 for pos in crabs)
    prev = calc_fuel(0)
    for i in range(1, max(crabs)):
        new = calc_fuel(i)
        if new > prev:
            return int(prev)
        prev = new