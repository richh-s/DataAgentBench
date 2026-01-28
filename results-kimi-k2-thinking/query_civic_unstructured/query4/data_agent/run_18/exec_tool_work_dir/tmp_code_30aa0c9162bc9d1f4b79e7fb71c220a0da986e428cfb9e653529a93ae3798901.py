code = """import json
import re
from datetime import datetime

# Load civic documents (stored in file)
civic_docs_file = var_functions.query_db:11
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents loaded: {len(civic_docs)}")

# Load funding data
funding_file = var_functions.query_db:12
funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Total funding records loaded: {len(funding_data)}")

print('__RESULT__:')
print(json.dumps({'civic_docs_count': len(civic_docs), 'funding_count': len(funding_data)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
