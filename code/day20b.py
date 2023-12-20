from helpers.datagetter import aocd_data_in
from collections import defaultdict

din, aocd_submit = aocd_data_in(split=True, numbers=False)

modules = defaultdict(lambda: ("", []))
states = defaultdict(lambda: False)

for line in din:
    if line[0].isalpha():
        type = ""
    else:
        type = line[0]
        line = line[1:]
    name, out = line.split(" -> ")
    out = out.split(", ")
    modules[name] = (type, out)
    if type == "&":
        cons = {}
        for i in range(len(din)):
            if name in din[i].split(" -> ")[1].split(", "):
                cons[din[i].split(" -> ")[0] if din[i][0].isalpha() else din[i].split(" -> ")[0][1:]] = False
        states[name] = cons

lh = [0, 0]

periods = []
prereqs = {"vd", "ns", "bh", "dl"}

button_presses = 1
while True:
    queue = [("broadcaster", False)]
    while queue:
        name, pulse = queue.pop(0)
        output = None

        if modules[name][0] == "":
            output = pulse
        elif modules[name][0] == "%":
            states[name] = not states[name]
            output = states[name]
        elif modules[name][0] == "&":
            output = not all(states[name].values())
            if output:
                if name in prereqs:
                    periods.append(button_presses)
                    prereqs.remove(name)
                if len(prereqs) == 0:
                    ans = 1
                    for period in periods:
                        ans *= period
                    aocd_submit(ans)
                    exit()

        for out in modules[name][1]:
            if modules[out][0] == "%":
                if not output:
                    queue.append((out, pulse))
            elif modules[out][0] == "&":
                states[out][name] = output
                queue.append((out, None))

    button_presses += 1
