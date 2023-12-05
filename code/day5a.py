from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

maps = {}
m = ""

seeds = [int(i) for i in din[0].split(": ")[1].split(" ")]

for line in din[2:]:
    if ":" in line:
        m = line.split("-")[0]
        maps[m] = []
    elif line == "":
        continue
    else:
        maps[m].append([int(i) for i in line.split(" ")])


locations = []
for seed in [i for i in range(79, 79+14)]:
    for k in maps.keys():
        for m in maps[k]:
            if m[1] <= seed < m[1] + m[2]:
                seed = m[0] + (seed - m[1])
                break
    locations.append(seed)

aocd_submit(min(locations))
