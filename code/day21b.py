from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

garden = Matrix([len(din), len(din[0])], 0, wrap=True)
start = []

for i in range(len(din)):
    for j in range(len(din[0])):
        if din[i][j] in "#S":
            garden.set([i, j], 1)
        if din[i][j] == "S":
            start = (i, j, 0)

def examine(steps):
    visited = set()
    positions = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        x, y, moved = node
        curr = (x, y)

        if node in visited:
            continue
        if moved >= steps:
            positions.add(curr)
            continue
        visited.add(node)

        for val, pos in garden.neighbors(list(curr)):
            if val == 0:
                new_node = tuple([pos[0], pos[1], moved + 1])
                queue.append(new_node)

    return len(positions)

print(examine(0))
print(examine(6))
print(examine(10))
print(examine(50))

exit()
aocd_submit(ans)
