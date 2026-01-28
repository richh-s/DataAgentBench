code = """import json

docs_key = "var_function-call-4014968237340429633"
with open(locals()[docs_key], "r") as f:
    docs_data = json.load(f)

targets = ["Legacy Park Paver Repair Project", "Legacy Park Benches and Arbors Renovation"]
res = {}

for t in targets:
    res[t] = "Not Found"
    for d in docs_data:
        if t in d["text"]:
            start = d["text"].find(t)
            res[t] = d["text"][start:start+800]
            break

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json', 'var_function-call-2811947825801822237': {'matches': ['Malibu Park Drainage Improvements', 'Permanent Skate Park', 'Bluffs Park Shade Structure'], 'total': 135000}, 'var_function-call-2620570463614741313': {'matches': ['Malibu Park Drainage Improvements', 'Bluffs Park Shade Structure'], 'total': 38000}, 'var_function-call-1494925959871915800': ['Malibu Park Drainage Improvements\n\n(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert\nRoad, Morning View Drive, Busch Drive, Harvester Road and Birdview\nAvenue. This project is scheduled to be accepted by the Council at the\nJanuary 24, 2022 meeting.\n\nClover Heights Storm Drain (FEMA Project)\n\n(cid:190) Project Description: This project consists of design and construction of a few\nstorm drains on Clover Heights. The existing storm drain facility ends at the\ninters'], 'var_function-call-9950525588550440390': ['Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas Playground Resurfacing\n\n(cid:190) Project Description: The project will include removing and replac']}

exec(code, env_args)
