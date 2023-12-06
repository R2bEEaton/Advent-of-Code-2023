import os

import requests
import json
from datetime import datetime, time, timedelta

# Create markdown files
for file in os.listdir("../code"):
    if not file.endswith(".py"):
        continue
    fname = "".join([i for i in file if i.isdigit()])
    if os.path.exists("%s.md" % fname):
        continue

    r = requests.get("https://adventofcode.com/2023/leaderboard/private/view/144198.json", cookies={'session': open("../code/helpers/sess", "r").read()})
    r = json.loads(r.text)

    parta, delta, partb = "0:00", "0:00", "0:00"

    for key, player in r["members"].items():
        if player["name"] == "Ryan Eaton":
            try:
                midnight = datetime.combine(datetime.today(), time.min).timestamp()
                parta = str(timedelta(seconds=player["completion_day_level"][fname]["1"]["get_star_ts"] - midnight))
                while parta[0] in ["0", ":"]:
                    parta = parta[1:]
                print(parta)
                delta = str(timedelta(seconds=player["completion_day_level"][fname]["2"]["get_star_ts"] - player["completion_day_level"][fname]["1"]["get_star_ts"]))
                while delta[0] in ["0", ":"]:
                    delta = delta[1:]
                partb = str(timedelta(seconds=player["completion_day_level"][fname]["2"]["get_star_ts"] - midnight))
                while partb[0] in ["0", ":"]:
                    partb = partb[1:]
                break
            except:
                None

    with open("%s.md" % fname, "w+") as f:
        f.write("""# Day %s
brief note

|      | Part 1 | Part 2 | Total |
|------|--------|--------|-------|
| Time | %s | %s | %s |

## Part 1
brief notes
```python
%s
```

## Part 2
brief notes
```python
%s
```""" % (fname, parta, delta, partb, open("../code/day%sa.py" % fname).read(), open("../code/day%sb.py" % fname).read()))

# Replace contents of all existing files
"""for file in os.listdir():
    if not file.endswith(".md"):
        continue
    with open(file, 'r+') as f:
        contents = f.read()

        contents = contents.split("```")
        print(contents)
        contents[1] = "python\n" + open("../code/day%sa.py" % file.split(".md")[0]).read()
        contents[3] = "python\n" + open("../code/day%sb.py" % file.split(".md")[0]).read()

        f.seek(0)
        f.write("```".join(contents))
        f.truncate()"""