code = """import json
import re

# Load data from file paths
civic_docs = json.load(open(var_functions_query_db_2, 'r'))
funding_records = json.load(open(var_functions_query_db_8, 'r'))

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Show first document details
first = civic_docs[0]
print('First doc filename:', first.get('filename'))
print('Text length:', len(first.get('text', '')))
print('Sample:', first.get('text', '')[:800])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
