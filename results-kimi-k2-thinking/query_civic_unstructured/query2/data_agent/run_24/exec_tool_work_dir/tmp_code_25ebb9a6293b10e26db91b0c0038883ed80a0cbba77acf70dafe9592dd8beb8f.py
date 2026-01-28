code = """import json
import re

# First, let's examine the structure of the civic documents
with open('/tmp/tmpw8a01a0z.json', 'r') as f:
    civic_docs = json.load(f)

print('Number of civic documents:', len(civic_docs))
print('\nFirst document snippet:')
first_doc = civic_docs[0]
print('Filename:', first_doc.get('filename'))
print('Text length:', len(first_doc.get('text', '')))
print('\nFirst 1000 chars of text:')
print(first_doc.get('text', '')[:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
