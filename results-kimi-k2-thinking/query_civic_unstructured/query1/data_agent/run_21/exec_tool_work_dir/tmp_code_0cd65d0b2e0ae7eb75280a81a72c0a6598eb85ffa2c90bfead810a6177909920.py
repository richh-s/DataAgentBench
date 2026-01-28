code = """import json

# Try to access var_functions.query_db:2
# Since tool results are stored under this key, let's inspect it
funding_data = locals().get('var_functions.query_db:2', [])  # fallback empty if not present

# If it's a string (file path), open it
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Load as DataFrame for easier handling
import pandas as pd
funding_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Filter Amount > 50000
filtered_funding = funding_df[funding_df['Amount'] > 50000]

# Show count
result = {'funding_records_over_50000': len(filtered_funding)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
