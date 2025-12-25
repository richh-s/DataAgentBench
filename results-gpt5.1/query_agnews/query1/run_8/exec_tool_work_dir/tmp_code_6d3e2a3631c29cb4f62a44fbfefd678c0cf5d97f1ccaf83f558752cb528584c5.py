code = """import json
import pandas as pd

# Load full result from file
with open(var_call_Zs7MXJdxYKWHZHe78fRxkgqy, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure description is string and compute length
df['description_str'] = df['description'].astype(str)
df['desc_len'] = df['description_str'].str.len()

# Find row with maximum description length
max_row = df.loc[df['desc_len'].idxmax()]

result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Zs7MXJdxYKWHZHe78fRxkgqy': 'file_storage/call_Zs7MXJdxYKWHZHe78fRxkgqy.json'}

exec(code, env_args)
