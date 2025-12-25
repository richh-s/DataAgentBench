code = """import json, pandas as pd
from pathlib import Path

file_path = Path(var_call_81KwFwNqlKOKOn9C6KRVZwE3)
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
idx = df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = df.loc[idx, ['System','Name','Version']]
result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yPpXlVfm6ScbUH2S2tJxhtOl': ['project_info', 'project_packageversion'], 'var_call_81KwFwNqlKOKOn9C6KRVZwE3': 'file_storage/call_81KwFwNqlKOKOn9C6KRVZwE3.json'}

exec(code, env_args)
