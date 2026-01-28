code = """import json
import re
import pandas as pd

# Get file paths from storage
mongo_docs_file = locals()['var_functions.query_db:0']
funding_data_file = locals()['var_functions.query_db:2']

# Load MongoDB documents
with open(mongo_docs_file, 'r') as f:
    mongo_docs = json.load(f)

# Load funding data
with open(funding_data_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(mongo_docs)} documents and {len(funding_data)} funding records")

# Convert funding data to DataFrame
df_funding = pd.DataFrame(funding_data)
print(f"Funding data shape: {df_funding.shape}")
print(f"Funding columns: {df_funding.columns.tolist()}")
print(f"\nSample funding records:")
print(df_funding.head().to_string())"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
