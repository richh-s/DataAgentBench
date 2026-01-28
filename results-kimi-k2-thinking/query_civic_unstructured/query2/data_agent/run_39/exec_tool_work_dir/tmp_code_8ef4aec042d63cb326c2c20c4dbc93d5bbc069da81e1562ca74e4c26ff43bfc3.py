code = """import json
import re

mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'completed' in text.lower() and '2022' in text and 'park' in text.lower():
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if 'park' in line.lower():
                for j in range(i+1, min(i+10, len(lines))):
                    if 'completed' in lines[j].lower() and '2022' in lines[j]:
                        clean_name = re.sub(r'^[•\-●\s]+', '', line)
                        if clean_name and len(clean_name) < 200:
                            park_projects_2022.append(clean_name)
                        break

park_projects_2022 = list(set(park_projects_2022))

funding_map = {}
for f in funding_records:
    funding_map[f['Project_Name']] = int(f['Amount'])

total = 0
matches = []

for park in park_projects_2022:
    for fund_name in funding_map:
        if park.lower() in fund_name.lower() or fund_name.lower() in park.lower():
            amt = funding_map[fund_name]
            total += amt
            matches.append({'project': park, 'fund': fund_name, 'amount': amt})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'matched_projects': matches}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
