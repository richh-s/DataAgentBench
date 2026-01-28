code = """import json
import pandas as pd
import re

# Load the full results from the MongoDB documents
with open('var_functions.query_db:0', 'r') as f:
    civic_docs_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} documents from civic_docs_database")
print("Sample document keys:", list(civic_docs_data[0].keys()))

# Load the full results from the Funding table
with open('var_functions.query_db:2', 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(funding_data)} funding records from funding_database")
print("Sample funding record:", funding_data[0])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
