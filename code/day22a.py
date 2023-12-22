from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

world = defaultdict(int)
bricks = []


def get_brick(brick_ends):
    for x in range(brick_ends[0][0], brick_ends[1][0] + 1):
        for y in range(brick_ends[0][1], brick_ends[1][1] + 1):
            for z in range(brick_ends[0][2], brick_ends[1][2] + 1):
                yield (x, y, z)


def move_down(brick):
    return (brick[0], brick[1], brick[2] - 1)


def move_up(brick):
    return (brick[0], brick[1], brick[2] + 1)


def move_down_be(brick_ends):
    return [(brick_ends[0][0], brick_ends[0][1], brick_ends[0][2] - 1), (brick_ends[1][0], brick_ends[1][1], brick_ends[1][2] - 1)]


for i in range(len(din)):
    brick = din[i]
    brick_ends = [eval("(%s)" % x) for x in brick.split("~")]
    brick_ends.sort(key=lambda x: [x[2], x[0], x[1]])
    print(brick_ends)
    for b in get_brick(brick_ends):
        world[b] = i + 1
    bricks.append(brick_ends)

stopped = False
while not stopped:
    moved = 0

    for i in range(len(bricks)):
        brick = bricks[i]

        # On ground
        if brick[0][2] == 1:
            continue

        free = True
        for b in get_brick(brick):
            if world[move_down(b)] not in [0, world[b]]:
                free = False
                break
        if free:
            for b in get_brick(brick):
                brick_label = world[b]
                world[b] = 0
                world[move_down(b)] = brick_label
            bricks[i] = move_down_be(brick)
            moved += 1

    if moved == 0:
        stopped = True


supporters = {}
supporteds = {}

bricks.sort()
for brick in bricks:
    supported_by = set()
    supports = set()

    if brick[0][0] == brick[1][0] and brick[0][1] == brick[1][1]:
        # Vertical brick
        curr = world[brick[0]]
        print(chr(64 + curr), "verticlal brick", brick)
        below = world[move_down(brick[0])]
        above = world[move_up(brick[1])]
        if below != 0:
            supported_by.add(chr(64 + below))
        if above != 0:
            supports.add(chr(64 + above))
    else:
        for b in get_brick(brick):
            curr = world[b]
            below = world[move_down(b)]
            above = world[move_up(b)]
            if below != 0:
                supported_by.add(chr(64 + below))
            if above != 0:
                supports.add(chr(64 + above))

    supporters[chr(64 + curr)] = supports
    supporteds[chr(64 + curr)] = supported_by

print(supporters)
print(supporteds)


for brick, supports in supporters.items():
    good = True
    for s in supports:
        if len(supporteds[s]) == 1:
            good = False
    if good:
        ans += 1


aocd_submit(ans)
