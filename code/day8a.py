from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

maps = defaultdict(list)

instr = din[0]

for line in din[2:]:
    maps[line.split(" ")[0]] = [line.split("(")[1].split(",")[0], line.split(", ")[1].split(")")[0]]

at = "AAA"
i = 0
while at != "ZZZ":
    at = maps[at][0] if instr[i % len(instr)] == "L" else maps[at][1]
    i += 1

aocd_submit(i)
