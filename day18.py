from aocutils import get_lines

from math import ceil
from copy import deepcopy
from itertools import permutations

def problem1():
    numbers = [parse_input(InputString(line)) for line in get_lines(0)]
    total = numbers.pop(0)
    reduce(total)
    for number in numbers:
        total = reduce(add(total, number))
    return magnitude(total)

def problem2():
    numbers = [parse_input(InputString(line)) for line in get_lines(18)]
    return max(magnitude(reduce(add(deepcopy(num1), deepcopy(num2)))) for num1, num2 in permutations(numbers, 2))

def parse_input(s):
    pair = []
    while True:
        match s.pop():
            case '[':
                pair.append(parse_input(s))
            case ']':
                return pair
            case ',':
                continue
            case num:
                pair.append(int(num))

def reduce(pair):
    while explode(pair) or split(pair):
        pass
    return pair

def explode(pair, depth=0):
    if depth == 3:
        for i in range(2):
            if isinstance(pair[i], list):
                removed = pair[i]
                pair[i] = 0
                if isinstance(pair[~i], list):
                    add_to_side(pair[~i], removed[~i], i)
                else:
                    pair[~i] += removed[~i]
                removed[~i] = 0
                return removed
    else:
        for i in range(2):
            removed = None
            if isinstance(pair[i], list) and (removed := explode(pair[i], depth + 1)):
                if isinstance(pair[~i], list):
                    add_to_side(pair[~i], removed[~i], i)
                else:
                    pair[~i] += removed[~i]
                removed[~i] = 0
                return removed

def split(pair):
    for i in range(2):
        if isinstance(pair[i], int) and pair[i] >= 10:
            new_pair = [pair[i] // 2, ceil(pair[i] / 2)]
            pair[i] = new_pair
            return True
        elif isinstance(pair[i], list) and split(pair[i]):
            return True
            
def magnitude(pair):
    if isinstance(pair, int):
        return pair
    else:
        return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])

def add_to_side(pair, value, side):
    if isinstance(pair[side], int):
        pair[side] += value
    else:
        add_to_side(pair[side], value, side)

def add(a, b):
    return [a, b]

class InputString:

    def __init__(self, s):
        self.s = s
        self.pop()

    def pop(self, n=1):
        chars = self.s[:n]
        self.s = self.s[n:]
        return chars