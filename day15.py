from aocutils import get_lines

def problem1():
    grid = [[int(i) for i in row] for row in get_lines(15)]
    return find_shortest_path(grid)

def problem2():
    grid = get_large_grid()
    return find_shortest_path(grid)

def find_shortest_path(grid):
    visited = {(0, 0)}
    current = [[] for _ in range(10)]
    current[0].append((0, 0))
    step = 0
    while True:
        for r, c in current[step % 10]:
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return step
            for ri, ci in get_neighbors(grid, r, c):
                if (ri, ci) not in visited:
                    visited.add((ri, ci))
                    current[(step + grid[ri][ci]) % 10].append((ri, ci))
        current[step % 10] = []
        step += 1

def get_neighbors(grid, r, c):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]):
            yield r + i, c + j

def get_large_grid():
    original = [[int(i) for i in row] for row in get_lines(15)]
    grid = []
    for r in range(5):
        new_row = [[] for _ in range(len(original))]
        for c in range(5):
            new_row = [row + [((i + r + c - 1) % 9) + 1 for i in original[n]] for n, row in enumerate(new_row)]
        grid += new_row
    return grid    