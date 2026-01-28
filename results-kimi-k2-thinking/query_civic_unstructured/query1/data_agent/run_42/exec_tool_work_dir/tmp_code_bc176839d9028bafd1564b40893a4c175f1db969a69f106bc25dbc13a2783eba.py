code = """import json

# Get funding data (this was a successful query)
file_path_funding = var_functions.query_db_6
with open(file_path_funding, 'r') as f:
    funding_data = json.load(f)

print('Funding records > $50k:', len(funding_data))

# Debug mongo data access
try:
    file_path_mongo = var_functions.query_db_2
    with open(file_path_mongo, 'r') as f:
        mongo_data = json.load(f)
    print('Mongo documents:', len(mongo_data))
except Exception as e:
    print('Error accessing mongo data:', e)

# Sample of project names from funding
print('\nSample project names from funding:')
for f in funding_data[:10]:
    print(f" - {f['Project_Name']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
