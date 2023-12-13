from helpers.datagetter import aocd_data_in
from itertools import combinations

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0


def match(s, cont):
    out = []
    o = 0
    for char in s:
        if char == "#":
            o += 1
        else:
            if o:
                out.append(o)
                if len(out) > len(cont) or out[-1] != cont[len(out) - 1]:
                    return False
            o = 0
    if o:
        out.append(o)
    return out == cont

for line in din:
    contig = [int(x) for x in line.split(" ")[1].split(",")]
    qs = []
    for i in range(len(line.split(" ")[0])):
        if line[i] == "?":
            qs.append(i)
    combs = [()]
    for r in range(len(qs)):
        combs += combinations(qs, r + 1)

    #print(contig, qs)
    for comb in combs:
        l = list(line.split(" ")[0])
        for i in range(len(l)):
            if i in comb:
                l[i] = "#"
            elif i in qs:
                l[i] = "."
        if match("".join(l), contig):
            #print("".join(l))
            ans += 1

print(ans)
aocd_submit(ans)
