code = """import json, pandas as pd
import os

file_path = var_call_EBghXUfxuevY0EQecjRpUC10
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
idx = df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = df.loc[idx, ['System','Name','Version']]
result = latest.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_ZAXQnJ11ek3Dr9ZVmxkYYfpk': ['project_info', 'project_packageversion'], 'var_call_EBghXUfxuevY0EQecjRpUC10': 'file_storage/call_EBghXUfxuevY0EQecjRpUC10.json'}

exec(code, env_args)
