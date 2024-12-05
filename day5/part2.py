from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

# bans[a] -> ids that cannot go before a
bans = defaultdict(list)
i = 0
while lines[i] != '\n':
    a, b = lines[i].strip().split('|')
    bans[a].append(b)

    i += 1

ans = 0
i += 1
while i < len(lines):
    seen = {}
    line = lines[i].strip().split(',')
    any_add = False

    add = True
    while add:
        add = False

        for index in range(len(line)):
            id = line[index]
            for index2 in range(index):
                if line[index2] in bans[id]:
                    add = True
                    any_add = True
                    line[index], line[index2] = line[index2], line[index]
    
    if any_add:
        print('ok', line)
        ans += int(line[len(line) // 2])

    i += 1

print(ans)