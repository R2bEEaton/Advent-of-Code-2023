from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

workflows = {}

for line in din:
    if line == "":
        break

    name = line.split("{")[0]
    raw_rules = line.split("{")[1][:-1].split(",")

    rules = []
    for r in raw_rules:
        if ":" in r:
            rules.append((r.split(":")[0], r.split(":")[1]))
        else:
            rules.append((1, r))

    workflows[name] = rules


def do_workflow(w, xmas):
    x, m, a, s = xmas

    if w == "R":
        return 0
    elif w == "A":
        return (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)

    track = 0
    for rule in workflows[w]:
        if str(rule[0])[0] == "1":
            track += do_workflow(rule[1], xmas)
            continue
        to_modify = "xmas".index(str(rule[0])[0])

        num = int(rule[0][2:])
        xmas_copy = xmas.copy()
        if rule[0][1] == "<":
            if xmas[to_modify][0] >= num:
                continue
            if xmas[to_modify][1] < num:
                track += do_workflow(rule[1], xmas)
                continue
            xmas_copy[to_modify] = (xmas[to_modify][0], num - 1)
            xmas[to_modify] = (num, xmas[to_modify][1])
            track += do_workflow(rule[1], xmas_copy)
        else:
            if xmas[to_modify][1] <= num:
                continue
            if xmas[to_modify][0] > num:
                track += do_workflow(rule[1], xmas)
                continue
            xmas_copy[to_modify] = (num + 1, xmas[to_modify][1])
            xmas[to_modify] = (xmas[to_modify][0], num)
            track += do_workflow(rule[1], xmas_copy)
    return track


aocd_submit(do_workflow("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]))
