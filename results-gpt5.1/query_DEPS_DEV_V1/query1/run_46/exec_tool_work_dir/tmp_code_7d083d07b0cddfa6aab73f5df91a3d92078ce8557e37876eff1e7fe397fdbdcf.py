code = """import json, pandas as pd
path = var_call_dPgVOSdxo3BEWb3C9qHFSwGZ
with open(path) as f:
    data = json.load(f)
df = pd.DataFrame(data)
# keep only latest version per (System, Name) using UpstreamPublishedAt if available; but we don't have it here, so just keep max Version lexicographically
# we only need keys, actual latest detection will require timestamps, but approximate here
latest = df.sort_values(['System','Name','Version']).groupby(['System','Name']).tail(1)
result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_dPgVOSdxo3BEWb3C9qHFSwGZ': 'file_storage/call_dPgVOSdxo3BEWb3C9qHFSwGZ.json', 'var_call_zcurF4o6Wv4G3zX2pC4DFbCU': ['project_info', 'project_packageversion'], 'var_call_MaFRQXk2ytbZgVdx1cnXHz1b': 'file_storage/call_MaFRQXk2ytbZgVdx1cnXHz1b.json'}

exec(code, env_args)
