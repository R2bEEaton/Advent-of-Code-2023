from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=False, numbers=False)
ans = 0

boxes = defaultdict(list)

for code in din.split(","):
    focal = 0
    if "-" in code:
        hsh = code.split("-")[0]
        operation = "-"
    else:
        hsh = code.split("=")[0]
        operation = "="
        focal = int(code.split("=")[1])

    current_value = 0
    for c in hsh:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    if operation == "-":
        for i in range(len(boxes[current_value])):
            if boxes[current_value][i][0] == hsh:
                boxes[current_value].pop(i)
                break
    else:
        for i in range(len(boxes[current_value])):
            if boxes[current_value][i][0] == hsh:
                boxes[current_value].pop(i)
                boxes[current_value].insert(i, [hsh, focal])
                break
        else:
            boxes[current_value].append([hsh, focal])

for box_num, lenses in boxes.items():
    if not lenses:
        continue
    for i in range(len(lenses)):
        ans += (box_num + 1) * (i + 1) * (lenses[i][1])

aocd_submit(ans)
