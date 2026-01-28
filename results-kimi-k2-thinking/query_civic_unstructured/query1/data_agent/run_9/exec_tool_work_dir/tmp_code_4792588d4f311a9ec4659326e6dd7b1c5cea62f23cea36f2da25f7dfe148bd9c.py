code = """import json
import sys

# Try to load the data from the variables
funding_data = var_functions.query_db:2
civic_docs = var_functions.query_db:8

print('Types:', type(funding_data), type(civic_docs))
print('Funding is string?', isinstance(funding_data, str))
print('Civic is string?', isinstance(civic_docs, str))
print('Funding starts with / ?', isinstance(funding_data, str) and funding_data.startswith('/'))
print('Civic starts with / ?', isinstance(civic_docs, str) and civic_docs.startswith('/'))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
