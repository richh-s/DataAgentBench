code = """import json, pandas as pd
import os

path = var_call_yjHuHL7V1r8J8XtV3HY1WvEV
with open(path) as f:
    data = json.load(f)

df = pd.DataFrame(data)
idx = df.groupby('Name')['UpstreamPublishedAt'].idxmax()
latest = df.loc[idx, ['System','Name','Version']]
latest_json = latest.to_json(orient='records')

print('__RESULT__:')
print(latest_json)"""

env_args = {'var_call_B9rXac9rbbvyCqKvbr6prM7O': ['project_info', 'project_packageversion'], 'var_call_yjHuHL7V1r8J8XtV3HY1WvEV': 'file_storage/call_yjHuHL7V1r8J8XtV3HY1WvEV.json'}

exec(code, env_args)
