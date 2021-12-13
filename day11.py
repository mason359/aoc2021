from aocutils import get_lines

def problem1():
    grid = [[int(i) for i in line] for line in get_lines(11)]
    flashes = 0
    for _ in range(100):
        flashes += do_step(grid)
    return flashes

def problem2():
    grid = [[int(i) for i in line] for line in get_lines(11)]
    step = 0
    while not all(all(i == 0 for i in row) for row in grid):
        do_step(grid)
        step += 1
    return step

def do_step(grid):
    flashes = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            increment(grid, r, c)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] >= 1000:
                flashes += 1
                grid[r][c] = 0
    return flashes

def increment(grid, r, c):
    grid[r][c] += 1
    if grid[r][c] > 9 and grid[r][c] < 1000:
        grid[r][c] = 1000
        for ri, ci in neighbors(grid, r, c):
            increment(grid, ri, ci)

def neighbors(grid, r, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if r + i in range(len(grid)) and c + j in range(len(grid[0])) and not (i == 0 and j == 0):
                yield r + i, c + j