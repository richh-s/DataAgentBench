code = """import json
import re

# Read the data files
with open('/tmp/tmp9q1f0j8y.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmphg9s8x_1.json', 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for f in funding_data:
    try:
        funding_lookup[f['Project_Name'].lower()] = int(f['Amount'])
    except:
        pass

# Extract disaster projects that started in 2022
disaster_projects_2022 = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        # Check if project name contains disaster indicators
        if any(x in line.lower() for x in ['fema', 'caljpia', 'caloes', 'fire', 'disaster', 'emergency']):
            # Look for start date containing 2022
            for j in range(i+1, min(i+15, len(lines))):
                if '2022' in lines[j]:
                    disaster_projects_2022.append(line)
                    break

# Match with funding
total_funding = 0
matched = []
for proj_name in disaster_projects_2022:
    proj_lower = proj_name.lower()
    if proj_lower in funding_lookup:
        amount = funding_lookup[proj_lower]
        total_funding += amount
        matched.append({"project": proj_name, "amount": amount})

result_str = json.dumps({"total_funding": total_funding, "matched_projects": matched, "total_disaster_projects": len(disaster_projects_2022)})

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
