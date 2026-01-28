code = """import json, re, os

# Get file paths and load data
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:7']

with open(f_path, 'r') as f:
    funding = json.load(f)
with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    n = r.get('Project_Name', '')
    fund_map[n] = fund_map.get(n, 0) + int(r.get('Amount', 0))

# Find disaster projects with 2022 dates
disaster_projs = []
for doc in civic_docs:
    t = doc.get('text', '')
    lines = t.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower() or 'agenda item' in line.lower():
            continue
        if i < len(lines)-1 and any(x in lines[i+1] for x in ['Updates:', 'Project Schedule:']):
            name = line
            is_disaster = False
            has_2022 = False
            for j in range(i+1, min(i+10, len(lines))):
                cl = lines[j]
                if any(k in cl.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY']):
                    is_disaster = True
                if '2022' in cl and any(s in cl.upper() for s in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE']):
                    has_2022 = True
            if is_disaster and has_2022:
                disaster_projs.append(name)

# Calculate funding
total = 0
for dp in disaster_projs:
    for fn, amt in fund_map.items():
        if dp in fn or fn in dp or any(tok in fn for tok in dp.split() if len(tok) > 8):
            total += amt
            break

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'disaster_projects': len(disaster_projs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
