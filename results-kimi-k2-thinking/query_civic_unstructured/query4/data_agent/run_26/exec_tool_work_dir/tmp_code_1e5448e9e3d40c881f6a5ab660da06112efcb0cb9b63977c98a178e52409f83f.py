code = """import json
import os

# Check available variables
available_vars = [var for var in dir() if var.startswith('var_')]
print("Available variables:", available_vars)

# Try to access civic_docs
try:
    civic_docs = var_functions_query_db_0
    print(f"civic_docs type: {type(civic_docs)}")
    if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
        with open(civic_docs, 'r') as f:
            civic_docs_data = json.load(f)
        print(f"Loaded civic_docs from file: {len(civic_docs_data)} records")
    else:
        civic_docs_data = civic_docs
        print(f"civic_docs is already loaded: {len(civic_docs_data)} records")
except Exception as e:
    print(f"Error accessing civic_docs: {e}")
    civic_docs_data = []

# Try to access funding
try:
    funding = var_functions_query_db_5
    print(f"funding type: {type(funding)}")
    if isinstance(funding, str) and funding.endswith('.json'):
        with open(funding, 'r') as f:
            funding_data = json.load(f)
        print(f"Loaded funding from file: {len(funding_data)} records")
    else:
        funding_data = funding
        print(f"funding is already loaded: {len(funding_data)} records")
except Exception as e:
    print(f"Error accessing funding: {e}")
    funding_data = []

# Debug: show first few records
print("\n--- First civic doc ---")
if civic_docs_data:
    print(json.dumps(civic_docs_data[0])[:500])
    
print("\n--- First funding record ---")
if funding_data:
    print(json.dumps(funding_data[0]))

print("\n__RESULT__:")
print(json.dumps({
    "civic_docs_count": len(civic_docs_data),
    "funding_count": len(funding_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
