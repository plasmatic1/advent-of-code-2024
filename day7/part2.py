import itertools

with open("input.txt") as f:
	eqns = [
		(int(parts[0]), list(map(int, parts[1].split())))
			for parts in map(lambda line: line.split(":"), f.readlines())
	]

OPS = [
	lambda a, b: a + b,
	lambda a, b: a * b,
	lambda a, b: int(str(a) + str(b))
]

total = 0
for target, nums in eqns:
	found = False
	for comb in itertools.product(OPS, repeat=len(nums) - 1):
		cur = nums[0]
		for num, op in zip(nums[1:], comb):
			cur = op(cur, num)
		
		if cur == target:
			found = True
			break
	
	if found:
		print(f"found {target=}")
		total += target

print(total)