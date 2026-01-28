code = """import json
import re
import pandas as pd

# Load MongoDB documents
mongo_docs_path = locals()['var_functions.query_db:0']
with open(mongo_docs_path, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data
funding_data_path = locals()['var_functions.query_db:2']
with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(mongo_docs)} documents and {len(funding_data)} funding records")

# Convert funding data to DataFrame for easier processing
df_funding = pd.DataFrame(funding_data)
print(f"Funding data shape: {df_funding.shape}")
print(f"Funding columns: {df_funding.columns.tolist()}")

# Display first few funding records
print("\nSample funding records:")
print(df_funding.head())"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
