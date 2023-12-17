from helpers.datagetter import aocd_data_in
import heapq

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

for i in range(len(din)):
    din[i] = [c for c in din[i]]

visited = set()

q = [(0, (0, 0), None, (None, None, None, None, None, None, None, None, None))]
while q:
    node = heapq.heappop(q)
    heat, current, direction, prev = node
    x, y = current

    if x == len(din) - 1 and y == len(din[0]) - 1 and [*prev[-3:], direction].count(direction) == 4:
        ans = heat
        break

    if (current, direction, prev) in visited:
        continue
    visited.add((current, direction, prev))

    for i in range(-1, 2):
        for j in range(-1, 2):
            if abs(i) + abs(j) != 1 or (x + i) < 0 or (x + i) >= len(din) or (y + j) < 0 or (y + j) >= len(din[0]):
                continue
            d = [(-1, 0), (0, 1), (1, 0), (0, -1)].index((i, j))

            if direction is not None:
                if abs(direction - d) == 2 and direction != -1:
                    continue
                if None not in prev and prev.count(prev[0]) == len(prev) and prev[0] == direction == d:
                    continue
                if [*prev[-3:], direction].count(direction) != 4 and direction != d:
                    continue

            alt = heat + int(din[x + i][y + j])
            new_node = (alt, (x + i, y + j), d, (*prev[1:], direction))
            heapq.heappush(q, new_node)

print(ans)
aocd_submit(ans)
