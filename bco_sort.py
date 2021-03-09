import json

  

lines = open("bcodb.json", "r").read().split("\n")

for line in lines:
    if line.strip() == "":
        continue
    bco_obj = json.loads(line)
    print json.dumps(bco_obj, indent=4)