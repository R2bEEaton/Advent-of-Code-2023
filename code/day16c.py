from helpers.datagetter import aocd_data_in
import tqdm
import time

din, aocd_submit = aocd_data_in(split=True, numbers=False)
height = len(din)
width = len(din[0])

for i in range(len(din)):
    din[i] = [c for c in din[i]]


def in_range(i, j):
    if 0 <= i < height and 0 <= j < width:
        return True
    return False


def move(bm):
    out = []
    d = bm[0]
    x, y = bm[1], bm[2]
    c = din[x][y]
    if d == 0:
        if c in ".|":
            out.append((d, x - 1, y))
        if c in "\\-":
            out.append((3, x, y - 1))
        if c in "/-":
            out.append((1, x, y + 1))
    elif d == 1:
        if c in ".-":
            out.append((d, x, y + 1))
        if c in "\\|":
            out.append((2, x + 1, y))
        if c in "/|":
            out.append((0, x - 1, y))
    elif d == 2:
        if c in ".|":
            out.append((d, x + 1, y))
        if c in "\\-":
            out.append((1, x, y + 1))
        if c in "/-":
            out.append((3, x, y - 1))
    elif d == 3:
        if c in ".-":
            out.append((d, x, y - 1))
        if c in "\\|":
            out.append((0, x - 1, y))
        if c in "/|":
            out.append((2, x + 1, y))
    return out


def start_at(direction, x, y):
    beams = [(direction, x, y)]
    already = set()
    energy = {}

    while beams:
        b = beams.pop()
        if b in already or not in_range(b[1], b[2]):
            continue
        energy["%s,%s" % (b[1], b[2])] = 1
        already.add(b)
        bb = move(b)
        for beam in bb:
            beams.append(beam)

    return len(energy)

m = []
for i in tqdm.tqdm(range(len(din))):
    m.append(start_at(1, i, 0))
    m.append(start_at(3, i, len(din[0]) - 1))

for j in tqdm.tqdm(range(len(din[0]))):
    m.append(start_at(2, 0, j))
    m.append(start_at(0, len(din) - 1, j))

aocd_submit(max(m))
