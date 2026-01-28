code = """import json
import re

# Load data from files
mongo_file = str(locals()['var_functions.query_db:2'])
funding_file = str(locals()['var_functions.query_db:5'])

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        stripped = line.strip()
        
        if not stripped:
            continue
        
        # Check for park in project name
        if 'park' in stripped.lower() and 5 < len(stripped) < 200:
            # Look for completion in 2022 in nearby lines
            for j in range(i+1, min(i+15, len(lines))):
                ahead = lines[j]
                ahead_lower = ahead.lower()
                if 'completed' in ahead_lower and '2022' in ahead:
                    clean = re.sub(r'^[\s\-•●■]+', '', stripped)
                    park_projects_2022.append(clean)
                    break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Create funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Match projects with funding
total_funding = 0
matched = []

for park_proj in park_projects_2022:
    park_proj_lower = park_proj.lower()
    for fund_name in funding_map:
        fund_lower = fund_name.lower()
        if park_proj_lower in fund_lower or fund_lower in park_proj_lower:
            amount = funding_map[fund_name]
            total_funding += amount
            matched.append({'project': park_proj, 'fund': fund_name, 'amount': amount})

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}}

exec(code, env_args)
