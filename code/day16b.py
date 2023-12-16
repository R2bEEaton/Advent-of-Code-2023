import functools
from helpers.datagetter import aocd_data_in
import tqdm
import time

din, aocd_submit = aocd_data_in(split=True, numbers=False)

for i in range(len(din)):
    din[i] = [c for c in din[i]]


def in_range(i, j):
    if i in range(len(din)) and j in range(len(din[0])):
        return True
    return False


@functools.cache
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
    already = []

    while len(beams):
        new_beams = []
        for b in beams:
            if b in already or not in_range(b[1], b[2]):
                continue
            already.append(b)
            bb = move(b)
            for beam in bb:
                new_beams.append(beam)
        beams = new_beams.copy()

    dict = {}
    for bm in already:
        dict["%s, %s" % (bm[1], bm[2])] = 1

    return len(dict)

m = []
for i in tqdm.tqdm(range(len(din))):
    m.append(start_at(1, i, 0))
    m.append(start_at(3, i, len(din[0]) - 1))

for j in tqdm.tqdm(range(len(din[0]))):
    m.append(start_at(2, 0, j))
    m.append(start_at(0, len(din) - 1, j))

aocd_submit(max(m))