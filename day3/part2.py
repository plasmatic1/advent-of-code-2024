import re

with open('input.txt') as f:
	s = f.read()

m = re.findall(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", s)

ans=0
enable = True
for mm in m:
	print(mm)
	if len(mm[0]) == 0:
		if mm[-1] == "don't()":
			enable = False
		else:
			enable = True
	else:
		if enable:
			a = int(mm[1])
			b = int(mm[2])
			ans += int(a)*int(b)

print(ans)
