code = """import json

funding_path = locals()["var_function-call-4570374009180656928"]
with open(funding_path, "r") as f:
    funding = json.load(f)

hits = []
for x in funding:
    if "Resurfacing" in x["Project_Name"] or "Morning" in x["Project_Name"]:
        hits.append(x)

print("__RESULT__:")
print(json.dumps(hits))"""

env_args = {'var_function-call-4570374009180656928': 'file_storage/function-call-4570374009180656928.json', 'var_function-call-12751430188961870496': 'file_storage/function-call-12751430188961870496.json', 'var_function-call-13689454801406461365': 'file_storage/function-call-13689454801406461365.json', 'var_function-call-6647682698323320664': ['Malibu Bluffs Park South Walkway Repairs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH Median Improvements Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure'], 'var_function-call-15717659823703027698': [['Civic Center Stormwater Diversion Structure', '64000'], ['Trancas Canyon Park Playground Resurfacing', '65000'], ['Trancas Canyon Park Slope Stabilization Project', '68000'], ['Trancas Playground Resurfacing', '90000'], ['Westward Beach Road Shoulder Repairs (CalOES Project)', '77000']]}

exec(code, env_args)
