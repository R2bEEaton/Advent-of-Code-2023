from helpers.datagetter import aocd_data_in
import networkx as nx

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 1

G = nx.Graph()

for line in din:
    curr, others = line.split(": ")
    others = others.split(" ")
    for other in others:
        G.add_edge(curr, other)

for edge in nx.minimum_edge_cut(G):
    G.remove_edge(edge[0], edge[1])

for x in nx.connected_components(G):
    ans *= len(x)

aocd_submit(ans)
