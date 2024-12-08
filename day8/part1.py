from collections import defaultdict

with open("input.txt") as f:
    grid = list(
        map(lambda l: l.strip(), f.readlines())
    )

n = len(grid)
m = len(grid[0])
byfreq = defaultdict(list)

for i, row in enumerate(grid):
    for j, freq in enumerate(row):
        if freq != '.':
            byfreq[freq].append((i, j))

antinode = [[0]*m for _ in range(n)]
def mark(i, j):
    if 0 <= i < n and 0 <= j < m:
        antinode[i][j] = 1

# For points A, B
# Antinode from A->B -- A + 2(B-A) = 2B-A
# Antinode from B->A -- B + 2(A-B) = 2A-B
for _, posns in byfreq.items():
    for p in posns:
        for q in posns:
            if p != q:
                px, py = p
                qx, qy = q

                mark(2*qx - px, 2*qy - py)
                mark(2*px - qx, 2*py - qy)

ans = sum(
    map(
        lambda row: sum(row),
        antinode
    )
)
print(ans)