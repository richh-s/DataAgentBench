code = """import json
import re

# Read the full MongoDB results
with open('var_functions.query_db:0', 'r') as f:
    civic_docs = json.load(f)

# Read the full SQLite funding results
with open('var_functions.query_db:2', 'r') as f:
    funding_data = json.load(f)

# Let's analyze the structure
print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'civic_docs_fields': list(civic_docs[0].keys()) if civic_docs else [],
    'funding_data_count': len(funding_data),
    'funding_data_sample': funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
