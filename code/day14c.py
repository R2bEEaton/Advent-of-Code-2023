from helpers.datagetter import aocd_data_in
import time
import json

din, aocd_submit = aocd_data_in(split=True, numbers=False)
now = time.time()
for i in range(len(din)):
    din[i] = [c for c in din[i]]

ans = 0

def cycle(grid):
    # North
    moved = True
    y, x = len(grid), len(grid[0])
    while moved:
        moved = False
        for i in range(1, y):
            for j in range(x):
                if grid[i][j] == "O" and grid[i - 1][j] == ".":
                    grid[i][j] = "."
                    grid[i - 1][j] = "O"
                    moved = True

    # West
    moved = True
    while moved:
        moved = False
        for i in range(y):
            for j in range(1, x):
                if grid[i][j] == "O" and grid[i][j - 1] == ".":
                    grid[i][j] = "."
                    grid[i][j - 1] = "O"
                    moved = True

    # South
    moved = True
    while moved:
        moved = False
        for i in range(y - 1):
            for j in range(x):
                if grid[i][j] == "O" and grid[i + 1][j] == ".":
                    grid[i][j] = "."
                    grid[i + 1][j] = "O"
                    moved = True

    # East
    moved = True
    while moved:
        moved = False
        for i in range(y):
            for j in range(0, x - 1):
                if grid[i][j] == "O" and grid[i][j + 1] == ".":
                    grid[i][j] = "."
                    grid[i][j + 1] = "O"
                    moved = True

    return grid


found = [json.dumps(din)]
cycle_len, cycle_start = 0, 0

while True:
    din = cycle(din)
    dump = json.dumps(din)
    if dump in found:
        at = found.index(dump)
        cycle_start = len(found)
        cycle_len = len(found) - at
        break
    found.append(dump)

print(cycle_start, cycle_len)

din = json.loads(found[cycle_start - cycle_len + (1000000000 - cycle_start) % cycle_len])
for i in range(len(din)):
    ans += din[i].count("O") * (len(din) - i)

print(time.time() - now)

aocd_submit(ans)