code = """import json

civic_docs_path = var_functions.query_db:5
civic_docs = json.load(open(civic_docs_path))

funding_path = var_functions.query_db:48
funding = json.load(open(funding_path))

park_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    if 'Park' in text and '2022' in text and 'completed' in text.lower():
        for line in text.split('\n'):
            line = line.strip()
            if 'Park' in line and len(line) > 5:
                if not line.startswith('(') and 'Subject' not in line and 'Page' not in line:
                    park_projects.append(line)

unique_parks = list(set(park_projects))
funding_total = 0
matches = []

for proj in unique_parks:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            funding_total += int(rec.get('Amount',0))
            matches.append({'project': proj, 'match': name, 'amount': int(rec.get('Amount',0))})

result = {'projects': unique_parks, 'count': len(unique_parks), 'total_funding': funding_total, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
