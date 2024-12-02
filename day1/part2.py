with open("input.txt") as f:
    list1 = []
    list2 = []
    for line in f:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

from collections import Counter

fre2 = Counter(list2)

score = sum(
    x * fre2[x] for x in list1
)

print(score)