from helpers.datagetter import aocd_data_in, submit
from collections import defaultdict

din = aocd_data_in(split=True, numbers=False)
ans = 0

gears = defaultdict(list)

for i in range(len(din)):
    num = ""
    din[i] += "."
    for j in range(len(din[i])):
        char = din[i][j]
        if char.isdigit():
            num += char
        else:
            if len(num):
                geared_already = []
                breakout = False
                for offset in range(1, len(num) + 1):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if breakout:
                                break
                            try:
                                c = din[i+k][j-offset+l]
                                if c == "*" and [i+k, j-offset+l] not in geared_already:
                                    gears["%s %s" % (i+k, j-offset+l)].append(int(num))
                                    geared_already.append([i+k, j-offset+l])
                            except:
                                None
            num = ""

for items in gears.values():
    if len(items) == 2:
        ans += items[0] * items[1]

submit(ans)
