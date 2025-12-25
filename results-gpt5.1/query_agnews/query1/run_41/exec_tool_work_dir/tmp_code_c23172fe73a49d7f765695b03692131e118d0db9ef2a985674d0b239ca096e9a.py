code = """import json
import pandas as pd

# Load full results from file path
file_path = var_call_KcZU8n9St4GvG05g7bGtiRwW
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Drop rows with missing descriptions just in case
df = df.dropna(subset=['description'])

# Compute length of descriptions
df['desc_len'] = df['description'].astype(str).str.len()

# Find the row with max description length
max_row = df.loc[df['desc_len'].idxmax()]

result = json.dumps({"title": max_row['title'], "max_description_length": int(max_row['desc_len'])})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_KcZU8n9St4GvG05g7bGtiRwW': 'file_storage/call_KcZU8n9St4GvG05g7bGtiRwW.json'}

exec(code, env_args)
