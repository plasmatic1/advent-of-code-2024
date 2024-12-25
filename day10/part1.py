from collections import deque

with open("input.txt") as f:
    grid = list(map(lambda line: list(map(int, line.strip())), f.readlines()))
    n = len(grid)
    m = len(grid[0])

def get_adj(i, j):
    return [
        (ii, jj) for ii, jj
            in [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1)
            ] 
            if 0 <= ii < n and 0 <= jj < m
    ]

total = 0

for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == 0:
            # BFS
            q = deque()
            vis = set()
            
            q.append((i, j))

            while q:
                r, c = q.popleft()
                for rr, cc in get_adj(r, c):
                    if grid[r][c] + 1 == grid[rr][cc]:
                        if (rr, cc) not in vis:
                            vis.add((rr, cc))
                            q.append((rr, cc))
                            if grid[rr][cc] == 9:
                                total += 1

print(total)