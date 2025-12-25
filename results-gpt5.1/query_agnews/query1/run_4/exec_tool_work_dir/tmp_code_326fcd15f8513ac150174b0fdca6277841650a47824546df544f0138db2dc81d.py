code = """import json
import pandas as pd

# Load full result from file
file_path = var_call_hfw17ZmoQPWxNf5bwJAPlG7j
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Compute description length
df['desc_len'] = df['description'].astype(str).str.len()

# Find row with max description length
max_row = df.loc[df['desc_len'].idxmax()]

result = max_row['title']

import json as js
res_json = js.dumps(result)

print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_hfw17ZmoQPWxNf5bwJAPlG7j': 'file_storage/call_hfw17ZmoQPWxNf5bwJAPlG7j.json'}

exec(code, env_args)
