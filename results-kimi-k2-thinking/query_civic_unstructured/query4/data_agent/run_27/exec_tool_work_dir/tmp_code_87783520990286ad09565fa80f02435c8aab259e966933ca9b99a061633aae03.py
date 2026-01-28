code = """import json
import re
import os

# Access the variables from storage
mongo_key = 'var_functions.query_db:5'
funding_key = 'var_functions.query_db:20'

# Check what's in these variables
print("=== Checking data types ===")
mongo_path = globals()[mongo_key]
funding_path = globals()[funding_key]

print("Mongo data type:", type(mongo_path))
print("Mongo data preview:", str(mongo_path)[:300])
print("Funding data type:", type(funding_path))
print("Funding data preview:", str(funding_path)[:300])

# Load the data
print("\n=== Loading data ===")

# Load MongoDB civic documents
if isinstance(mongo_path, str) and '.json' in mongo_path:
    with open(mongo_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = mongo_path

# Load Funding data
if isinstance(funding_path, str) and '.json' in funding_path:
    with open(funding_path, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_path

print("Civic docs loaded:", len(civic_docs))
print("Funding records loaded:", len(funding_records))
print("Civic docs keys:", list(civic_docs[0].keys()) if civic_docs else "Empty")
print("Funding record keys:", list(funding_records[0].keys()) if funding_records else "Empty")

# Display sample document text
print("\n=== Sample Document Text ===")
sample_doc = civic_docs[0]
print("Filename:", sample_doc.get('filename'))
print("Text preview:", sample_doc.get('text', '')[:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
