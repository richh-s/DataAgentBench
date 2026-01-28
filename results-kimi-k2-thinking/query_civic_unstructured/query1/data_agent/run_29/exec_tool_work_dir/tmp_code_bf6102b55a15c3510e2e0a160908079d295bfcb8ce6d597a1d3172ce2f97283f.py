code = """import json
import pandas as pd
from pathlib import Path

# Read funding data
funding_file = "/tmp/tmp4bjh5yrr.json"
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create DataFrame for funding
df_funding = pd.DataFrame(funding_data)
# Filter for Amount > 50000
df_funding_filtered = df_funding[df_funding['Amount'].astype(int) > 50000]

# Read civic docs - need to check the file path format
# From previous message, it seems the file path might be in a variable
# Let me check what's in the storage

print('__RESULT__:')
print(json.dumps({
    'funding_count': len(df_funding_filtered),
    'sample_funding': df_funding_filtered.head(5).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
