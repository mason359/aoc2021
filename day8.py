from aocutils import get_lines

UNIQUE_LEN = {2: '1', 3: '7', 4: '4', 7: '8'}

def problem1():
    return sum(sum(len(digit) in [2, 3, 4, 7] for digit in line.split(' | ')[1].split()) for line in get_lines(8))

def problem2():
    lines = [[digits.split() for digits in line.split(' | ')] for line in get_lines(8)]
    total = 0
    for digits, out in lines:
        one, four = sorted([digit for digit in digits if len(digit) in [2, 4]], key=lambda x: len(x))
        total += int(''.join([get_digit(digit, one, four) for digit in out]))
    return total

def get_digit(digit, one, four):
        if len(digit) in [2, 3, 4, 7]:
            return UNIQUE_LEN[len(digit)]
        elif len(digit) == 5:
            if all(c in digit for c in one):
                return '3'
            elif sum(c in digit for c in four) == 3:
                return '5'
            else:
                return '2'
        elif len(digit) == 6:
            if all(c in digit for c in four):
                return '9'
            elif all(c in digit for c in one):
                return '0'
            else:
                return '6'
