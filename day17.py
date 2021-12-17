from aocutils import get_raw

def problem1():
    vy = abs(int(get_raw(17).split('=')[-1].split('..')[0])) - 1
    return (vy + 1) * vy // 2

def problem2():
    bounds = [[int(n) for n in bound.split('..')] for bound in get_raw(17).split('x=')[1].split(', y=')]
    lands_in_bounds = set_bounds(bounds)
    vy_max = abs(bounds[1][0])
    vx_max = bounds[0][1]
    total = 0
    for x in range(1, vx_max + 1):
        for y in range(-vy_max, vy_max + 1):
            total += lands_in_bounds(x, y)
    return total
    
def set_bounds(bounds):
    [[x1, x2], [y1, y2]] = bounds

    def check_launch(vx, vy):
        x, y = 0, 0
        while x <= x2 and y >= y1:
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True
        return False
    
    return check_launch