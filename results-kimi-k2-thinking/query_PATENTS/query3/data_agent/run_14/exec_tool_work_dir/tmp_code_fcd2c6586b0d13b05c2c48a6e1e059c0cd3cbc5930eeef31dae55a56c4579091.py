code = """import json
import re

# Read the full dataset
file_path = 'var_functions.query_db:2'
with open(file_path, 'r') as f:
    records = json.load(f)

print('Total records:', len(records))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
