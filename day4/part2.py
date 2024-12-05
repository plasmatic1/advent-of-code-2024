from collections import Counter
import itertools

with open("input.txt") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    lines[i] = line.strip()

def get_cell(i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
        return lines[i][j]
    else:
        return '.'
    
TARGET = 'MAS'

dirs = [(i, j) for i in [-1, 1] for j in [-1, 1]]

mid_cnts = Counter() # mid_cnts[i] = number of diagonal MAS' with midpoint at i
for i in range(len(lines)):
    for j in range(len(lines[i])):
        for d in dirs:
            dx, dy = d
            x = i
            y = j
            posns = []
            match = 0
            for step in range(len(TARGET)):
                posns.append((x, y))

                if get_cell(x, y) == TARGET[step]:
                    match += 1

                x += dx
                y += dy
            
            if match == len(TARGET):
                mid_cnts[posns[len(TARGET) // 2]] += 1

ans = sum(
    1 for _ in
        filter(
            lambda t: t[1] == 2,
            mid_cnts.items()
        )
)
print(ans)
