code = """import json

civic_docs_file = locals()['var_functions.query_db:6']
print('File path:', civic_docs_file)

# Read the file
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

print('Number of docs:', len(civic_docs_data))
print('First doc keys:', list(civic_docs_data[0].keys()))
print('Sample text preview:', civic_docs_data[0]['text'][:200])

result = {'file_path': civic_docs_file, 'doc_count': len(civic_docs_data)}
print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
