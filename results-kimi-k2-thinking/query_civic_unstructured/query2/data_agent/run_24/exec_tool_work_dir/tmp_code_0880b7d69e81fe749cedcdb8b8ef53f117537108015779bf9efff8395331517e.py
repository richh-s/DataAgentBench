code = """import json
import re

# Load civic documents from the file path stored in var_functions_query_db_2  
with open(var_functions_query_db_2, 'r') as f:
    civic_docs = json.load(f)

# Load funding records from the file path stored in var_functions_query_db_8
with open(var_functions_query_db_8, 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(civic_docs), 'civic documents and', len(funding_records), 'funding records')

# Show first civic doc filename and text sample
first_doc = civic_docs[0]
print('\nFirst document filename:', first_doc.get('filename'))
print('Text length:', len(first_doc.get('text', '')))
print('Sample text:', first_doc.get('text', '')[:600])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
