code = """import json
import re

mongo_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        
        if not line:
            continue
        
        lowercase_line = line.lower()
        
        # Skip headers
        skip_headers = ['page', 'agenda', 'to:', 'prepared', 'approved', 'subject:', 'recommended', 'discussion:', 'date', 'meeting', 'public', 'commission', 'cid:']
        if any(header in line.lower() for header in skip_headers):
            continue
            
        # Look for park projects
        if 'park' in lowercase_line and 5 < len(line) < 200:
            # Look ahead for completion in 2022
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j]
                if 'completed' in next_line.lower() and '2022' in next_line:
                    clean_name = re.sub(r'^[\s\-•●■]+', '', line)
                    park_projects_2022.append(clean_name)
                    break

park_projects_2022 = list(set(park_projects_2022))

# Build funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Match and sum
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    for fund_proj in funding_map:
        proj_lower = proj.lower()
        fund_lower = fund_proj.lower()
        
        if proj_lower in fund_lower or fund_lower in proj_lower:
            amt = funding_map[fund_proj]
            total_funding += amt
            matched_projects.append({'project': proj, 'funding_name': fund_proj, 'amount': amt})

result = {
    'park_projects_2022': park_projects_2022,
    'total_funding': total_funding,
    'matched_details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}}

exec(code, env_args)
