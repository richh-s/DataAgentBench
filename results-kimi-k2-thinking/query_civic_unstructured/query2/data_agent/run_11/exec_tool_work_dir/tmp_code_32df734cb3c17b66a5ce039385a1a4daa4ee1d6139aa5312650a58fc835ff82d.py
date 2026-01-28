code = """import json

civic_docs = var_functions.query_db:5
if type(civic_docs) is str:
    civic_docs = json.load(open(civic_docs))

projects = []
for doc in civic_docs:
    t = doc.get('text','')
    if 'Park' in t and 'completed' in t.lower() and '2022' in t:
        lines = t.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line)>10 and not line.startswith('('):
                if 'Subject' not in line and 'Page' not in line:
                    projects.append(line)

unique = list(set(projects))
print('__RESULT__:')
print(json.dumps({'projects': unique, 'count': len(unique)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
