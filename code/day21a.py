from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

garden = Matrix([len(din), len(din[0])], 0)
start = ()

for i in range(len(din)):
    for j in range(len(din[0])):
        if din[i][j] in "#S":
            garden.set([i, j], 1)
        if din[i][j] == "S":
            start = (i, j, 0)

visited = set()
positions = set()
queue = [start]

while queue:
    node = queue.pop(0)
    x, y, moved = node
    curr = (x, y)

    if node in visited:
        continue
    if moved >= 64:
        positions.add(curr)
        continue
    visited.add(node)

    for val, pos in garden.neighbors(list(curr)):
        if val == 0:
            queue.append(tuple([pos[0], pos[1], moved + 1]))

aocd_submit(len(positions) + 1)
