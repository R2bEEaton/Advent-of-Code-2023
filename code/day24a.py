from helpers.datagetter import aocd_data_in
import itertools

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0

for pair in itertools.combinations(din, 2):
    L1, L2 = pair
    x1, y1 = L1[0], L1[1]
    x2, y2 = L1[0] + L1[3], L1[1] + L1[4]
    x3, y3 = L2[0], L2[1]
    x4, y4 = L2[0] + L2[3], L2[1] + L2[4]

    try:
        # Compute intersection given two points on two lines
        Px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        Py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        # In range
        if 200000000000000 <= Px <= 400000000000000 and 200000000000000 <= Py <= 400000000000000:
            # In future
            if abs(Px - x2) < abs(Px - x1) and abs(Py - y2) < abs(Py - y1) and abs(Px - x4) < abs(Px - x3) and abs(Py - y4) < abs(Py - y3):
                ans += 1
    except:
        None

aocd_submit(ans)
