from helpers.datagetter import aocd_data_in
from collections import defaultdict
from PIL import Image

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

ground = defaultdict(str)
at = [0, 0]

x_0, x_1, y_0, y_1 = float('inf'), float('-inf'), float('inf'), float('-inf')

for line in din:
    d, n, color = line.split(" ")

    directions = ["U", "R", "D", "L"]
    d = directions.index(d)

    for _ in range(int(n)):
        if d == 0:
            at[0] -= 1
        elif d == 1:
            at[1] += 1
        elif d == 2:
            at[0] += 1
        else:
            at[1] -= 1
        ground[",".join(map(str, at))] = color
        x_0 = min(x_0, at[0])
        x_1 = max(x_1, at[0])
        y_0 = min(y_0, at[1])
        y_1 = max(y_1, at[1])

print(ground)
width = abs(x_0 - x_1) + 1
height = abs(y_0 - y_1) + 1

print(width, height)

im = Image.new(mode="RGB", size=(width, height))
for pixel, color in ground.items():
    x, y = map(int, pixel.split(","))
    print(x, y)
    im.putpixel((x - x_0, y - y_0), color)

im.show()
# im.save("a.png")
# Flood fill in paint.net, then use magic wand to select, and count is visible on bottom left
