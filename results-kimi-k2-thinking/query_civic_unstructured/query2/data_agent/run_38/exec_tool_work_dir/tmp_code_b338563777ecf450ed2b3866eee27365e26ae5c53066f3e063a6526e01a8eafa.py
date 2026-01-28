code = """import json
import re
import pandas as pd

# Get the stored results using locals()
civic_docs_result = locals()['var_functions.query_db:2']
funding_result = locals()['var_functions.query_db:5']

# Read the civic documents from file
with open(civic_docs_result, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Read the funding data from file  
with open(funding_result, 'r') as f:
    funding_data = json.load(f)

print(f"Total funding records: {len(funding_data)}")

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print(f"Funding data loaded: {funding_df.shape}")
print(funding_df.head())

print("__RESULT__:")
print(json.dumps({"civic_docs_count": len(civic_docs), "funding_count": len(funding_data), "funding_columns": list(funding_df.columns)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
