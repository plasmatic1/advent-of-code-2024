from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    lines[i] = line.strip()

def get_cell(i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
        return lines[i][j]
    else:
        return '.'
    
TARGET = 'XMAS'

dirs = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
dirs.remove((0, 0))

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        for d in dirs:
            dx, dy = d
            x = i
            y = j
            match = 0
            for step in range(len(TARGET)):
                if get_cell(x, y) == TARGET[step]:
                    match += 1

                x += dx
                y += dy
            
            if match == len(TARGET):
                count += 1

print(count)
