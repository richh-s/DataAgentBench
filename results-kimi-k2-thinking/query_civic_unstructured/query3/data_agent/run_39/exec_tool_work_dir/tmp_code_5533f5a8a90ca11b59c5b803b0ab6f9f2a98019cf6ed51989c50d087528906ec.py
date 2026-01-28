code = """import json
import re

# Access the stored results using the provided variable names
civic_docs_file = locals()['var_functions.query_db:0']
funding_data_file = locals()['var_functions.query_db:2']

print("Civic docs file:", civic_docs_file)
print("Funding data file:", funding_data_file)

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_data_file, 'r') as f:
    funding_data = json.load(f)

print("\nNumber of civic documents:", len(civic_docs))
print("Number of funding records:", len(funding_data))

# Show sample data
print("\nCivic doc keys:", list(civic_docs[0].keys()))
print("Sample funding record:", funding_data[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
