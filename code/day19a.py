from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

workflows = {}

for i in range(len(din)):
    line = din[i]
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
    if w == "R":
        return False
    elif w == "A":
        return True

    x, m, a, s = xmas

    for rule in workflows[w]:
        if eval(str(rule[0])):
            return do_workflow(rule[1], xmas)


for j in range(i + 1, len(din)):
    line = din[j]
    xmas = [int(x.split("=")[1]) for x in line[1:-1].split(",")]
    if do_workflow("in", xmas):
        ans += sum(xmas)

aocd_submit(ans)
