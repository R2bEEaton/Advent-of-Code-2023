from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix
from collections import deque

din, aocd_submit = aocd_data_in(split=True, numbers=False)

garden = Matrix([len(din), len(din[0])], 0, wrap=True)
start = []

for i in range(len(din)):
    for j in range(len(din[0])):
        if din[i][j] in "#":
            garden.set([i, j], 1)
        if din[i][j] == "S":
            start = (i, j)

queue = deque([start])
visited = set()
evenodd = [0, 0]
first_few = []
for i in range(1, 26501365):
    for _ in range(len(queue)):
        place = queue.popleft()
        for val, pos in garden.neighbors(place):
            if tuple(pos) in visited:
                continue
            if val == 0:
                visited.add(tuple(pos))
                queue.append(pos)
                evenodd[i % 2] += 1

    if i % 131 == 65:
        first_few.append(evenodd[i % 2])
        if len(first_few) == 3:
            break

# Credit to mgtezak ; https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_21.py
y = first_few
a = (y[2] - (2 * y[1]) + y[0]) // 2
b = y[1] - y[0] - a
c = y[0]
x = (26501365 - 65) // 131

aocd_submit((a * x**2) + (b * x) + c)
