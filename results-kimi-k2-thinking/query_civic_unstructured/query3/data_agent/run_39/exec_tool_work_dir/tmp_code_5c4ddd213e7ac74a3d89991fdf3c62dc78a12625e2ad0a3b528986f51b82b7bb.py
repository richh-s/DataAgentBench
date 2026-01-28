code = """import json
import re

# Access the stored results using the provided key names
civic_docs_path = locals()['var_functions.query_db:0']
funding_data_path = locals()['var_functions.query_db:2']

print("Civic docs file path:", civic_docs_path)
print("Funding data file path:", funding_data_path)

# Load the data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

print("\nNumber of civic documents:", len(civic_docs))
print("Number of funding records:", len(funding_data))

# Show sample data
print("\nCivic doc keys:", list(civic_docs[0].keys()))
print("Sample civic doc text (first 200 chars):", civic_docs[0]['text'][:200])
print("\nSample funding record:", funding_data[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
