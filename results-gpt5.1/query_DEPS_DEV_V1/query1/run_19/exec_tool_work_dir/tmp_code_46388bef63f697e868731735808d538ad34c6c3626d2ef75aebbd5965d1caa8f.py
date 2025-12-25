code = """import json, pandas as pd
from pathlib import Path

file_path = Path(var_call_GgQrM9b3Aqk0QLhFEnYu4Z2h)
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
idx = df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = df.loc[idx, ['System','Name','Version']].reset_index(drop=True)
result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_uzzi04eQU6KQ9xvQeXimAnma': ['project_info', 'project_packageversion'], 'var_call_GgQrM9b3Aqk0QLhFEnYu4Z2h': 'file_storage/call_GgQrM9b3Aqk0QLhFEnYu4Z2h.json'}

exec(code, env_args)
