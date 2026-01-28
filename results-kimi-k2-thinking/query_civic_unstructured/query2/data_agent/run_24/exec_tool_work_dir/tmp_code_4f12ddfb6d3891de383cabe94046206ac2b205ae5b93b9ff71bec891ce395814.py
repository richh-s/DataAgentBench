code = """import json
import re

# Access the stored result keys
civic_docs_file = var_functions_list_db_14
funding_file = var_functions_list_db_5

print("Civic docs file:", civic_docs_file)
print("Funding file:", funding_file)

# Load civic documents
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('\nNumber of civic documents:', len(civic_docs))
print('First document filename:', civic_docs[0].get('filename'))
print('First document text length:', len(civic_docs[0].get('text', '')))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
