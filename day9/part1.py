import heapq

with open("input.txt") as f:
    sizes = list(map(int, f.read().strip()))

layout = [-1] * sum(sizes)
blocks = []
free = []

cur = 0
ctype = 0
fileno = 0
for blen in sizes:
    l, r = cur, cur + blen
    if ctype == 0:
        for i in range(l, r):
            blocks.append((i, fileno))
        fileno += 1
    else:
        for i in range(l, r):
            heapq.heappush(free, i)

    cur += blen
    ctype ^= 1

total_bsize = len(blocks)
while free[0] < blocks[-1][0]:
    posn = heapq.heappop(free)
    origpos, fileno = blocks.pop()
    layout[posn] = fileno
    print(posn, origpos, fileno)
    heapq.heappush(free, origpos)

for posn, fileno in blocks:
    layout[posn] = fileno

print(layout)

checksum = sum(
    i * fileno for i, fileno in enumerate(layout) if fileno != -1
)
print(checksum)