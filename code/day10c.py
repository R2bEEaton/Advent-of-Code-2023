from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

matrix = Matrix([len(din), len(din[0])], " ")
start = []

for i in range(len(din)):
    for j in range(len(din[i])):
        c = din[i][j]
        if c not in "-|F7JLS":
            continue
        if c == "S":
            start = [i, j]
        matrix.set([i, j], c)

connections = {
    "-": ["", "-J7", "", "-LF"],
    "|": ["|F7", "", "|LJ", ""],
    "F": ["", "-J7", "|LJ", ""],
    "J": ["|F7", "", "", "-LF"],
    "7": ["", "", "|LJ", "-LF"],
    "L": ["|F7", "-J7", "", ""]
}

for check in connections.keys():
    match = 0
    for neighbor, pos in matrix.neighbors(start):
        i = pos[0] - start[0]
        j = pos[1] - start[1]
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        if neighbor in connections[check][dirs.index([i, j])]:
            match += 1
    if match == 2:
        matrix.set(start, check)
        break

visit = [start]
visited = []
while visit:
    check = visit.pop(0)
    current = matrix.get(check)
    visited.append(check)

    for neighbor, pos in matrix.neighbors(check):
        if pos in visited:
            continue
        i = pos[0] - check[0]
        j = pos[1] - check[1]
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        if neighbor in connections[current][dirs.index([i, j])]:
            visit.append(pos)


for i in range(len(din)):
    last = ""
    count = 0
    for j in range(len(din[i])):
        if [i, j] not in visited:
            if count % 2 == 1:
                ans += 1
        else:
            pipe = matrix.get([i, j])
            if pipe in ["|", "L", "J"]:
                count += 1
            if pipe != "-":
                last = pipe

aocd_submit(ans)
