code = """import json
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)
print('Number of docs:', len(civic_docs))
for i, doc in enumerate(civic_docs[:2]):
    print('\nDoc', i+1)
    print('filename:', doc.get('filename'))
    print('text length:', len(doc.get('text', '')))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
