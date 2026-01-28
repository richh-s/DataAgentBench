code = """import json
import pandas as pd

f_key = 'var_function-call-9396770381544518491'
with open(locals()[f_key], 'r') as f:
    funding_data = json.load(f)

e_key = 'var_function-call-3853755936868958583'
with open(locals()[e_key], 'r') as f:
    extracted_data = json.load(f)

funding_map = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

unique_projects = set()
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']

for p in extracted_data:
    name = p['n'].strip()
    is_disaster = False
    for kw in disaster_keywords:
        if kw in name:
            is_disaster = True
            break
    
    if is_disaster and p['s']:
        unique_projects.add(name)

details = []
total = 0
for name in unique_projects:
    if name in funding_map:
        amt = funding_map[name]
        total += amt
        details.append({"name": name, "amount": amt})

print("__RESULT__:")
print(json.dumps({"projects": details, "total": total}))"""

env_args = {'var_function-call-9396770381544518491': 'file_storage/function-call-9396770381544518491.json', 'var_function-call-9396770381544517930': 'file_storage/function-call-9396770381544517930.json', 'var_function-call-3853755936868958583': 'file_storage/function-call-3853755936868958583.json', 'var_function-call-6428126987969155742': 273000.0}

exec(code, env_args)
