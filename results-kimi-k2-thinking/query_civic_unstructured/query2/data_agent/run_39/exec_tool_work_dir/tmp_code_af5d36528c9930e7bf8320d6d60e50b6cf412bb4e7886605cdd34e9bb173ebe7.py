code = """import json
import re

mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Look for park projects completed in 2022 in the MongoDB documents
park_projects = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Find project sections and check for park completion in 2022
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'park' in line.lower():
            # Look ahead for completion info
            for j in range(i+1, min(i+15, len(lines))):
                if 'completed' in lines[j].lower() and '2022' in lines[j]:
                    # Clean up the project name
                    proj_name = line.strip()
                    # Remove bullet points and special chars
                    proj_name = re.sub(r'^[•\-●■\s]+', '', proj_name)
                    if proj_name and len(proj_name) < 200:
                        park_projects.append(proj_name)
                    break

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding data and sum amounts
project_names_in_funding = [f.get('Project_Name', '') for f in funding_records]
funding_map = {}
for f in funding_records:
    funding_map[f.get('Project_Name', '')] = int(f.get('Amount', 0))

total_funding = 0
matched_projects = []

for park_proj in park_projects:
    for fund_name in project_names_in_funding:
        # Check for exact or close matches
        if park_proj.lower() in fund_name.lower() or fund_name.lower() in park_proj.lower():
            amount = funding_map.get(fund_name, 0)
            total_funding += amount
            matched_projects.append({
                'project': park_proj,
                'matched_funding_name': fund_name,
                'amount': amount
            })

result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
