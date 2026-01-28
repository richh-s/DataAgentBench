code = """import json

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:6']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Number of documents:', len(civic_docs))

# Simple extraction: look for park-related projects with 2022 completion
text_combined = ' '.join([doc['text'] for doc in civic_docs])

print('Text length:', len(text_combined))
print('__RESULT__:', json.dumps({'text_length': len(text_combined), 'doc_count': len(civic_docs)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'status': 'loaded', 'count': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': {'file_path': 'file_storage/functions.query_db:6.json', 'doc_count': 5}}

exec(code, env_args)
