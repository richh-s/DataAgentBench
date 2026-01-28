code = """import json

# Load previous result
res = json.loads(locals()['var_function-call-1225812636950463672'])
projects = res['projects']

# Load funding again to get details
with open(locals()['var_function-call-18189666317777667959'], 'r') as f:
    funding_list = json.load(f)

p_map = {p['Project_Name']: p['Amount'] for p in funding_list}

total = 0
print("Breakdown:")
for p in projects:
    amt = float(p_map.get(p, 0))
    print(f"{p}: {amt}")
    total += amt
    
print(f"Calculated Total: {total}")
print(f"Previous Total: {res['total_funding']}")"""

env_args = {'var_function-call-18189666317777669424': 'file_storage/function-call-18189666317777669424.json', 'var_function-call-18189666317777667959': 'file_storage/function-call-18189666317777667959.json', 'var_function-call-9598999800864405820': 'file_storage/function-call-9598999800864405820.json', 'var_function-call-1225812636950463672': {'count': 11, 'total_funding': 567000.0, 'projects': ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Bluffs Park Shade Structure', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)']}}

exec(code, env_args)
