code = """import json
import re
from collections import defaultdict

# Load funding data
funding_file = 'var_functions.query_db_2'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Total funding records loaded:', len(funding_data))

# Load civic_docs
civic_file = 'var_functions.query_db_6'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Total civic documents loaded:', len(civic_docs))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
