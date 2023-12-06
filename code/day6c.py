from helpers.datagetter import aocd_data_in
import math

din, aocd_submit = aocd_data_in(split=True, numbers=False)
din = [int(i.split(":")[1].replace(" ", "")) for i in din]

intercept = math.ceil((-din[0] + math.sqrt(din[0] ** 2 - (4 * din[1]))) / -2)
ans = din[0] - 2 * intercept + 1

aocd_submit(ans)
