code = """import json
import pandas as pd

# Load full result from file
path = var_call_QRI1VrTOViALsaRatbpmPIWn
with open(path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Compute length of descriptions
df['desc_len'] = df['description'].astype(str).str.len()

# Find row with max description length
max_row = df.loc[df['desc_len'].idxmax()]

result = json.dumps(max_row['title'])

print("__RESULT__:")
print(result)"""

env_args = {'var_call_QRI1VrTOViALsaRatbpmPIWn': 'file_storage/call_QRI1VrTOViALsaRatbpmPIWn.json'}

exec(code, env_args)
