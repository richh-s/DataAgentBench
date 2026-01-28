code = """import json
import re

# Load the funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Load the civic docs data
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs)}")
print("__RESULT__:")
print(json.dumps({"funding_count": len(funding_data), "docs_count": len(civic_docs)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
