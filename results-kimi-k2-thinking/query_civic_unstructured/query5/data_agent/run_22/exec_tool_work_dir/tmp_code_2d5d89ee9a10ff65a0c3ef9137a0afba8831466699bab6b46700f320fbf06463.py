code = """import json, re

funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:7']

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    if name:
        fund_map[name] = fund_map.get(name, 0) + int(r.get('Amount', 0))

disaster_projs = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
        if 'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]:
            proj = line
            is_dis = False
            has_2022 = False
            for j in range(i+1, min(i+12, len(lines))):
                cl = lines[j].upper()
                # Check for disaster indicators
                for indicator in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']:
                    if indicator in cl:
                        is_dis = True
                        break
                # Check for 2022 dates with project context
                if '2022' in cl:
                    for sw in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE']:
                        if sw in cl:
                            has_2022 = True
                            break
            if is_dis and has_2022:
                disaster_projs.append(proj)

# Remove duplicates
unique_disaster_projs = list(set(disaster_projs))

total_funding = 0
for proj in unique_disaster_projs:
    for fproj, amt in fund_map.items():
        # Match by name
        if proj in fproj or fproj in proj:
            total_funding += amt
            break

result = {'total_funding': total_funding, 'disaster_projects': len(unique_disaster_projs)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
