code = """import json, pandas as pd

pkg_file = var_call_MEaQ8Er8fplu6LkGdZVD9PA7
ppv_file = var_call_z5bj9hrb9L2sl10uM2L3bbd0

with open(pkg_file) as f:
    pkg = json.load(f)
with open(ppv_file) as f:
    ppv = json.load(f)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

latest = pkg_df.sort_values('Version').groupby(['System','Name']).tail(1)
latest_npm = latest[latest['System']=='NPM'][['Name','Version']]

merged = latest_npm.merge(ppv_df, on=['Name','Version'], how='inner')

# extract star count from Project_Information using a regex like "Stars: 12345" or "⭐ 12345" if present

proj_names = merged['ProjectName'].unique().tolist()

result = json.dumps({'proj_names_sample': proj_names[:10], 'count': len(proj_names)})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_MEaQ8Er8fplu6LkGdZVD9PA7': 'file_storage/call_MEaQ8Er8fplu6LkGdZVD9PA7.json', 'var_call_z5bj9hrb9L2sl10uM2L3bbd0': 'file_storage/call_z5bj9hrb9L2sl10uM2L3bbd0.json'}

exec(code, env_args)
