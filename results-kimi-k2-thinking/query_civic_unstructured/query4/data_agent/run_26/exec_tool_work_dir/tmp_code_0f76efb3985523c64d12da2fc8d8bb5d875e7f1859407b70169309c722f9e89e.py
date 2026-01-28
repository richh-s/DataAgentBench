code = """# Let's check what variables are available in the environment
import json
import os

# Check available variables
print("Available variables:")
for var_name in list(locals().keys()):
    if var_name.startswith("var_"):
        print(var_name)

# Try to access the civic docs data
try:
    civic_docs = var_functions.query_db_0
    print(f"\ncivic_docs type: {type(civic_docs)}")
    if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
        with open(civic_docs, 'r') as f:
            civic_docs_data = json.load(f)
        print(f"Loaded civic_docs from file: {len(civic_docs_data)} records")
    else:
        civic_docs_data = civic_docs
        print(f"civic_docs is already loaded: {len(civic_docs_data)} records")
except Exception as e:
    print(f"Error accessing civic_docs: {e}")

# Try to access the funding data
try:
    funding = var_functions.query_db_5
    print(f"\nfunding type: {type(funding)}")
    if isinstance(funding, str) and funding.endswith('.json'):
        with open(funding, 'r') as f:
            funding_data = json.load(f)
        print(f"Loaded funding from file: {len(funding_data)} records")
    else:
        funding_data = funding
        print(f"funding is already loaded: {len(funding_data)} records")
except Exception as e:
    print(f"Error accessing funding: {e}")

print("\n__RESULT__:")
print(json.dumps({
    "status": "loaded",
    "civic_docs_count": len(civic_docs_data) if 'civic_docs_data' in locals() else 0,
    "funding_count": len(funding_data) if 'funding_data' in locals() else 0
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
