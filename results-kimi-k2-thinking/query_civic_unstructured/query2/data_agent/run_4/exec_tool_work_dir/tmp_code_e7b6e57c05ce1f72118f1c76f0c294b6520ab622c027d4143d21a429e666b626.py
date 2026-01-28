code = """import json

# Load the data from the stored variables
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Let's see what we're working with
if isinstance(civic_docs, str):
    # It's a file path
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str):
    # It's a file path
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'civic_sample_keys': list(civic_docs[0].keys()) if civic_docs else [],
    'funding_sample': funding_data[:3]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json']}

exec(code, env_args)
