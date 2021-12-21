from aocutils import get_raw

def problem1():
    return simulate(2)    

def problem2():
    return simulate(50)

def simulate(steps):
    image = Image()
    for i in range(steps):
        image.step(i)
    return len(image.image)

class Image:

    def __init__(self):
        key, image = get_raw(20).split('\n\n')
        image = image.strip().split('\n')
        self.minr, self.maxr = -1, len(image) + 1
        self.minc, self.maxc = -1, len(image[0]) + 1
        self.key = key
        self.image = set()
        for r, row in enumerate(image):
            for c, pixel in enumerate(row):
                if pixel == '#':
                    self.image.add((r, c))

    def step(self, step):
        new_image = set()
        for r in range(self.minr, self.maxr):
            for c in range(self.minc, self.maxc):
                index = '0' + ''.join(b for b in self.get_neighbors(r, c, step))
                if self.key[int(index, 2)] == '#':
                    new_image.add((r, c))
        self.image = new_image
        self.minr -= 1
        self.maxr += 1
        self.minc -= 1
        self.maxc += 1

    def get_neighbors(self, row, col, step):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if self.minr < r < self.maxr - 1 and self.minc < c < self.maxc - 1:
                    yield ('0', '1')[(r, c) in self.image]
                else:
                    yield ('0', '1')[(((r, c) in self.image) + step) % 2]