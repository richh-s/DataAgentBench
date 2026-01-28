code = """import json
import os

# Get the file paths from stored variables
mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

print("Mongo file:", mongo_file)
print("Funding file:", funding_file)

# Load data
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_recs = json.load(f)

print("MongoDB docs:", len(mongo_docs))
print("Funding records:", len(funding_recs))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
