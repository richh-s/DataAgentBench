code = """# Load data from storage variables
civic_docs_path = var_functions.query_db:60
funding_path = var_functions.query_db:48

import json

civic_docs = json.load(open(civic_docs_path))
funding = json.load(open(funding_path))

print('Civic docs loaded:', len(civic_docs))
print('Funding records loaded:', len(funding))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
