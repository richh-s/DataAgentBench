code = """import json
import os

# Access storage variables via locals()
storage = locals()
funding_file = storage['var_functions.query_db:2']
civic_docs_file = storage['var_functions.query_db:8']

# Debug: print file paths
print('Funding file path:', funding_file)
print('Civic docs file path:', civic_docs_file)
print('Files exist:', os.path.exists(funding_file), os.path.exists(civic_docs_file))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
