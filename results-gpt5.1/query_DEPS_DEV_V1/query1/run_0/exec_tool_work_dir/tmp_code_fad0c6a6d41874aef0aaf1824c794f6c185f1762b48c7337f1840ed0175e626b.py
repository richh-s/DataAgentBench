code = """import json, pandas as pd
path = var_call_esQgIkJbYcAetGMFXKGRQ5oe
with open(path) as f:
    data = json.load(f)

df = pd.DataFrame(data)
# parse VersionInfo JSON and keep only releases
vi = df['VersionInfo'].apply(json.loads)
vi = pd.json_normalize(vi)
# add IsRelease and Ordinal
df['IsRelease'] = vi['IsRelease']
df['Ordinal'] = vi['Ordinal']
# filter to releases only
releases = df[df['IsRelease']]
# for each Name, keep row with max Ordinal
idx = releases.groupby('Name')['Ordinal'].idxmax()
latest = releases.loc[idx, ['System','Name','Version']]
result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_esQgIkJbYcAetGMFXKGRQ5oe': 'file_storage/call_esQgIkJbYcAetGMFXKGRQ5oe.json', 'var_call_wOSiEy2orHHEz4hM5q3hw7lH': ['project_info', 'project_packageversion'], 'var_call_whJh4DlklF8Dbphwe2meg2nz': 'file_storage/call_whJh4DlklF8Dbphwe2meg2nz.json', 'var_call_ZypVxjjyEN8cKNMgfjQzpLco': 'file_storage/call_ZypVxjjyEN8cKNMgfjQzpLco.json'}

exec(code, env_args)
