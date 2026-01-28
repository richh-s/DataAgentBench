code = """import json
import re
from collections import defaultdict

# Get data from storage
mongo_result = var_functions.query_db:4
funding_result = var_functions.query_db:6

# Check if data is loaded
print(f"MongoDB result type: {type(mongo_result)}")
print(f"Funding result type: {type(funding_result)}")

# Convert to list if it's a string (file path)
if isinstance(mongo_result, str) and '.json' in mongo_result:
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_result

if isinstance(funding_result, str) and '.json' in funding_result:
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

print(f"Loaded {len(mongo_docs)} civic documents")
print(f"Loaded {len(funding_records)} funding records")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
