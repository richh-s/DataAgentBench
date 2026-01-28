code = """import json
import re

# Load data files
mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Find park projects completed in 2022
park_projects_2022 = []
total_funding = 0

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Skip headers
        if line.startswith('Page') or line.startswith('Agenda'):
            continue
        if 'To:' in line or 'Prepared by:' in line or 'Approved by:' in line:
            continue
        if 'Subject:' in line or 'RECOMMENDED' in line or 'DISCUSSION:' in line:
            continue
        if 'Date prepared:' in line or 'Meeting date:' in line:
            continue
        if '(cid:' in line or line.startswith('Public Works') or line.startswith('Commission'):
            continue
            
        # Look for park projects
        if 'park' in line.lower() and len(line) > 5 and len(line) < 200:
            # Look ahead for completion in 2022
            for j in range(i+1, min(i+15, len(lines))):
                ahead = lines[j]
                ahead_lower = ahead.lower()
                
                has_completed = 'completed' in ahead_lower
                has_2022 = '2022' in ahead
                has_completion = 'completion' in ahead_lower
                has_nov_2022 = 'november 2022' in ahead_lower
                has_construction_complete = 'construction was completed' in ahead_lower
                
                if (has_completed and has_2022) or (has_completion and has_2022) or (has_nov_2022) or (has_construction_complete and has_2022):
                    clean_name = re.sub(r'^[\s\-•●■]+', '', line)
                    if clean_name:
                        park_projects_2022.append(clean_name)
                    break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match with funding
matched_projects = []
for proj in park_projects_2022:
    proj_lower = proj.lower()
    for fund_name in funding_map:
        fund_lower = fund_name.lower()
        if proj_lower == fund_lower or proj_lower in fund_lower or fund_lower in proj_lower:
            amount = funding_map[fund_name]
            total_funding += amount
            matched_projects.append({'project': proj, 'fund': fund_name, 'amount': amount})
            break

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}, 'var_functions.execute_python:58': {'mongo_docs_count': 19, 'funding_records_count': 500}}

exec(code, env_args)
