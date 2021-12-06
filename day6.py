from aocutils import get_raw

def problem1():
    return simulate(80)

def problem2():
    return simulate(256)

def simulate(days):
    fish = [0] * 9
    for i in get_raw(6).split(','):
        fish[int(i)] += 1
    day_zero = 0
    for _ in range(days):
        new_fish = fish[day_zero]
        fish[day_zero] += fish[7]
        fish[7] = fish[8]
        fish[8] = new_fish
        day_zero = (day_zero + 1) % 7
    return sum(fish)