from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
din[0] = int(din[0].split(":")[1].replace(" ", ""))
din[1] = int(din[1].split(":")[1].replace(" ", ""))
ans = 1


def compute_score(hold_time, total_time):
    return (total_time-hold_time) * hold_time


wins = []
for j in range(din[0]):
    if compute_score(j, din[0]) > din[1]:
        wins.append(j)
ans *= len(wins)

aocd_submit(ans)
