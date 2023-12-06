from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)
ans = 1


def compute_score(hold_time, total_time):
    return (total_time-hold_time) * hold_time


for i in range(len(din[0])):
    print(din[0][i], din[1][i])
    wins = []
    for j in range(din[0][i]):
        if compute_score(j, din[0][i]) > din[1][i]:
            wins.append(j)
    ans *= len(wins)

aocd_submit(ans)
