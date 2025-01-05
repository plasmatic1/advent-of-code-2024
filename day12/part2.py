"""
Detecting the number of sides in a shape

. - Empty cells
* - Filled cells
o - Cells that are required to be empty
# - Cells that are required to be filled

Instead of detecting sides, we can detect corners instead (# corners = # sides). 

There are 2 types of corners -- inner and outer corners.

For outer corners, there are 4 possible directions:

....... ....... ....... .......
..o.... ....o.. ....... .......
.o#**.. ..**#o. ..***.. ..***..
..***.. ..***.. ..***.. ..***..
..***.. ..***.. ..**#o. .o#**..
....... ....... ....o.. ..o....
....... ....... ....... .......

Similarly, for inner corners, there are 4 possible directions:

....... ....... ....... .......
.##***. .***##. .*****. .*****.
.#o..*. .*..o#. .*...*. .*...*.
.*...*. .*...*. .*...*. .*...*.
.*...*. .*...*. .*..o#. .#o..*.
.*****. .*****. .***##. .##***.
....... ....... ....... .......

To count the number of sides, we can just count the total number of outer and inner corners. Note that a single square can be multiple corners.
"""

with open("input.txt") as f:
    grid = list(map(lambda s: s.strip(), f.readlines()))
    n = len(grid)
    m = len(grid[0])

# shape - a list of cells that form the shape
# center - center x and y
# constraints - a list of constraints of the form (x, y, is_filled), requiring that cell center_x+x and center_y+y has the state is_filled
def check_constraint(shape, center, constraints):
    x, y= center
    for dx, dy, is_filled in constraints:
        if ((x + dx, y + dy) in shape) != is_filled:
            return False
    return True

CORNER_CONSTRAINTS = [
    # Outer Corners
    (
        (0, 0, True),
        (0, -1, False),
        (-1, 0, False)
    ),
    (
        (0, 0, True),
        (0, 1, False),
        (-1, 0, False)
    ),
    (
        (0, 0, True),
        (0, 1, False),
        (1, 0, False)
    ),
    (
        (0, 0, True),
        (0, -1, False),
        (1, 0, False)
    ),
    # Inner Corners
    (
        (0, 0, True),
        (0, 1, True),
        (1, 0, True),
        (1, 1, False),
    ),
    (
        (0, 0, True),
        (0, -1, True),
        (1, 0, True),
        (1, -1, False),
    ),
    (
        (0, 0, True),
        (0, -1, True),
        (-1, 0, True),
        (-1, -1, False),
    ),
    (
        (0, 0, True),
        (0, 1, True),
        (-1, 0, True),
        (-1, 1, False),
    ),
]

def in_bound(p):
    return 0 <= p[0] < n and 0 <= p[1] < m

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
            num_sides = sum(
                map(
                    lambda p: sum(
                        [
                            1 for constraints in CORNER_CONSTRAINTS
                                if check_constraint(posns, p, constraints)
                                
                        ]
                    ),
                    posns
                )
            )

            total += area * num_sides

            print(f"{(i, j)=} {area=} {num_sides=}")

print(total)



