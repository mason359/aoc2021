from aocutils import get_lines

def problem1():
    x, y = 0, 0
    for dir in get_lines(2):
        match dir.split():
            case ['forward', val]:
                x += int(val)
            case ['down', val]:
                y += int(val)
            case ['up', val]:
                y -= int(val)
    return x * y

def problem2():
    x, y, aim = 0, 0, 0
    for dir in get_lines(2):
        match dir.split():
            case ['forward', val]:
                x += int(val)
                y += int(val) * aim
            case ['down', val]:
                aim += int(val)
            case ['up', val]:
                aim -= int(val)
    return x * y