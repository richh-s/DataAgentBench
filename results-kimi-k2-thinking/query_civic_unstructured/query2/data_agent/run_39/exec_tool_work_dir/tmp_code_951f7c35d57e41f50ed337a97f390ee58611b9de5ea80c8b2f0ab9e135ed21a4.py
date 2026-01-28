code = """import json
import re

# Read MongoDB data from file
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Read funding data from file
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Find all park projects completed in 2022
park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    # Find patterns like "Bluffs Park Shade Structure" with completion in 2022
    
    # Split into lines
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        line_lower = line.lower()
        
        # Check if line contains park (potential project name)
        if 'park' in line_lower:
            # Skip if it's a header or too short/long
            if len(line) < 5 or len(line) > 200:
                continue
            if any(line.startswith(x) for x in ['Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Date', 'Meeting', 'Public', 'Commission', 'Capital']):
                continue
            if '(cid:' in line:
                continue
                
            # Look ahead for completion date
            for j in range(i+1, min(i+15, len(lines))):
                ahead_line = lines[j]
                if 'completed' in ahead_line.lower() and '2022' in ahead_line:
                    park_projects_2022.append(line)
                    break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Build funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Match projects with funding
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    for fund_proj in funding_map:
        proj_lower = proj.lower()
        fund_lower = fund_proj.lower()
        
        # Check if they match (partial match in either direction)
        if proj_lower in fund_lower or fund_lower in proj_lower:
            amt = funding_map[fund_proj]
            total_funding += amt
            matched_projects.append({'project': proj, 'funding_name': fund_proj, 'amount': amt})

result = {
    'park_projects_2022': park_projects_2022,
    'matched_funding': matched_projects,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
