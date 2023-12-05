from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "|", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in din:
    first = len(line)
    first_dig = -1
    last = 0
    last_dig = 0
    for dig in digits:
        if str(dig) not in line:
            continue
        if line.index(str(dig)) <= first:
            first = line.index(str(dig))
            first_dig = dig
        if line.rindex(str(dig)) >= last:
            last = line.rindex(str(dig))
            last_dig = dig
    first_dig = digits.index(first_dig) % 10
    last_dig = digits.index(last_dig) % 10
    sum += int(str("%s%s" % (first_dig, last_dig)))

aocd_submit(sum)
