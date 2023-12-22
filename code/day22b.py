from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

world = defaultdict(int)
bricks = []


# Get all segments of a brick
def get_brick(brick_ends):
    for x in range(brick_ends[0][0], brick_ends[1][0] + 1):
        for y in range(brick_ends[0][1], brick_ends[1][1] + 1):
            for z in range(brick_ends[0][2], brick_ends[1][2] + 1):
                yield (x, y, z)


# Move a brick segment down
def move_down(brick):
    return (brick[0], brick[1], brick[2] - 1)


# Move a brick segment up
def move_up(brick):
    return (brick[0], brick[1], brick[2] + 1)


# Move an entire brick down
def move_down_be(brick_ends):
    return [(brick_ends[0][0], brick_ends[0][1], brick_ends[0][2] - 1), (brick_ends[1][0], brick_ends[1][1], brick_ends[1][2] - 1)]


# Simulate bricks falling until nothing can fall anymore - falls down by one each time, not efficient
def simulate_fall(world, bricks, to_remove):
    moved_bricks = set()
    while True:
        moved = 0

        for i in range(len(bricks)):
            brick = bricks[i]

            # On ground
            if brick[0][2] == 1:
                continue

            free = True
            for b in get_brick(brick):
                # If any segment of the brick is not above air, or itself, or the removed brick, it cannot fall
                if world[move_down(b)] not in [0, world[b], to_remove]:
                    free = False
                    break
            if free:
                # If the brick can fall, update the world accordingly
                brick_label = world[brick[0]]
                for b in get_brick(brick):
                    world[b] = 0
                    world[move_down(b)] = brick_label
                bricks[i] = move_down_be(brick)
                moved += 1
                moved_bricks.add(i)

        # If we didn't move anything, we can stop
        if moved == 0:
            break

    # Return the updated world, updated bricks, and number of moved bricks
    return world, bricks, len(moved_bricks)


# Parse input, create world
for i in range(len(din)):
    brick = din[i]
    brick_ends = [eval("(%s)" % x) for x in brick.split("~")]
    brick_ends.sort(key=lambda x: [x[2], x[0], x[1]])
    for b in get_brick(brick_ends):
        world[b] = i + 1
    bricks.append(brick_ends)

# Fall the world
world, bricks, _ = simulate_fall(world, bricks, None)

# For each brick, simulate the world falling with that brick removed
for brick in range(1, len(din) + 1):
    ans += simulate_fall(world.copy(), bricks.copy(), brick)[2]

aocd_submit(ans)
