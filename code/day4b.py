from helpers.datagetter import aocd_data_in

din, submit = aocd_data_in(split=True, numbers=True)
copies = [1 for _ in range(len(din))]

for i in range(len(din)):
    card = din[i]
    winners = card[1:11]
    mine = card[11:]

    w = 0
    for num in winners:
        if num in mine:
            w += 1
    if w > 0:
        for j in range(i+1, i+w+1):
            copies[j] += copies[i]

ans = sum(copies)
submit(ans)
