with open("input.txt") as f:
    reports = []
    for line in f:
        report = list(map(int, line.split()))
        reports.append(report)

num_ok = 0
for report in reports:
    # check order
    if report == list(sorted(report)) or report == list(sorted(report, reverse=True)):
        # check diff
        diffs_ok = True
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i+1])
            if diff < 1 or diff > 3:
                diffs_ok = False
                break
        
        if diffs_ok:
            num_ok += 1

print(num_ok)
