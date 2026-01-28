code = """import json
import re

# Load data from file paths stored in variables
funding_path = str(locals()['var_functions.query_db:5'])
civic_docs_path = str(locals()['var_functions.query_db:8'])

print('Loading funding data from:', funding_path)
funding_records = json.loads(open(funding_path).read())

print('Loading civic docs from:', civic_docs_path)
civic_docs = json.loads(open(civic_docs_path).read())

print('Loaded', len(funding_records), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Show sample data
print('\nFirst funding record:', funding_records[0])
print('\nFirst civic doc keys:', list(civic_docs[0].keys())[:5])
print('\nText preview:', civic_docs[0]['text'][:250])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
