import re

with open('input.txt') as f:
	s = f.read()

m = re.findall(r"mul\((\d+),(\d+)\)", s)

ans=0
for mm in m:
	print(mm)
	a, b = mm
	ans += int(a)*int(b)

print(ans)
