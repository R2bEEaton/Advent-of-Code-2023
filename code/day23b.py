from helpers.datagetter import aocd_data_in
from helpers.matrix import Matrix
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

world = Matrix([len(din), len(din[0])], 0)
start = []
end = []

# Load into matrix, gosh I need to make a helper for this
for i in range(len(din)):
    for j in range(len(din[i])):
        if i == 0 and din[i][j] == ".":
            start = [i, j]
        if i == len(din) - 1 and din[i][j] == ".":
            end = [i, j]
        world.set([i, j], "." if din[i][j] in ".<>^v" else "#")

# Find all intersections
intersections = []
for i in range(len(din)):
    for j in range(len(din[i])):
        if din[i][j] == ".":
            if len([x[0] for x in world.neighbors([i, j]) if x[0] == "."]) != 2:
                intersections.append([i, j])

edges = defaultdict(dict)

# Get distance between each intersection and its adjacent intersections
for inter in intersections:
    queue = [(0, inter)]
    visited = set()
    while queue:
        dist, curr = queue.pop(0)

        if tuple(curr) in visited:
            continue
        visited.add(tuple(curr))

        if curr in intersections and curr != inter:
            edges[tuple(inter)][tuple(curr)] = dist
            continue

        for val, n in world.neighbors(curr):
            if val == ".":
                queue.append((dist + 1, n))

# Run Part 1 code on this compressed graph
longest_path = 0
queue = [(tuple(start), set(), 0)]
while queue:
    curr = queue.pop(-1)  # Use DFS instead to limit memory growth bottleneck
    pos, visited, dist = curr

    # If we reached the end, update the candidate for the longest path
    if pos == tuple(end):
        longest_path = max(longest_path, dist)
        continue

    # Check each outgoing node that hasn't been explored yet
    for neighbor in edges[pos].keys():
        if neighbor in visited:
            continue
        queue.append([neighbor, visited | {neighbor}, dist + edges[pos][neighbor]])

aocd_submit(longest_path)
