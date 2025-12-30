code = """import json

funding_file = locals()['var_function-call-16963672935343025941']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

target_projects = [
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)",
    "Latigo Canyon Road Culvert Repairs (FEMA Project)",
    "Malibu Road Slope Repairs (CalOES Project)",
    "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)",
    "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)",
    "Westward Beach Road Shoulder Repairs (CalOES Project)"
]

total_funding = 0
found_projects = []

for record in funding_data:
    name = record['Project_Name'].strip()
    if name in target_projects:
        amount = int(record['Amount'])
        total_funding += amount
        found_projects.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-11045079689153923464': 'file_storage/function-call-11045079689153923464.json', 'var_function-call-17870921543984633070': 'file_storage/function-call-17870921543984633070.json', 'var_function-call-16963672935343025941': 'file_storage/function-call-16963672935343025941.json'}

exec(code, env_args)
