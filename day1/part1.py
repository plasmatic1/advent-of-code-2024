with open("input.txt") as f:
    list1 = []
    list2 = []
    for line in f:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

list1.sort()
list2.sort()

ans = sum((abs(a - b) for a, b in zip(list1, list2)))
print(ans)