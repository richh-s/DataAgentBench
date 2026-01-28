code = """import json
import re

# Load data from files
funding_path = locals()['var_functions.query_db:66']
civic_path = locals()['var_functions.query_db:67']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs_data = json.load(f)

# Build funding map
fund_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if name:
        fund_map[name] = amount

# Find disaster projects with 2022 dates
disaster_projs = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
        if 'Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]:
            proj = line
            is_disaster = False
            has_2022 = False
            for j in range(i+1, min(i+12, len(lines))):
                cl = lines[j].upper()
                checklist = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']
                for item in checklist:
                    if item in cl:
                        is_disaster = True
                if '2022' in cl and 'DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl:
                    has_2022 = True
            if is_disaster and has_2022:
                disaster_projs.append(proj)

disaster_projs = list(set(disaster_projs))

total_funding = 0
for proj in disaster_projs:
    for fproj, amt in fund_map.items():
        if proj in fproj or fproj in proj:
            total_funding += amt

result = {'total_funding': total_funding, 'disaster_projects': len(disaster_projs)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
