code = """import json
import re

# Load funding data
f_path = locals()['var_functions.query_db:6']
with open(f_path) as f:
    funding = json.load(f)

# Load civic documents
c_path = locals()['var_functions.query_db:7']
with open(c_path) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    amt = int(r.get('Amount', 0))
    if name:
        fund_map[name] = fund_map.get(name, 0) + amt

# Find disaster projects with 2022 dates
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
            is_disaster = False
            has_2022 = False
            for j in range(i+1, min(i+12, len(lines))):
                cl = lines[j].upper()
                # Check disaster indicators
                if 'FEMA' in cl or 'CALOES' in cl or 'CALJPIA' in cl or 'DISASTER' in cl or 'WOOLSEY' in cl:
                    is_disaster = True
                # Check for 2022 dates with project context
                if '2022' in cl and ('DESIGN' in cl or 'CONSTRUCTION' in cl or 'BEGIN' in cl or 'COMPLETE' in cl):
                    has_2022 = True
            if is_disaster and has_2022:
                disaster_projs.append(proj)

# Filter unique projects
disaster_projs = list(set(disaster_projs))

# Calculate total funding
total = 0
for proj in disaster_projs:
    for fproj, amt in fund_map.items():
        if proj in fproj or fproj in proj:
            total += amt
            break
        # Check word overlap for partial matches
        proj_words = set([w for w in re.findall(r'\w+', proj) if len(w) > 7])
        fproj_words = set([w for w in re.findall(r'\w+', fproj) if len(w) > 7])
        if proj_words and len(proj_words.intersection(fproj_words)) > 0:
            total += amt
            break

result = {'total_funding_for_disaster_projects_started_2022': total, 'number_of_projects': len(disaster_projs)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
