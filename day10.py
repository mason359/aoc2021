from aocutils import get_lines

from functools import reduce

SCORES_P1 = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
SCORES_P2 = {'(': 1, '[': 2, '{': 3, '<': 4}
OPEN = {'(', '[', '{', '<'}
PAIRS = {')': '(', ']': '[', '}': '{', '>': '<'}

def problem1():
    return sum(SCORES_P1[get_invalid(line)] for line in get_lines(10))

def problem2():
    scores = sorted([get_score(line) for line in get_lines(10) if not get_invalid(line)])
    return scores[len(scores) // 2]

def get_invalid(line):
    stack = []
    for c in line:
        if c in OPEN:
            stack.append(c)
        elif stack.pop() != PAIRS[c]:
            return c
            
def get_score(line):
    stack = []
    for c in line:
        if c in OPEN:
            stack.append(c)
        else:
            stack.pop()
    return reduce(lambda total, c: total * 5 + SCORES_P2[c], reversed(stack), 0)
    