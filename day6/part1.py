with open("input.txt") as f:
    grid = list(map(lambda l: l.strip(), f.readlines()))
    n, m = len(grid), len(grid[0])

start = None
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == '^':
            start = i, j
            break

dx, dy = -1, 0
def rot90cw(dir):
    dx, dy = dir
    return (dy, -dx)

def inbound(pos):
    x, y = pos
    return 0 <= x < n and 0 <= y < m

x, y = start
visited= [[0] * m for _ in range(n)]
while inbound((x, y)):
    visited[x][y] = 1
    nx, ny = x + dx, y + dy
    while inbound((nx, ny)) and grid[nx][ny] == '#':
        dx, dy = rot90cw((dx, dy))
        nx, ny = x + dx, y + dy
    x += dx
    y += dy

total = sum(
    map(sum, visited)
)
print(total)