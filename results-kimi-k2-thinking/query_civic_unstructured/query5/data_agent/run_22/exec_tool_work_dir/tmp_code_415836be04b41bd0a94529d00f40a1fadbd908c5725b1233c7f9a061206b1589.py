code = """import json

# Load data
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:7']

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    n = r.get('Project_Name', '')
    if n:
        fund_map[n] = fund_map.get(n, 0) + int(r.get('Amount', 0))

# Find disaster projects started in 2022
disaster_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Check if this doc has disaster keywords
    has_disaster = any(k in text.upper() for k in ['FEMA', 'CALOES', 'CALJPIA'])
    has_2022 = '2022' in text and ('DESIGN' in text.upper() or 'CONSTRUCTION' in text.upper() or 'BEGIN' in text.upper())
    
    if has_disaster and has_2022:
        lines = text.split('\n')
        for i in range(len(lines)-1):
            line = lines[i].strip()
            if not line or line.startswith('(') or 'page' in line.lower():
                continue
            if 'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]:
                disaster_projs.append(line)

# Remove duplicates
disaster_projs = list(set(disaster_projs))

# Calculate funding
total = 0
for proj in disaster_projs:
    for fproj, amt in fund_map.items():
        if proj in fproj or fproj in proj:
            total += amt
            break

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'disaster_projects': len(disaster_projs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
