code = """import json

# Load funding data
funding_file = var_functions.query_db_14
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
civic_file = var_functions.query_db_15
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_data))
print('First funding record:', funding_data[0])
print('First civic doc keys:', list(civic_data[0].keys()))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': []}

exec(code, env_args)
