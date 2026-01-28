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

print('Total funding records: ' + str(len(funding_data)))
print('Total civic documents: ' + str(len(civic_docs)))

# Show first record structure
first_funding = funding_data[0]
first_civic = civic_docs[0]
print('\nFirst funding record keys: ' + str(list(first_funding.keys())))
print('\nFirst civic doc keys: ' + str(list(first_civic.keys())))

# Print simple info
print('\nFirst funding record: ' + str(first_funding))
print('\nFirst civic doc snippet: ' + str(first_civic)[:200] + '...')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
