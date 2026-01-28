code = """import json

# Load the funding data
funding_result = locals()['var_functions.query_db:2']
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_result

# Load civic docs
civic_result = locals()['var_functions.query_db:8']
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

# Debug info
print('Funding records:', len(funding_data))
print('Civic docs:', len(civic_docs))
print('First funding record:', funding_data[0] if funding_data else None)
print('First civic doc keys:', list(civic_docs[0].keys()) if civic_docs else None)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
