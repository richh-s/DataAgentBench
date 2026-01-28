code = """import json
import re

# Load data from known file paths
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding_records = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Loaded data successfully')
print('Civic docs count:', len(civic_docs))
print('Funding records count:', len(funding_records))

# Display sample of first civic document
first_doc = civic_docs[0]
print('\nFirst document filename:', first_doc.get('filename'))
print('First document text length:', len(first_doc.get('text', '')))
print('\nFirst 600 chars of text:')
print(first_doc.get('text', '')[400:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
