code = """import json
# Read the full result from the JSON file
with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'num_documents': len(civic_docs),
    'sample_doc': civic_docs[0] if civic_docs else None,
    'has_text_field': 'text' in civic_docs[0] if civic_docs else False
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json'], 'var_functions.execute_python:8': {'path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
