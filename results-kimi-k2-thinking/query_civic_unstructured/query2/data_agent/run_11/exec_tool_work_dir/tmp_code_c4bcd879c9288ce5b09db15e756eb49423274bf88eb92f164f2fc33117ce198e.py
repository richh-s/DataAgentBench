code = """import json
import re

# Access the civic documents data
civic_docs_key = 'var_functions.query_db:5'
civic_docs_data = locals().get(civic_docs_key)

# If it's a file path, load the data
if isinstance(civic_docs_data, str) and '/tmp/' in civic_docs_data:
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

# Access the funding data
funding_key = 'var_functions.query_db:6'
funding_data = locals().get(funding_key)

# If it's a file path, load the data
if isinstance(funding_data, str) and '/tmp/' in funding_data:
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs_data) if civic_docs_data else 0,
    'funding_records_count': len(funding_data) if funding_data else 0,
    'status': 'Data loaded successfully'
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
