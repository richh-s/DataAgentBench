code = """import json

# Load the JSON files properly
with open('var_functions.query_db:20.json', 'r') as f:
    civic_docs = json.load(f)

print('Civic docs loaded successfully')
print('Number of documents:', len(civic_docs))
print('First document keys:', list(civic_docs[0].keys()))
print('Sample text snippet:', civic_docs[0]['text'][:200])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
