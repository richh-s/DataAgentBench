code = """import json
import re

# Load the funding data
with open('query_results.json', 'r') as f:
    funding_data = json.load(f)

# Load the MongoDB civic documents data
with open('query_results.json', 'r') as f:
    civic_docs_data = json.load(f)

print(f"Funding records: {len(funding_data)}")
print(f"Civic documents: {len(civic_docs_data)}")
print("\nSample funding data:", funding_data[:3])
print("\nSample civic docs:", civic_docs_data[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
