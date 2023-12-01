import keyboard
import re
from collections import defaultdict


def data_in(split=True, numbers=False, n_type=int):
    print("| CTRL Ex  |  SHFT R |")
    key = keyboard.read_key()
    data_ver = "Real"

    if key == 'ctrl':
        data = open("testdata1.txt").read()
        data_ver = "Test"
    else:
        import aocd
        with open("helpers/sess") as f:
            sess = f.readline()
        data = aocd.get_data(session=sess)
        with open("aoc.txt", "w+") as f:
            f.write(data)

    # Parse
    if split:
        data = data.split("\n")
    if numbers:
        out = []
        for line in (data if type(data) == list else data.split("\n")):
            out.append(get_numbers(line, n_type))
        data = out

    print("| %s Data loaded.  |\n|====================|" % data_ver)
    return data


def submit(ans):
    import aocd
    with open("sess") as f:
        sess = f.readline()
    aocd.submit(answer=ans, session=sess)


def get_numbers(a, t):
    return list(map(t, re.findall(r'(?:-)?\d+(?:\.\d+)?', a)))
