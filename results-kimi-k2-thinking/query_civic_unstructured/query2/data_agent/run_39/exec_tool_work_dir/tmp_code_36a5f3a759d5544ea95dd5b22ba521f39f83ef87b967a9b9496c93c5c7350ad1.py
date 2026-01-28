code = """import json
import re

# Load both datasets
mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Build list of park projects completed in 2022
park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        
        if not line:
            continue
            
        # Skip obvious non-project lines
        if line.startswith('Page') or line.startswith('Agenda Item'):
            continue
        if 'To:' in line or 'Prepared by:' in line or 'Approved by:' in line:
            continue
        if line.startswith('Subject:') or line.startswith('RECOMMENDED ACTION:'):
            continue
        if '(cid:' in line:
            continue
            
        # Look for park in line (potential project name)
        if 'park' in line.lower() and 5 < len(line) < 150:
            # Look ahead for completion status
            for j in range(i, min(i + 10, len(lines))):
                ahead_line = lines[j]
                if 'completed' in ahead_line.lower() and '2022' in ahead_line:
                    clean_name = re.sub(r'^[\s\-\•●■]+', '', line)
                    if clean_name:
                        park_projects_2022.append(clean_name)
                    break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Build funding lookup map
funding_map = {}
for rec in funding_records:
    name = rec['Project_Name']
    amount = int(rec['Amount'])
    funding_map[name] = amount

# Calculate total funding by matching project names
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    proj_lower = proj.lower()
    for fund_name in funding_map:
        fund_lower = fund_name.lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            amount = funding_map[fund_name]
            total_funding += amount
            matched_projects.append({
                'project_name': proj,
                'funding_record_name': fund_name,
                'amount': amount
            })

result = {
    'total_funding_2022_park_projects': total_funding,
    'matched_projects': len(matched_projects),
    'details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}}

exec(code, env_args)
