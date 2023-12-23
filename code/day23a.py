from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

world = Matrix([len(din), len(din[0])], 0)
start = []
end = []

for i in range(len(din)):
    for j in range(len(din[i])):
        if i == 0 and din[i][j] == ".":
            visited = set()
            visited.add(tuple([i, j]))
            start = [i, j, visited]
        if i == len(din) - 1 and din[i][j] == ".":
            end = [i, j]
        world.set([i, j], din[i][j])

longpaths = []

queue = [start]
while queue:
    curr = queue.pop(0)
    pos = [curr[0], curr[1]]

    visited = curr[2]

    if pos == end:
        longpaths.append(len(visited) - 1)
        continue

    for val, neighbor in world.neighbors(pos):
        if tuple(neighbor) in visited:
            continue

        vcopy = visited.copy()
        if val in ".>^v<":
            vcopy.add(tuple(neighbor))

        if val == ".":
            queue.append([neighbor[0], neighbor[1], vcopy])
        if val == ">" and tuple([neighbor[0], neighbor[1] + 1]) not in vcopy:
            vcopy.add(tuple([neighbor[0], neighbor[1] + 1]))
            queue.append([neighbor[0], neighbor[1] + 1, vcopy])
        if val == "<" and tuple([neighbor[0], neighbor[1] - 1]) not in vcopy:
            vcopy.add(tuple([neighbor[0], neighbor[1] - 1]))
            queue.append([neighbor[0], neighbor[1] - 1, vcopy])
        if val == "v" and tuple([neighbor[0] + 1, neighbor[1]]) not in vcopy:
            vcopy.add(tuple([neighbor[0] + 1, neighbor[1]]))
            queue.append([neighbor[0] + 1, neighbor[1], vcopy])
        if val == "^" and tuple([neighbor[0] - 1, neighbor[1]]) not in vcopy:
            vcopy.add(tuple([neighbor[0] - 1, neighbor[1]]))
            queue.append([neighbor[0] - 1, neighbor[1], vcopy])


aocd_submit(max(longpaths))
