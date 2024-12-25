import functools

with open("input.txt") as f:
    stones = list(map(int, f.read().split()))

@functools.lru_cache
def num_stones(stone, iters):
    if iters == 0:
        return 1
    elif stone == 0:
        return num_stones(1, iters - 1)
    elif len(s := str(stone)) % 2 == 0:
        halflen = len(s) // 2
        return num_stones(int(s[:halflen]), iters - 1) + num_stones(int(s[halflen:]), iters - 1)
    else:
        return num_stones(stone * 2024, iters - 1)

total = sum([
    num_stones(stone, 25) for stone in stones
])

print(total)