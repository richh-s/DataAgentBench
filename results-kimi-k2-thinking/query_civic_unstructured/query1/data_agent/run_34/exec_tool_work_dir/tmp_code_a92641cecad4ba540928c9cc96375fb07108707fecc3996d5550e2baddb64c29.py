code = """import json
import pandas as pd
import re
import os

# Read the file paths from the storage keys
funding_file = var_functions.query_db:5
civic_file = var_functions.query_db:12

# Load funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'funding_records': len(funding_data),
    'civic_documents': len(civic_data),
    'sample_project': funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
