from helpers.datagetter import aocd_data_in
import functools
import tqdm

din, aocd_submit = aocd_data_in(split=False, numbers=False)
ans = 0


@functools.lru_cache(maxsize=None)
def cycle(din):
    din = din.split("\n")
    # North
    moved = True
    while moved:
        moved = False
        for i in range(1, len(din)):
            for j in range(len(din[0])):
                if din[i][j] == "O" and din[i-1][j] == ".":
                    din[i] = [c for c in din[i]]
                    din[i][j] = "."
                    din[i-1] = [c for c in din[i-1]]
                    din[i-1][j] = "O"
                    din[i] = "".join(din[i])
                    din[i-1] = "".join(din[i-1])
                    moved = True

    # West
    moved = True
    while moved:
        moved = False
        for i in range(len(din)):
            for j in range(1, len(din[0])):
                if din[i][j] == "O" and din[i][j-1] == ".":
                    din[i] = [c for c in din[i]]
                    din[i][j] = "."
                    din[i][j-1] = "O"
                    din[i] = "".join(din[i])
                    moved = True

    # South
    moved = True
    while moved:
        moved = False
        for i in range(len(din) - 1):
            for j in range(len(din[0])):
                if din[i][j] == "O" and din[i+1][j] == ".":
                    din[i] = [c for c in din[i]]
                    din[i][j] = "."
                    din[i+1] = [c for c in din[i+1]]
                    din[i+1][j] = "O"
                    din[i] = "".join(din[i])
                    din[i+1] = "".join(din[i+1])
                    moved = True

    # East
    moved = True
    while moved:
        moved = False
        for i in range(len(din)):
            for j in range(0, len(din[0]) - 1):
                if din[i][j] == "O" and din[i][j+1] == ".":
                    din[i] = [c for c in din[i]]
                    din[i][j] = "."
                    din[i][j+1] = "O"
                    din[i] = "".join(din[i])
                    moved = True

    return "\n".join(din)


for _ in tqdm.tqdm(range(1000000000)):
    din = cycle(din)

din = din.split("\n")
for i in range(len(din)):
    ans += din[i].count("O") * (len(din) - i)

aocd_submit(ans)
