code = """import json
import re

# Load the data files
funding_file = var_functions.query_db_14
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = var_functions.query_db_24
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records loaded:', len(funding_data))
print('Civic documents loaded:', len(civic_data))

# Create a list of all project names from funding data
project_names = [item['Project_Name'] for item in funding_data]
print('Sample project names:', project_names[:10])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
