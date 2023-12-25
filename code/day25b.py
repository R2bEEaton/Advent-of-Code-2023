# This is the very slow, bad version lol

import itertools
from copy import deepcopy
import tqdm
from helpers.datagetter import aocd_data_in
from collections import defaultdict, deque

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

conns = defaultdict(set)
connections = []

for line in din:
    curr, others = line.split(": ")
    others = others.split(" ")
    for other in others:
        conns[curr].add(other)
        conns[other].add(curr)
        connections.append([curr, other])


def connects(a, b, c):
    visited = set()
    queue = deque([a])
    while queue:
        curr = queue.popleft()

        if curr == b:
            return True

        if curr in visited:
            continue
        visited.add(curr)

        for next in c[curr]:
            queue.append(next)
    return False


wires = list(conns.copy().keys())
for remove_wires in tqdm.tqdm(itertools.combinations(connections, r=3)):
    a, b, c = remove_wires

    conns_copy = deepcopy(conns)

    conns_copy[a[0]].discard(a[1])
    conns_copy[a[1]].discard(a[0])
    conns_copy[b[0]].discard(b[1])
    conns_copy[b[1]].discard(b[0])
    conns_copy[c[0]].discard(c[1])
    conns_copy[c[1]].discard(c[0])

    groups = [[wires[0]], []]
    bad = False
    for wire in wires[1:]:
        if connects(wires[0], wire, conns_copy):
            groups[0].append(wire)
        elif len(groups[1]) == 0 or connects(groups[1][0], wire, conns_copy):
            groups[1].append(wire)
        else:
            bad = True
            break

    if not bad and len(groups[0]) != 0 and len(groups[1]) != 0:
        ans = len(groups[0]) * len(groups[1])
        break

aocd_submit(ans)
