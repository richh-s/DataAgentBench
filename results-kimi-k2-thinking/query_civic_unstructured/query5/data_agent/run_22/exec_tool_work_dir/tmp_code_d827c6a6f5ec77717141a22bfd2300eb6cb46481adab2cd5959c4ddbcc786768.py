code = """import json
import re

with open(locals()['var_functions.query_db:6']) as f:
    funding = json.load(f)
with open(locals()['var_functions.query_db:7']) as f:
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
                indicators = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']
                schedule_words = ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE']
                if any(x in cl for x in indicators):
                    is_dis = True
                if '2022' in cl and any(s in cl for s in schedule_words):
                    has_2022 = True
            if is_dis and has_2022:
                disaster_projs.append(proj)

total = 0
for proj in disaster_projs:
    for fproj, amt in fund_map.items():
        if proj in fproj or fproj in proj:
            total += amt
            break
        proj_parts = set([w for w in re.findall(r'\w+', proj) if len(w) > 7])
        fproj_parts = set([w for w in re.findall(r'\w+', fproj) if len(w) > 7])
        if proj_parts and len(proj_parts.intersection(fproj_parts)) > 0:
            total += amt
            break

result = {'total_funding': total, 'disaster_projects': len(disaster_projs), 'sample_projects': disaster_projs[:3]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
