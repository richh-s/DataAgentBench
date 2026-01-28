code = """import json

# Get the results from storage keys
mongo_docs = var_functions.query_db:4
funding_records = var_functions.query_db:6

# Check types
print(f"MongoDB type: {type(mongo_docs)}")
print(f"Funding type: {type(funding_records)}")

# Count records
if isinstance(mongo_docs, list):
    print(f"MongoDB docs count: {len(mongo_docs)}")
else:
    print(f"MongoDB docs: {str(mongo_docs)[:100]}...")
    
if isinstance(funding_records, list):
    print(f"Funding records count: {len(funding_records)}")
else:
    print(f"Funding records: {str(funding_records)[:100]}...")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
