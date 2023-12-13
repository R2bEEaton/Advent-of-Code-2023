from helpers.datagetter import aocd_data_in
import functools

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0


@functools.lru_cache()
def recurse(s, instructions, group_size, done):
    if len(s) == 0:
        if instructions:
            if len(instructions) == 1 and group_size == instructions[0]:
                return 1
            return 0
        else:
            if group_size == 0:
                return 1
            return 0

    if len(instructions) == 0:
        if "#" in s or group_size != 0:
            return 0
        return 1

    curr = s[0]
    rest = s[1:]

    if curr == "?":
        return recurse("#" + rest, instructions, group_size, done) + recurse("." + rest, instructions, group_size, done)

    if curr == "#":
        if group_size + 1 > instructions[0]:
            return 0
        elif group_size == instructions[0]:
            return recurse(rest, instructions[1:], 0, True)
        return recurse(rest, instructions, group_size + 1, False)

    if curr == ".":
        if done or group_size == 0:
            return recurse(rest, instructions, 0, False)
        else:
            if group_size == instructions[0]:
                return recurse(rest, instructions[1:], 0, False)
            return 0


for line in din:
    contig = ((line.split(" ")[0] + "?") * 5)[:-1]
    instrs = tuple([int(x) for x in ((line.split(" ")[1] + ",") * 5)[:-1].split(",")])

    a = recurse(contig, instrs, 0, False)
    ans += a

aocd_submit(ans)
