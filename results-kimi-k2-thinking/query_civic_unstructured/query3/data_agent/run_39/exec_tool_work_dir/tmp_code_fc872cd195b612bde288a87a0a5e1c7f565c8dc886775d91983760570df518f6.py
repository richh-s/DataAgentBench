code = """import json
import re

# Load the data from storage
with open(var_functions.query_db:0, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(var_functions.query_db:2, 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

# Show a sample of the data
print("\nSample civic doc:")
print(json.dumps(civic_docs[0], indent=2)[:1000])

print("\nSample funding records:")
for i, rec in enumerate(funding_data[:5]):
    print(f"{i}: {rec}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
