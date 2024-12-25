from collections import defaultdict, Counter, deque

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

# build graph
g = defaultdict(list)
for i in range(n):
    for j in range(m):
        for ii, jj in get_adj(i, j):
            if grid[i][j] + 1 == grid[ii][jj]:
                g[(i, j)].append((ii, jj))

# indegree counter
indeg = {(i, j): 0 for i in range(n) for j in range(m)} # we need all of the keys
for tos in g.values():
    for to in tos:
        indeg[to] += 1

# topological sort
path_count = Counter() # maintain path count DP while doing toposort
q = deque()

for k, v in indeg.items():
    if v == 0:
        path_count[k] = 1 if grid[k[0]][k[1]] == 0 else 0
        q.append(k)

trail_count = 0

while q:
    c = q.popleft()
    print(f"{c=} {path_count[c]=}")

    if grid[c[0]][c[1]] == 9:
        trail_count += path_count[c]

    for to in g[c]:
        path_count[to] += path_count[c]
        indeg[to] -= 1
        if indeg[to] == 0:
            q.append(to)

print(trail_count)