code = """import json
import pandas as pd
import re

# Load funding data from the file path
funding_file = var_functions.query_db:9
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents from the file path
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print(f"\nFunding DataFrame shape: {funding_df.shape}")
print(funding_df.head(3).to_string())

# Check for disaster-related projects in funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
disaster_funding = funding_df[funding_df['Project_Name'].str.contains('|'.join(disaster_keywords), case=False, na=False)]
print(f"\nDisaster-related funding records: {len(disaster_funding)}")
print(disaster_funding.head().to_string())"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
