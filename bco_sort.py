import json

  

lines = open("../bcodb.json", "r").read().split("\n")

for line in lines:
    if line.strip() == "":
        continue
    bco_obj = json.loads(line)
    del bco_obj['_id']
    bco_id = 'OMX_' + bco_obj['bco_id'].split('/')[-1].split('_')[1]
    bco_obj['bco_id'] = 'http://data.oncomx.org/' + bco_id
    print(bco_obj['bco_id'])
    fileName = bco_id + '.json'
    print(fileName)
    with open(fileName, 'w+') as file:
        file.write(json.dumps(bco_obj, indent=4))