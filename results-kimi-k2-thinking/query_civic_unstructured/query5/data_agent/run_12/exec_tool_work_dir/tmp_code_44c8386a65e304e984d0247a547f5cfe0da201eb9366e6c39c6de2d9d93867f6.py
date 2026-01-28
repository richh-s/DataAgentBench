code = """import json
import pandas as pd

# Read the MongoDB results
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Print basic info
print(f'__RESULT__:')
print(f'Number of documents: {len(civic_docs_data)}')
print(f'First document keys: {list(civic_docs_data[0].keys())}')
print(f'First document preview: {str(civic_docs_data[0])[:500]}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
