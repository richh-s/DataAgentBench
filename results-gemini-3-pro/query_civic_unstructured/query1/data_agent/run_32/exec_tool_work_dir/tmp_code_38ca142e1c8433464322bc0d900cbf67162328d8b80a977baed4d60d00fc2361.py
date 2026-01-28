code = """import json

funding_path = locals()["var_function-call-4570374009180656928"]

with open(funding_path, "r") as f:
    funding = json.load(f)

keywords = ["Morning", "Shoulder", "Slope", "Playground", "Water Treatment", "Civic Center"]

hits = []
for x in funding:
    name = x["Project_Name"]
    amt = x["Amount"]
    for kw in keywords:
        if kw in name:
            hits.append((name, amt))

print("__RESULT__:")
print(json.dumps(hits))"""

env_args = {'var_function-call-4570374009180656928': 'file_storage/function-call-4570374009180656928.json', 'var_function-call-12751430188961870496': 'file_storage/function-call-12751430188961870496.json', 'var_function-call-13689454801406461365': 'file_storage/function-call-13689454801406461365.json', 'var_function-call-6647682698323320664': ['Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH Median Improvements Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure']}

exec(code, env_args)
