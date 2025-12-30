code = """import json, pandas as pd
import os

# Load full citations result from file
path = var_call_hyxWmVTlPpguK2u0RkSm9S1Y
with open(path, 'r') as f:
    data = json.load(f)

# Convert citation_count to int and compute average
df = pd.DataFrame(data)
df['citation_count'] = df['citation_count'].astype(int)
avg = float(df['citation_count'].mean())

result = json.dumps(avg)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_hyxWmVTlPpguK2u0RkSm9S1Y': 'file_storage/call_hyxWmVTlPpguK2u0RkSm9S1Y.json'}

exec(code, env_args)
