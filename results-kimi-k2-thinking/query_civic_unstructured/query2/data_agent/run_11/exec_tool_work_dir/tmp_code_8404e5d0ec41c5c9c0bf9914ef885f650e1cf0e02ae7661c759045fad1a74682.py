code = """import json
import sys

# Get the data from the previous tool results
civic_docs_data = var_functions.query_db:60
funding_data = var_functions.query_db:48

# Parse JSON strings if needed
if isinstance(civic_docs_data, str):
    civic_docs = json.loads(civic_docs_data)
else:
    civic_docs = civic_docs_data

if isinstance(funding_data, str):
    funding = json.loads(funding_data)
else:
    funding = funding_data

print('Documents:', len(civic_docs))
print('Funding records:', len(funding))
print('Sample doc:', str(civic_docs[0])[:200])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
