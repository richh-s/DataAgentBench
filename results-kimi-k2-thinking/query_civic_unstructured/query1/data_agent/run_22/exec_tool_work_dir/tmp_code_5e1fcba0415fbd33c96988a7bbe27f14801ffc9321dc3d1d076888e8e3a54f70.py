code = """import json
import re

# Read the funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

result = {}
result['total_funding_records'] = len(funding_data)
result['total_civic_docs'] = len(civic_docs)

# Show first record structure
result['first_funding_keys'] = list(funding_data[0].keys()) if funding_data else []
result['first_civic_keys'] = list(civic_docs[0].keys()) if civic_docs else []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
