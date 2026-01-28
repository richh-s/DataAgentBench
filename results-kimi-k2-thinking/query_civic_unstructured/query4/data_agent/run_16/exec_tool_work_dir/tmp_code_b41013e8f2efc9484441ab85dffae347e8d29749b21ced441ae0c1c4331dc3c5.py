code = """import json
import re

# Load funding data
funding_file = '/tmp/tmptf8vwxq6.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Number of funding records:', len(funding_data))
print('Sample funding records:')
for i, record in enumerate(funding_data[:5]):
    print(f"  {i+1}. {record}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
