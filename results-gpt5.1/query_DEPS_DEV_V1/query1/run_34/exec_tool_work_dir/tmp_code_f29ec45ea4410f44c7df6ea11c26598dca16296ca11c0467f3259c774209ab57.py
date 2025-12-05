code = """import pandas as pd, json
import os

path = var_call_UQC9GPlj5T53scmjbbAAC5hL
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
idx = df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = df.loc[idx, ['System','Name','Version']]
result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_LXWPZszMZItiAcI1by9sxnXM': ['project_info', 'project_packageversion'], 'var_call_UQC9GPlj5T53scmjbbAAC5hL': 'file_storage/call_UQC9GPlj5T53scmjbbAAC5hL.json'}

exec(code, env_args)
