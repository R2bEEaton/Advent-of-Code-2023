from helpers.datagetter import aocd_data_in
from itertools import combinations

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

expand_rows = []
expand_cols = []

for i in range(len(din)):
    g = 0
    for j in range(len(din[0])):
        if din[i][j] == "#":
            g += 1
    if g == 0:
        expand_rows.append(i)

for j in range(len(din[0])):
    g = 0
    for i in range(len(din)):
        if din[i][j] == "#":
            g += 1
    if g == 0:
        expand_cols.append(j)

for i in range(len(expand_rows)):
    din.insert(expand_rows[i] + i, "".join(["." for _ in range(len(din[0]))]))

for j in range(len(expand_cols)):
    for i in range(len(din)):
        din[i] = din[i][:expand_cols[j] + j] + "." + din[i][expand_cols[j] + j:]

galaxies = []
for i in range(len(din)):
    for j in range(len(din[0])):
        if din[i][j] == "#":
            galaxies.append([i, j])

coms = list(combinations(galaxies, 2))
for pair in coms:
    ans += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

aocd_submit(ans)
