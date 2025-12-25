code = """import json
import pandas as pd

# Load full result from file path
file_path = var_call_lGWb5Y6RVeDejd5TUyneAK5f
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Compute description length
df['desc_len'] = df['description'].astype(str).str.len()

# Find article with max description length
max_row = df.loc[df['desc_len'].idxmax()]
result = max_row['title']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lGWb5Y6RVeDejd5TUyneAK5f': 'file_storage/call_lGWb5Y6RVeDejd5TUyneAK5f.json'}

exec(code, env_args)
