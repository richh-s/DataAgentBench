code = """import json

# Load funding data with Amount > 50000
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_file = var_functions.query_db:6
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({'funding_count': len(funding_data), 'docs_count': len(civic_docs)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
