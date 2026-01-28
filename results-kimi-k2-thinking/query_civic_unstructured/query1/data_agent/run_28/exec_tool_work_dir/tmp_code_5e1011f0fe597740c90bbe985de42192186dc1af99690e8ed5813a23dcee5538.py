code = """import json
import re

# Load the funding data
with open('funding_query.json', 'r') as f:
    funding_data = json.load(f)

print('Funding records count:', len(funding_data))
print('Sample funding record:', funding_data[0])

# Load the civic docs data
with open('civic_docs_query.json', 'r') as f:
    civic_docs_data = json.load(f)

print('Civic docs count:', len(civic_docs_data))
print('Sample civic doc keys:', list(civic_docs_data[0].keys()))

# Let's examine the text structure of the first document
text = civic_docs_data[0]['text']
print('First 500 chars of text:', text[:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
