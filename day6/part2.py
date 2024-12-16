from tqdm import tqdm

with open("input.txt") as f:
    grid = list(map(lambda l: list(l.strip()), f.readlines()))
    n, m = len(grid), len(grid[0])

start = None
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == '^':
            start = i, j
            break

# Rotate vector by 90 deg CW
def rot90cw(dir):
    dx, dy = dir
    return (dy, -dx)

# Check if position is in-bound
def inbound(pos):
    x, y = pos
    return 0 <= x < n and 0 <= y < m

def is_cyclic(start):
    # To detect whether starting at (start) is a cycle, we can use pidgeonhole principle- a cycle can be of length at most 4nm
    dx, dy = -1, 0
    x, y = start
    for _ in range(n * m * 4):
        nx, ny = x + dx, y + dy
        while inbound((nx, ny)) and grid[nx][ny] == '#':
            dx, dy = rot90cw((dx, dy))
            nx, ny = x + dx, y + dy
        x += dx
        y += dy

        if not inbound((x, y)):
            return False
    
    return True

print("Processing rows...")
total = 0
for i in tqdm(range(n)):
    for j in range(m):
        if grid[i][j] == '.':
            grid[i][j] = '#'
            if is_cyclic(start):
                # print(i, j)
                total += 1
            grid[i][j] = '.'
print(total)