code = """import json
import os

# Get file paths from stored variables
civic_docs_path = '/tmp/tmp2d2u8k1a.json'
funding_path = '/tmp/tmp0k5s9q8h.json'

print('Reading civic docs from:', civic_docs_path)
print('Reading funding from:', funding_path)

# Load the data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_data), 'funding records')

# Show first civic doc info
if len(civic_docs) > 0:
    print('First doc filename:', civic_docs[0].get('filename'))
    print('First doc text length:', len(civic_docs[0].get('text', '')))

# Show sample funding records
print('Sample funding records:')
for i in range(min(3, len(funding_data))):
    print(' ', funding_data[i])

result = {
    'status': 'loaded',
    'civic_docs': len(civic_docs),
    'funding_records': len(funding_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
