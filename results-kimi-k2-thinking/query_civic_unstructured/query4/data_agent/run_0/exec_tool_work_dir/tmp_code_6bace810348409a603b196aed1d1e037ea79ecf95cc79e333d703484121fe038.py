code = """import json
import os
import re

# The result is stored as a string path to the JSON file
file_path = locals()['var_functions.query_db:5']

# Read the full result from the file
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Number of documents:', len(civic_docs))
if civic_docs:
    print('First document keys:', list(civic_docs[0].keys()))
else:
    print('No documents')

# Show sample documents
for i, doc in enumerate(civic_docs[:3]):
    print('\n--- Document', i+1, '---')
    print('Filename:', doc.get('filename', 'N/A'))
    print('Text preview (first 500 chars):', (doc.get('text', ''))[:500], '...')

# Check if there are multiple documents
print('\nFilenames:')
for doc in civic_docs:
    print('-', doc.get('filename', 'N/A'))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
