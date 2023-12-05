from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)
ans = 0

for i in range(len(din)):
    num = ""
    din[i] += "."
    for j in range(len(din[i])):
        char = din[i][j]
        if char.isdigit():
            num += char
        else:
            if len(num):
                breakout = False
                for offset in range(1, len(num) + 1):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if breakout:
                                break
                            try:
                                c = din[i+k][j-offset+l]
                                if not c.isdigit() and c != ".":
                                    ans += int(num)
                                    breakout = True
                            except:
                                None
            num = ""

aocd_submit(ans)
