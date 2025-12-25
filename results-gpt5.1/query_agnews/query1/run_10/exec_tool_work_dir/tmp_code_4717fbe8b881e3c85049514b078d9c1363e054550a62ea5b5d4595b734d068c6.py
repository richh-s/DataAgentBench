code = """import json
import pandas as pd

# Load data from the JSON file path stored in var_call_yNGYjxt8YrNPVpZn8uTQPQWi
with open(var_call_yNGYjxt8YrNPVpZn8uTQPQWi, 'r') as f:
    articles = json.load(f)

# Create DataFrame
df = pd.DataFrame(articles)

# Ensure description is string and compute length
df['description'] = df['description'].astype(str)
df['desc_len'] = df['description'].str.len()

# Find row with maximum description length
max_row = df.loc[df['desc_len'].idxmax()]

result = json.dumps({"title": max_row['title'], "max_description_length": int(max_row['desc_len'])})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_yNGYjxt8YrNPVpZn8uTQPQWi': 'file_storage/call_yNGYjxt8YrNPVpZn8uTQPQWi.json'}

exec(code, env_args)
