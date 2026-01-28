code = """import json

# Load funding data
funding_path = var_functions.query_db_6
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Funding records loaded:', len(funding_data))

# Load mongo data  
mongo_path = var_functions.query_db_2
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

print('Mongo documents loaded:', len(mongo_docs))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
