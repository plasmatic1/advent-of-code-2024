from collections import Counter

with open("input.txt") as f:
    stones = Counter(map(int, f.read().split()))

def step_stone(stone):
    if stone == 0:
        return [1]
    elif len(s := str(stone)) % 2 == 0:
        halflen = len(s) // 2
        return [int(s[:halflen]), int(s[halflen:])]
    else:
        return [stone * 2024]

# Assume 50% chance x*2024 has even/odd # of digits
# In that case, we should have exponentially fewer values with 
for _ in range(75):
    next_stones = Counter()
    for k, v in stones.items():
        for next_stone in step_stone(k):
            next_stones[next_stone] += v

    stones = next_stones

total = sum(stones.values())

print(total)