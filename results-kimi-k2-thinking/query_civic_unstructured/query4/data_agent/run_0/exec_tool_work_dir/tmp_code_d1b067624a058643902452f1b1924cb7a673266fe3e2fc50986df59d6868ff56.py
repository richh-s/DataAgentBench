code = """import json
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)
print('num_documents:', len(civic_docs))
for i in range(min(2, len(civic_docs))):
    print('doc', i, 'filename:', civic_docs[i].get('filename', ''))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
