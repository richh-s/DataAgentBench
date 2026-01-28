code = """import json
# Read the full result from the JSON file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Show the structure of one document
print('__RESULT__:')
print(json.dumps({
    'num_documents': len(civic_docs),
    'sample_doc': civic_docs[0] if civic_docs else None
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
