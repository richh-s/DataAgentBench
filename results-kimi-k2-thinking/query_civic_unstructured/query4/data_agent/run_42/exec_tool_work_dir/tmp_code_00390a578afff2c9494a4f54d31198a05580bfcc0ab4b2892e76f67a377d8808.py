code = """import json
import re

# Read the MongoDB results
mongo_file_path = var_functions.query_db:14
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

# Read the funding results  
funding_file_path = var_functions.query_db:4
with open(funding_file_path, 'r') as f:
    funding_records = json.load(f)

print(f"MongoDB documents: {len(mongo_docs)}")
print(f"Funding records: {len(funding_records)}")
print("\nSample funding records:")
for i, rec in enumerate(funding_records[:5]):
    print(f"  {i+1}. {rec['Project_Name']}: ${rec['Amount']}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
