code = """import json
import re

# Load civic documents
civic_docs_file = '/tmp/tmpw8a01a0z.json'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding records  
funding_file = '/tmp/tmptjtu3_1d.json'
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Loaded {} civic documents'.format(len(civic_docs)))
print('Loaded {} funding records'.format(len(funding_records)))

# Show sample of first civic doc
doc = civic_docs[0]
print('\nFirst doc filename: {}'.format(doc.get('filename')))
print('Text length: {}'.format(len(doc.get('text', ''))))
print('Sample text: {}'.format(doc.get('text', '')[:700]))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
