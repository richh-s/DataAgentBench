code = """import json
import re

# Load the MongoDB data from the correct storage key
mongo_result_key = 'var_functions.query_db:2'
funding_result_key = 'var_functions.query_db:5'

mongo_file_path = locals().get(mongo_result_key)
funding_file_path = locals().get(funding_result_key)

# Load MongoDB data
if isinstance(mongo_file_path, str) and mongo_file_path.endswith('.json'):
    with open(mongo_file_path, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = locals().get(mongo_result_key, [])

# Load funding data  
if isinstance(funding_file_path, str) and funding_file_path.endswith('.json'):
    with open(funding_file_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals().get(funding_result_key, [])

print(f"MongoDB docs count: {len(mongo_docs)}")
print(f"Funding records count: {len(funding_data)}")

# Show sample data
if mongo_docs:
    print(f"\nSample MongoDB doc keys: {list(mongo_docs[0].keys())}")
    print(f"Sample MongoDB text snippet: {mongo_docs[0].get('text', '')[:200]}...")
    
if funding_data:
    print(f"\nSample funding record: {funding_data[0]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
