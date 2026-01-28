code = """import json
import re

# Load data from stored file paths
funding_path = locals()['var_functions.query_db:6']
civic_path = locals()['var_functions.query_db:7']

with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    name = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    fund_map[name] = fund_map.get(name, 0) + amount

# Extract disaster projects with 2022 dates
disaster_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower():
            continue
        # Check if this is a project header
        if i < len(lines)-1 and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
            proj_name = line
            is_disaster = False
            has_2022 = False
            # Check next 10 lines for indicators
            for j in range(i+1, min(i+10, len(lines))):
                cline = lines[j].upper()
                if any(k in cline for k in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY', 'RECOVERY']):
                    is_disaster = True
                if '2022' in cline and any(s in cline for s in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'SCHEDULE']):
                    has_2022 = True
            if is_disaster and has_2022:
                disaster_2022.append(proj_name)

# Calculate total funding
total = 0
for proj in disaster_2022:
    for fproj, amt in fund_map.items():
        if proj == fproj or proj in fproj or fproj in proj:
            total += amt
            break
        # Check significant word matches
        proj_words = set([w for w in proj.replace('&', ' ').replace('-', ' ').split() if len(w) > 6])
        fproj_words = set([w for w in fproj.replace('&', ' ').replace('-', ' ').split() if len(w) > 6])
        if len(proj_words.intersection(fproj_words)) > 1:
            total += amt
            break

print('__RESULT__:')
print(json.dumps({
    'total_funding': total,
    'disaster_projects': len(disaster_2022),
    'funding_map_size': len(fund_map)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
