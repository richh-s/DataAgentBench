code = """import json

# Read the file paths from the stored results
funding_path = var_functions.query_db_6
mongo_path = var_functions.query_db_2

print('Funding path:', funding_path)
print('Mongo path:', mongo_path)

# Load the data
with open(funding_path) as f:
    funding = json.load(f)

with open(mongo_path) as f:
    mongo = json.load(f)

print('Funding records:', len(funding))
print('Mongo docs:', len(mongo))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
