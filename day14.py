from aocutils import get_raw

from collections import defaultdict, Counter
from math import ceil

def problem1():
    return simulate(10)

def problem2():
    return simulate(40)

def simulate(steps):
    mapping, counts = parse_input()
    for _ in range(steps):
        counts = Counter({pair: sum(counts[starter] for starter in starters) for pair, starters in mapping.items()})
    return calc_answer(counts)

def parse_input():
    template, rules = get_raw(14).split('\n\n')
    mapping = defaultdict(list)
    for rule in rules.splitlines():
        pair, insert = rule.split(' -> ')
        mapping[pair[0] + insert].append(pair)
        mapping[insert + pair[1]].append(pair)
    counts = Counter()
    for i in range(len(template) - 1):
        counts[template[i:i + 2]] += 1
    return mapping, counts

def calc_answer(counts):
    elements = Counter()
    for pair, count in counts.items():
        elements[pair[0]] += count
        elements[pair[1]] += count
    return ceil((max(elements.values()) - min(elements.values())) / 2)