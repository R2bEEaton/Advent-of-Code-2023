from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

moved = True
while moved:
    moved = False
    for i in range(1, len(din)):
        for j in range(len(din[0])):
            if din[i][j] == "O" and din[i-1][j] == ".":
                din[i] = [c for c in din[i]]
                din[i][j] = "."
                din[i-1] = [c for c in din[i-1]]
                din[i-1][j] = "O"
                din[i] = "".join(din[i])
                din[i-1] = "".join(din[i-1])
                moved = True


for i in range(len(din)):
    ans += din[i].count("O") * (len(din) - i)

aocd_submit(ans)
