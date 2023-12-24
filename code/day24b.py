from helpers.datagetter import aocd_data_in
from z3 import *

din, aocd_submit = aocd_data_in(split=True, numbers=True)

rock = [Real('r%s' % i) for i in range(3)]
rock_v = [Real('rv%s' % i) for i in range(3)]
s = Solver()

for i in range(len(din)):
    point = din[i]
    t = Real('t%s' % i)
    for c in range(3):
        s.add(rock[c] + t*rock_v[c] == point[c] + t*point[3 + c])

if s.check() == sat:
    m = s.model()
    aocd_submit(sum([int(str(m.evaluate(v))) for v in rock]))
