code = """import json
import os

# Debug: List all variables available
print("Available variables:")
for key in locals().keys():
    if key.startswith('var_'):
        print(f"  {key}: {type(locals()[key])}")

# Access the stored results
funding_result = locals()['var_functions.query_db:2']
civic_result = locals()['var_functions.query_db:0']

print(f"\nFunding result type: {type(funding_result)}")
print(f"Funding result value: {str(funding_result)[:200]}...")

print(f"\nCivic result type: {type(civic_result)}")
print(f"Civic result value: {str(civic_result)[:200]}...")

# Check if these are file paths and load them
funding_data = []
civic_docs = []

# Load funding data
if isinstance(funding_result, str) and ('.json' in funding_result or '/tmp/' in funding_result):
    try:
        file_path = funding_result if funding_result.startswith('/') else f'/tmp/{funding_result}'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                funding_data = json.load(f)
                print(f"Loaded {len(funding_data)} funding records from file")
        else:
            print(f"File not found: {file_path}")
    except:
        print("Could not load funding data as file, trying as direct data")
        funding_data = funding_result
else:
    funding_data = funding_result

# Load civic documents
if isinstance(civic_result, str) and ('.json' in civic_result or '/tmp/' in civic_result):
    try:
        file_path = civic_result if civic_result.startswith('/') else f'/tmp/{civic_result}'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                civic_docs = json.load(f)
                print(f"Loaded {len(civic_docs)} civic documents from file")
        else:
            print(f"File not found: {file_path}")
    except:
        print("Could not load civic data as file, trying as direct data")
        civic_docs = civic_result
else:
    civic_docs = civic_result

# Ensure we have lists
if not isinstance(funding_data, list):
    print("Converting funding_data to list")
    funding_data = []

if not isinstance(civic_docs, list):
    print("Converting civic_docs to list")
    civic_docs = []

print(f"\nFinal counts: {len(funding_data)} funding records, {len(civic_docs)} civic documents")

__RESULT__ = json.dumps({"funding_count": len(funding_data), "civic_count": len(civic_docs)})"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
