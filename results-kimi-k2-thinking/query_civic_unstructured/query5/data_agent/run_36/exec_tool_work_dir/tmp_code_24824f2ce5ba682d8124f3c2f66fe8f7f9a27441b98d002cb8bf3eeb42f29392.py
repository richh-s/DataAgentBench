code = """import json
import os

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print("First 5 records:")
print(json.dumps(funding_data[:5], indent=2))

# Load civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

print(f"\nNumber of civic doc records: {len(civic_docs_data)}")
print("First civic doc:")
print(json.dumps(civic_docs_data[0], indent=2)[:1000] + "...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
