from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 0

def get_diff(l):
    o = []
    for i in range(len(l)-1):
        o.append(l[i+1] - l[i])
    return o


def get_diffs(l):
    o = [l]
    while any([x != 0 for x in l]):
        l = get_diff(l)
        o.append(l)
    return o


for line in din:
    diffs = get_diffs(line)
    diffs[-1].insert(0, 0)
    for i in range(len(diffs)-2, -1, -1):
        diffs[i].insert(0, diffs[i][0] - diffs[i+1][0])
    ans += diffs[0][0]

aocd_submit(ans)
