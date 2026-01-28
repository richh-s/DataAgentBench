code = """import json
import re

# Load the data from the stored variables
# Check if we have file paths or direct data
mongo_key = 'var_functions.query_db:10'
funding_key = 'var_functions.query_db:5'

# Load MongoDB data (civic documents)
mongo_data = locals().get(mongo_key)
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_data if mongo_data else []

# Load funding data
funding_data = locals().get(funding_key)
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data if funding_data else []

print(f"Loaded {len(mongo_docs)} civic documents")
print(f"Loaded {len(funding_records)} funding records")

# Display sample of funding data
if funding_records:
    print(f"\nSample funding record: {funding_records[0]}")
    # Count how many have amount > 50000
    high_funding = [f for f in funding_records if int(f.get('Amount', 0)) > 50000]
    print(f"Records with funding > $50,000: {len(high_funding)}")

# Display sample of mongo doc
if mongo_docs:
    print(f"\nSample mongo doc keys: {list(mongo_docs[0].keys())}")
    print(f"Sample text snippet:\n{mongo_docs[0].get('text', '')[:500]}...")

print("Data loaded successfully")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
