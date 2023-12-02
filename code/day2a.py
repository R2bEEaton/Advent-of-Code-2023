from helpers.datagetter import data_in, submit

din = data_in(split=True, numbers=False)
l = {
    "red": 12,
    "green": 13,
    "blue": 14
}

ans = 0
for game in din:
    id = int(game.split(":")[0].split(" ")[1])
    good = True
    for round in game.split(": ")[1].split("; "):
        for shown in round.split(", "):
            if int(shown.split(" ")[0]) > l[shown.split(" ")[1]]:
                good = False
    if good:
        ans += id

submit(ans)
