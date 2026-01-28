code = """import json
import re

mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []
keywords = ['park', 'completed', '2022']

for doc in mongo_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    if all(k in text_lower for k in ['park', 'completed']) and '2022' in text:
        lines = re.split(r'[\r\n]+', text)
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            if 'park' in line.lower() and len(line) > 5 and len(line) < 200:
                for j in range(i+1, min(i+15, len(lines))):
                    if 'completed' in lines[j].lower() and '2022' in lines[j]:
                        clean = re.sub(r'^[\s\-•●■]+', '', line)
                        park_projects_2022.append(clean)
                        break

park_projects_2022 = list(set(park_projects_2022))

# Build funding map
funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

# Match and sum
total = 0
for proj in park_projects_2022:
    proj_lower = proj.lower()
    for fund_name in funding_map:
        if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
            total += funding_map[fund_name]

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}}

exec(code, env_args)
