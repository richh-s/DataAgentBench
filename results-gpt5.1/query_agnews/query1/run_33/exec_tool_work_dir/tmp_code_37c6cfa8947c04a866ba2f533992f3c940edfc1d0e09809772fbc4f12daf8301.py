code = """import json, pandas as pd
from pathlib import Path

# Load full result from file
path = Path(var_call_Dtq7HNkAubLHJlqh3xAucZPJ)
with path.open() as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Compute description length
df['desc_len'] = df['description'].astype(str).str.len()

# Find row with max description length
idx = df['desc_len'].idxmax()
max_title = df.loc[idx, 'title']

result = json.dumps(max_title)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Dtq7HNkAubLHJlqh3xAucZPJ': 'file_storage/call_Dtq7HNkAubLHJlqh3xAucZPJ.json'}

exec(code, env_args)
