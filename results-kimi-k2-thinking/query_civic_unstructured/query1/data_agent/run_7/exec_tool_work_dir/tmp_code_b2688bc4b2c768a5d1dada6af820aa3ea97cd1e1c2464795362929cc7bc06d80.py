code = """import json
import re

# Load the MongoDB data
mongo_file = var_functions.query_db:2
if isinstance(mongo_file, str):
    with open(mongo_file, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = var_functions.query_db:2

# Load the funding data
funding_file = var_functions.query_db:5
if isinstance(funding_file, str):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:5

print(f"MongoDB docs count: {len(mongo_docs)}")
print(f"Funding records count: {len(funding_data)}")

# Show sample of data structure
print("\nSample MongoDB doc keys:", list(mongo_docs[0].keys()) if mongo_docs else "No docs")
print("Sample funding record:", funding_data[0] if funding_data else "No data")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
