code = """import json
import re
import pandas as pd

# Load the civic_docs data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = locals()['var_functions.query_db:1']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

# Let's examine the structure of civic_docs
print("\nFirst civic doc structure:")
print(json.dumps(civic_docs[0].keys(), indent=2))

print("\nSample text from first doc:")
print(civic_docs[0]['text'][:1000])

# Print first few funding records
print("\nFirst few funding records:")
for i, record in enumerate(funding_data[:5]):
    print(f"{i+1}. {record}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
