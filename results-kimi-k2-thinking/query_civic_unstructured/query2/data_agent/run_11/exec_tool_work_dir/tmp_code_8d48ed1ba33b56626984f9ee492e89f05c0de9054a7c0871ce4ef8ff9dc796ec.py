code = """import json
civic_docs = var_functions.query_db:5
if type(civic_docs) is str:
    with open(civic_docs) as f:
        civic_docs = json.load(f)

park_names = []
for doc in civic_docs:
    text = doc.get('text','')
    if 'Park' in text and 'completed' in text.lower() and '2022' in text:
        for line in text.splitlines():
            line = line.strip()
            if 'Park' in line and len(line) > 10:
                if not line.startswith('(') and 'Subject' not in line and 'Page' not in line:
                    park_names.append(line)

unique_parks = list(set(park_names))
print('__RESULT__:')
print(json.dumps({'parks': unique_parks, 'count': len(unique_parks)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
