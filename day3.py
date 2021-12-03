from aocutils import get_lines

def problem1():
    lines = get_lines(3)
    bits = len(lines[0]) - 1
    nums = [int(num, 2) for num in lines]
    gamma = 0
    for i in range(bits - 1, -1, -1):
        gamma = (gamma << 1) + int(sum([(num >> i) % 2 for num in nums]) > (len(nums) / 2))
    return gamma * (~gamma & (1 << bits) - 1)

def problem2():
    lines = get_lines(3)
    bits = len(lines[0]) - 1
    o2 = [int(num, 2) for num in lines]
    co2 = [int(num, 2) for num in lines]
    i = bits - 1
    while len(o2) > 1:
        most = int(sum([(num >> i) % 2 for num in o2]) >= (len(o2) / 2))
        o2 = [num for num in o2 if (num >> i) % 2 ^ most]
        i -= 1
    i = bits - 1
    while len(co2) > 1:
        least = int(sum([(num >> i) % 2 for num in co2]) < (len(co2) / 2))
        co2 = [num for num in co2 if (num >> i) % 2 ^ least]
        i -= 1
    return o2[0] * co2[0]