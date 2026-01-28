code = """import json
import re

# Load the data
with open('var_functions.query_db:6', 'r') as f:
    funding_records = json.load(f)

with open('var_functions.query_db:5', 'r') as f:
    civic_docs = json.load(f)

print('Funding records count:', len(funding_records))
print('Civic documents count:', len(civic_docs))

# Show first record structure
print('First funding record:', funding_records[0])
print('First civic doc keys:', list(civic_docs[0].keys()))

# Let's look at a sample of the text to understand structure
sample_text = civic_docs[0]['text'][:2000]
print('Sample text snippet:')
print(sample_text[:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
