from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)
ans = 0

for code in din.split(","):
    current_value = 0
    for c in code:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    ans += current_value

aocd_submit(ans)
