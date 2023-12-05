from helpers.datagetter import aocd_data_in

din, submit = aocd_data_in(split=True, numbers=False)

ans = 0
for game in din:
    id = int(game.split(":")[0].split(" ")[1])
    l = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round in game.split(": ")[1].split("; "):
        for shown in round.split(", "):
            if int(shown.split(" ")[0]) > l[shown.split(" ")[1]]:
                l[shown.split(" ")[1]] = int(shown.split(" ")[0])
    ans += l["red"] * l["green"] * l["blue"]

submit(ans)
