code = """import json

# Read MongoDB results from file
mongo_path = var_functions.query_db:2
funding_path = var_functions.query_db:6

print("Reading MongoDB file from:", str(mongo_path)[:100])
print("Reading Funding file from:", str(funding_path)[:100])

# Load the data
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print("Mongo docs count:", len(mongo_docs))
print("Funding records count:", len(funding_records))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
