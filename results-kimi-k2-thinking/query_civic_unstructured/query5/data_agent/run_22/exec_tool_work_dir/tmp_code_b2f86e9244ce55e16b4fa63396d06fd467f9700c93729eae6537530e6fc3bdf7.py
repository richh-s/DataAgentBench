code = """import json, re

# Load the data
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:7']

with open(f_path) as f:
    funding = json.load(f)
with open(c_path) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    n = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    if n:
        fund_map[n] = fund_map.get(n, 0) + amount

# Find disaster projects with 2022 dates from civic documents
disaster_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for project patterns
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
            
        # Check if this is a project name (next line has project info)
        if ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
            proj_name = line
            is_disaster = False
            has_2022 = False
            
            # Look ahead for disaster indicators and 2022 dates
            for j in range(i+1, min(i+10, len(lines))):
                cl = lines[j].upper()
                # Disaster keywords
                if 'FEMA' in cl or 'CALOES' in cl or 'CALJPIA' in cl or 'DISASTER' in cl or 'WOOLSEY' in cl:
                    is_disaster = True
                # 2022 date with project context
                if '2022' in cl and ('DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl):
                    has_2022 = True
            
            if is_disaster and has_2022 and proj_name:
                disaster_projs.append(proj_name)

# Filter for unique projects
disaster_projs = list(set(disaster_projs))

print('Found disaster projects with 2022 dates:', len(disaster_projs))
print('Sample projects:', disaster_projs[:3])

# Save results
result = {'found_projects': disaster_projs, 'funding_map_size': len(fund_map)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
