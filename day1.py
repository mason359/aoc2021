from aocutils import get_nums

def problem1():
    nums = get_nums(1)
    return sum([b - a > 0 for a, b in zip(nums[:-1], nums[1:])])

def problem2():
    nums = get_nums(1)
    sums = [sum(triple) for triple in zip(nums[:-2], nums[1:-1], nums[2:])]
    return sum([b - a > 0 for a, b in zip(sums[:-1], sums[1:])])