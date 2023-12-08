from helpers.datagetter import aocd_data_in
from collections import defaultdict
import math

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

maps = defaultdict(list)

instr = din[0]

for line in din[2:]:
    maps[line.split(" ")[0]] = [line.split("(")[1].split(",")[0], line.split(", ")[1].split(")")[0]]

at = [x for x in maps.keys() if x.endswith("A")]
i = 0
finished_by = [0 for _ in range(len(maps.keys()))]
while any([not x.endswith("Z") for x in at]):
    for j in range(len(at)):
        if finished_by[j] != 0:
            continue
        at[j] = maps[at[j]][0] if instr[i % len(instr)] == "L" else maps[at[j]][1]
        if at[j].endswith("Z"):
            finished_by[j] = i + 1
    i += 1

ans = math.lcm(*[x for x in finished_by if x != 0])

aocd_submit(ans)
