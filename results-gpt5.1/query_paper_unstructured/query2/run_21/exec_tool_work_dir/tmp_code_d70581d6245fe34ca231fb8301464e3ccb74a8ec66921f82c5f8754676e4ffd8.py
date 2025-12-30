code = """import json, pandas as pd
import os

# Load full result from file
path = var_call_IXGdKBddNxSc7KREfhWQoFjR
with open(path, 'r') as f:
    data = json.load(f)

# Convert citation_count to numeric and compute average
df = pd.DataFrame(data)
df['citation_count'] = pd.to_numeric(df['citation_count'])
avg_citations = df['citation_count'].mean()

result = json.dumps(avg_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_IXGdKBddNxSc7KREfhWQoFjR': 'file_storage/call_IXGdKBddNxSc7KREfhWQoFjR.json'}

exec(code, env_args)
