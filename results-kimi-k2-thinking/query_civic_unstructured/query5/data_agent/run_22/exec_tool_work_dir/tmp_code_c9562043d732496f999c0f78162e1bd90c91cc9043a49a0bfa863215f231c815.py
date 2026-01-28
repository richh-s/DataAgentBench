code = """import json, re

# Read and parse data
with open('var_functions.query_db:66') as f:
    funding = json.load(f)
with open('var_functions.query_db:67') as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    name = r['Project_Name']
    if name:
        fund_map[name] = fund_map.get(name, 0) + int(r['Amount'])

# Find disaster projects with 2022 dates
disaster_projs = []
for doc in civic_docs:
    text = doc['text']
    for i, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line or line.startswith('('):
            continue
        if i+1 < len(text.splitlines()):
            nxt = text.splitlines()[i+1].strip()
            if 'Updates:' in nxt or 'Project Schedule:' in nxt:
                proj = line
                is_disaster = False
                has_2022 = False
                for j in range(i+1, min(i+12, len(text.splitlines()))):
                    cl = text.splitlines()[j].upper()
                    if 'FEMA' in cl or 'CALOES' in cl:
                        is_disaster = True
                    if '2022' in cl and 'DESIGN' in cl:
                        has_2022 = True
                if is_disaster and has_2022:
                    disaster_projs.append(proj)

# Calculate total funding
total = 0
for proj in set(disaster_projs):
    for fproj, amt in fund_map.items():
        if proj in fproj or fproj in proj:
            total += amt

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'disaster_projects': len(set(disaster_projs))}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
