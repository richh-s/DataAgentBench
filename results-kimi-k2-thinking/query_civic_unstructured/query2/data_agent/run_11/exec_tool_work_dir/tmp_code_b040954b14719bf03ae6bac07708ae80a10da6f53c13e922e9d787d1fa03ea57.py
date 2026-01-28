code = """import json, re
civic_docs = var_functions.query_db:5
if type(civic_docs) is str:
    with open(civic_docs) as f:
        civic_docs = json.load(f)

funding = var_functions.query_db:6
if type(funding) is str:
    with open(funding) as f:
        funding = json.load(f)

park_2022 = []

for doc in civic_docs:
    t = doc.get('text','')
    if 'Park' in t and '2022' in t and 'completed' in t.lower():
        for line in t.split('\n'):
            line = line.strip()
            if 'Park' in line and len(line)>5 and not line.startswith('('):
                if 'Subject' not in line and 'Page' not in line and 'Item' not in line:
                    park_2022.append(line)

unique_parks = list(set(park_2022))
funding_total = 0
matches = []

for proj in unique_parks:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() == name.lower() or proj.lower() in name.lower() or name.lower() in proj.lower():
            funding_total += int(rec.get('Amount',0))
            matches.append({'project': proj, 'match': name, 'amount': int(rec.get('Amount',0))})

result = {'projects': unique_parks, 'count': len(unique_parks), 'funding': funding_total, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
