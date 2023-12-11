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

mult = 1000000
shift_down = 0
galaxies = []
for i in range(len(din)):
    shift_right = 0
    if i in expand_rows:
        shift_down += mult - 1
    else:
        for j in range(len(din[0])):
            if j in expand_cols:
                shift_right += mult - 1
            else:
                if din[i][j] == "#":
                    galaxies.append([i + shift_down, j + shift_right])

coms = list(combinations(galaxies, 2))
for pair in coms:
    ans += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

aocd_submit(ans)
