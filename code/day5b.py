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
        d = [int(i) for i in line.split(" ")]
        maps[m].append({"ds": d[0], "de": d[0] + d[2] - 1, "ss": d[1], "se": d[1] + d[2] - 1})


def get_ranges(key, ranges):
    # print(key, ranges)
    maps[key].sort(key=lambda x: x["ss"])

    out_ranges = []
    for sd in maps[key]:
        new_rgs = []
        for arange in ranges:
            if arange[0] < sd["ss"] and arange[1] >= sd["ss"] and arange[1] <= sd["se"]:
                new_rgs.append([arange[0], sd["ss"] - 1])
                out_ranges.append([sd["ds"], arange[1] - sd["ss"] + sd["ds"]])
            elif arange[0] >= sd["ss"] and arange[1] <= sd["se"]:
                out_ranges.append([arange[0] - sd["ss"] + sd["ds"], arange[1] - sd["ss"] + sd["ds"]])
            elif arange[0] >= sd["ss"] and arange[0] <= sd["se"] and arange[1] > sd["se"]:
                out_ranges.append([arange[0] - sd["ss"] + sd["ds"], sd["de"]])
                new_rgs.append([sd["se"] + 1, arange[1]])
            elif arange[0] < sd["ss"] and arange[1] > sd["se"]:
                new_rgs.append([arange[0], sd["ss"] - 1])
                out_ranges.append([sd["ds"], sd["de"]])
                new_rgs.append([sd["se"] + 1, arange[1]])
            else:
                new_rgs.append(arange)
        ranges = new_rgs.copy()

    out_ranges += ranges
    return out_ranges


locations = []
for i in range(0, len(seeds), 2):
    rgs = get_ranges("seed", [[seeds[i], seeds[i] + seeds[i + 1] - 1]])
    rgs = get_ranges("soil", rgs)
    rgs = get_ranges("fertilizer", rgs)
    rgs = get_ranges("water", rgs)
    rgs = get_ranges("light", rgs)
    rgs = get_ranges("temperature", rgs)
    rgs = get_ranges("humidity", rgs)
    for rg in rgs:
        locations.append(rg[0])

aocd_submit(min(locations))
