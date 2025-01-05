with open("input.txt") as f:
    grid = list(map(lambda s: s.strip(), f.readlines()))
    n = len(grid)
    m = len(grid[0])

def in_bound(p):
    return 0 <= p[0] < n and 0 <= p[1] < m

NO = lambda _: True

def get_adj(p, use_filter=in_bound):
    r, c = p
    return filter(
        use_filter,
        [
            (r + 1, c),
            (r - 1, c),
            (r, c + 1),
            (r, c - 1)
        ]
    )

def posn_eq(p, val):
    return grid[p[0]][p[1]] == val if in_bound(p) else False

vis = set()
total = 0

for i in range(n):
    for j in range(m):
        if (i, j) not in vis:
            target = grid[i][j]
            posns = []

            def dfs(p):
                if p in vis:
                    return
                if grid[p[0]][p[1]] != target:
                    return

                vis.add(p)
                posns.append(p)

                for adj_p in get_adj(p):
                    dfs(adj_p)
            
            dfs((i, j))

            area = len(posns)
            perimeter = sum(
                map(
                    lambda p: sum(
                        [
                            1 for adj_p in get_adj(p, use_filter=NO)
                                if not posn_eq(adj_p, grid[p[0]][p[1]])
                                
                        ]
                    ),
                    posns
                )
            )

            total += area * perimeter

print(total)



