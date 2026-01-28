code = """import json
import pandas as pd
import re

civic_docs_data = locals()['var_functions.query_db:0']
funding_data = locals()['var_functions.query_db:2']

# Check types
print('Checking data types...')

# Process civic_docs_data
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)
        
# Process funding_data  
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert to DataFrames for easier analysis
df_civic = pd.DataFrame(civic_docs_data)
df_funding = pd.DataFrame(funding_data)

print('Documents DataFrame shape:', df_civic.shape)
print('Funding DataFrame shape:', df_funding.shape)

# Show column names
print('Documents columns:', df_civic.columns.tolist())
print('Funding columns:', df_funding.columns.tolist())

# Show first few rows of each
print('First document:')
print(df_civic.head(1).to_dict('records'))
print('First funding record:')
print(df_funding.head(1).to_dict('records'))

result = {
    'civic_docs_shape': df_civic.shape,
    'funding_shape': df_funding.shape,
    'civic_docs_columns': df_civic.columns.tolist(),
    'funding_columns': df_funding.columns.tolist()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
