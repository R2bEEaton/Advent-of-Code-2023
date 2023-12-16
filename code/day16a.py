from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

for i in range(len(din)):
    din[i] = [c for c in din[i]]


def in_range(i, j):
    if 0 <= i < len(din) and 0 <= j < len(din[0]):
        return True
    return False


def move(bms):
    out = []
    for bm in bms:
        d = bm["dir"]
        x, y = bm["pos"]
        c = din[x][y]
        if d == 0:
            if c in ".|":
                out.append({"dir": d, "pos": (x - 1, y)})
            if c in "\\-":
                out.append({"dir": 3, "pos": (x, y - 1)})
            if c in "/-":
                out.append({"dir": 1, "pos": (x, y + 1)})
        elif d == 1:
            if c in ".-":
                out.append({"dir": d, "pos": (x, y + 1)})
            if c in "\\|":
                out.append({"dir": 2, "pos": (x + 1, y)})
            if c in "/|":
                out.append({"dir": 0, "pos": (x - 1, y)})
        elif d == 2:
            if c in ".|":
                out.append({"dir": d, "pos": (x + 1, y)})
            if c in "\\-":
                out.append({"dir": 1, "pos": (x, y + 1)})
            if c in "/-":
                out.append({"dir": 3, "pos": (x, y - 1)})
        elif d == 3:
            print("test", c, )
            if c in ".-":
                out.append({"dir": d, "pos": (x, y - 1)})
            if c in "\\|":
                print(d, x, y)
                out.append({"dir": 0, "pos": (x - 1, y)})
            if c in "/|":
                out.append({"dir": 2, "pos": (x + 1, y)})
    return out


beams = [{"dir": 1, "pos": (0, 0)}]
already = [{"dir": 1, "pos": (0, 0)}]

print(beams)

while len(beams):
    new_beams = []
    for beam in move(beams):
        if beam not in already and in_range(beam["pos"][0], beam["pos"][1]):
            new_beams.append(beam)
            already.append(beam)
    beams = new_beams.copy()
    print(beams)

uniq = []
for bm in already:
    if bm["pos"] not in uniq:
        uniq.append(bm["pos"])

aocd_submit(len(uniq))
