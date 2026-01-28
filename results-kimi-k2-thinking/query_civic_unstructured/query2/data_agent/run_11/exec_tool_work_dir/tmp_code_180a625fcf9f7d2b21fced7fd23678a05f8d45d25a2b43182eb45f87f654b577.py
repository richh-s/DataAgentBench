code = """import json
c_docs = json.load(open(var_functions.query_db:5))
funding = json.load(open(var_functions.query_db:48))

park2022 = []

for doc in c_docs:
    t = doc.get('text','')
    if 'Park' in t and '2022' in t and 'completed' in t.lower():
        for line in t.split('\n'):
            line = line.strip()
            if 'Park' in line and len(line)>5 and not line.startswith('('):
                if 'Subject' not in line and 'Page' not in line:
                    park2022.append(line)

unique = list(set(park2022))
total = 0
matches = []

for proj in unique:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            total += int(rec.get('Amount',0))
            matches.append([proj, name, int(rec.get('Amount',0))])

print('__RESULT__:')
print(json.dumps({'projects': unique, 'count': len(unique), 'funding': total, 'matches': matches}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
