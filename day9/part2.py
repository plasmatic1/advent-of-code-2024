with open("input.txt") as f:
    sizes = list(map(int, f.read().strip()))

layout = [-1] * sum(sizes)
blocks = []

cur = 0
ctype = 0
fileno = 0
for blen in sizes:
    l, r = cur, cur + blen
    if ctype == 0:
        blocks.append((l, r, fileno))
        fileno += 1

    cur += blen
    ctype ^= 1

# sort in rev file id order
for file in sorted(blocks, key=lambda block: -block[2]):
    moved = False
    moveblock = None
    newpos = None
    newinsertindex = None

    filel, filer, fileno = file
    for i in range(len(blocks) - 1):
        freel, freer = blocks[i][1], blocks[i + 1][0]

        if freel >= filel:
            break

        if freer - freel >= filer - filel:
            moved = True
            moveblock = file
            newpos = freel
            newinsertindex = i + 1
            break
    
    if moved:
        filel, filer, fileno = moveblock
        blocks.remove(moveblock)
        blocks.insert(newinsertindex, (newpos, newpos + filer - filel, fileno))

        print(f"{moveblock=} {newpos=} {newinsertindex=}")

print(blocks)

for l, r, fileno in blocks:
    for i in range(l, r):
        layout[i] = fileno

print(layout)

checksum = sum(
    i * fileno for i, fileno in enumerate(layout) if fileno != -1
)
print(checksum)