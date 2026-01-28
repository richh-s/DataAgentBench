code = """import json, re

mongo_file = str(locals()['var_functions.query_db:2'])
funding_file = str(locals()['var_functions.query_db:5'])

with open(mongo_file) as f:
    mongo_docs = json.load(f)
with open(funding_file) as f:
    funding_recs = json.load(f)

park_projs = []

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        if 'park' in line.lower() and len(line) > 5 and len(line) < 150:
            for j in range(i+1, min(i+12, len(lines))):
                if 'completed' in lines[j].lower() and '2022' in lines[j]:
                    clean = re.sub(r'^[\s\-•●■]+', '', line)
                    park_projs.append(clean)
                    break

park_projs = list(set(park_projs))

funding_map = {}
for rec in funding_recs:
    funding_map[rec['Project_Name']] = int(rec['Amount'])

total = 0
for proj in park_projs:
    for fund in funding_map:
        if proj.lower() in fund.lower() or fund.lower() in proj.lower():
            total += funding_map[fund]

result = {'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}}

exec(code, env_args)
