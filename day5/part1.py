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
    seen = set()
    line = lines[i].strip().split(',')
    ok = True
    for id in line:
        for banid in bans[id]:
            if banid in seen:
                ok = False
                break

        seen.add(id)
    
    if ok:
        print('ok', line)
        ans += int(line[len(line) // 2])

    i += 1

print(ans)