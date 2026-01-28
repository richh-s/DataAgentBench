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

print('Total funding records:', len(funding_data))
print('Total civic documents:', len(civic_docs))

# Show first record structure
first_funding = funding_data[0]
first_civic = civic_docs[0]
print('\nFirst funding record keys:', list(first_funding.keys()))
print('\nFirst civic doc keys:', list(first_civic.keys()))

# Print simple info
print('\nFirst funding record:', first_funding)
print('\nFirst civic doc has text length:', len(first_civic.get('text', '')))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
