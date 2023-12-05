from helpers.datagetter import aocd_data_in, submit

din = aocd_data_in(split=True, numbers=True)
ans = 0

for card in din:
    winners = card[1:11]
    mine = card[11:]

    w = 0
    for num in winners:
        if num in mine:
            w += 1

    if w > 0:
        ans += 2 ** (w - 1)

submit(ans)
