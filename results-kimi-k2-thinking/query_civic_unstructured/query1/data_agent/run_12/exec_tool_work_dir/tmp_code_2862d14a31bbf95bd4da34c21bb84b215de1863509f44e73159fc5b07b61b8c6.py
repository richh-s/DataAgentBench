code = """import json

# Access variables using locals()
funding_file_path = locals()['var_functions.query_db:0']
civic_file_path = locals()['var_functions.query_db:1']

# Read funding data
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data
with open(civic_file_path, 'r') as f:
    civic_docs_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'funding_records': len(funding_data),
    'civic_docs': len(civic_docs_data),
    'sample_funding': funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
