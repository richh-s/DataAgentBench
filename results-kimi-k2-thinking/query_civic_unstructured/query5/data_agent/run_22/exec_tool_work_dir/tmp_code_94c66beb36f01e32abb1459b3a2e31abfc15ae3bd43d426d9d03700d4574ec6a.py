code = """import json, re

with open(locals()['var_functions.query_db:66']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:67']) as f:
    civic_docs = json.load(f)

fund_map = {}
for r in funding:
    n = r.get('Project_Name', '')
    if n:
        fund_map[n] = fund_map.get(n, 0) + int(r.get('Amount', 0))

disaster_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or line.startswith('('):
            continue
        if 'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]:
            proj = line
            is_disaster = False
            has_2022 = False
            for j in range(i+1, min(i+12, len(lines))):
                cl = lines[j].upper()
                for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']:
                    if ind in cl:
                        is_disaster = True
                if '2022' in cl and ('DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl):
                    has_2022 = True
            if is_disaster and has_2022:
                disaster_projs.append(proj)

# Remove duplicates and add disaster project variations
disaster_projs = list(set(disaster_projs))

# Also check for projects with (FEMA Project) suffixes in funding and add to total
total = 0
for fproj, amt in fund_map.items():
    if 'FEMA' in fproj.upper() or 'CALOES' in fproj.upper() or 'CALJPIA' in fproj.upper() or 'WOOLSEY' in fproj.upper():
        # Check if this could be a 2022 project
        total += amt

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'disaster_projects': len(disaster_projs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
