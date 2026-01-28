code = """import json
import re
from collections import defaultdict

# Load funding data
funding_file = var_functions.query_db_2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Total funding records loaded:', len(funding_data))
print('Sample funding records:', funding_data[:3])

# Load civic_docs
civic_file = var_functions.query_db_6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('\nTotal civic documents loaded:', len(civic_docs))
print('Sample document keys:', list(civic_docs[0].keys()))

# Let's look at the first document's text to understand structure
first_doc_text = civic_docs[0].get('text', '')
print('\nFirst 2000 chars of first document:')
print(first_doc_text[:2000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
