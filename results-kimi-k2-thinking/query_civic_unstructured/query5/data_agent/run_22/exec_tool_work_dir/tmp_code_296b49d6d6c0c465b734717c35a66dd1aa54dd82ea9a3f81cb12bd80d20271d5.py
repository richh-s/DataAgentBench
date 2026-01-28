code = """import json
import re

# Directly access the stored variables
funding_data = locals()['var_functions.query_db:6']
civic_docs_data = locals()['var_functions.query_db:7']

# Debug info
print(f"Funding records type: {type(funding_data)}")
print(f"Civic docs type: {type(civic_docs_data)}")

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    # It's a file path
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

if isinstance(civic_docs_data, str) and civic_docs_data.endswith('.json'):
    # It's a file path
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic docs: {len(civic_docs_data)}")
print("__RESULT__:")
print(json.dumps({"funding_count": len(funding_data), "civic_docs_count": len(civic_docs_data)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
