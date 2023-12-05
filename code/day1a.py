from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

sum = 0
for line in din:
    sum += int(str("%s%s" % (str(line[0])[0], str(line[-1])[-1])))

aocd_submit(sum)
