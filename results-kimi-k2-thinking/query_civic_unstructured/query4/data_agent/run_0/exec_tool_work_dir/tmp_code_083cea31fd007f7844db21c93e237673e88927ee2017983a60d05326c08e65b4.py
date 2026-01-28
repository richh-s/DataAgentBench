code = """import json
import os
import re

# The result is stored as a string path to the JSON file
file_path = locals()['var_functions.query_db:5']

# Read the full result from the file
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Number of documents:', len(civic_docs))

# Show basic info
for i, doc in enumerate(civic_docs[:2]):
    print('\n', '-'*5, 'Document', i+1, '-'*5)
    print('Filename:', doc.get('filename', 'N/A'))
    print('Text length:', len(doc.get('text', '')))

# Show all filenames
print('\nAll filenames:')
for doc in civic_docs:
    print(' -', doc.get('filename', 'N/A'))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
