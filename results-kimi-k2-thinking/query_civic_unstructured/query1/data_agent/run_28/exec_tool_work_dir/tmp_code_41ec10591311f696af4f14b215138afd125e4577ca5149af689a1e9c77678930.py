code = """import json
import re

# Load data from the file paths
funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('Funding records loaded:', len(funding_records))
print('Civic docs loaded:', len(civic_docs))

# Show sample funding record
print('\nSample funding record:', funding_records[0])

# Show sample civic doc structure
print('\nSample civic doc keys:', list(civic_docs[0].keys()))
print('Sample civic doc text preview:', civic_docs[0]['text'][:300])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
