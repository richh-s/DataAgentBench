code = """import json, pandas as pd
import os

path = var_call_4gV01X4T1kO0s1Eot49lGyhD
with open(path, 'r') as f:
    npm_pkgs = json.load(f)

pkgs_df = pd.DataFrame(npm_pkgs)
vi = pkgs_df['VersionInfo'].apply(json.loads)
vi_df = pd.json_normalize(vi)
pkgs_df = pd.concat([pkgs_df.drop(columns=['VersionInfo']), vi_df], axis=1)

releases = pkgs_df[pkgs_df['IsRelease'] == True]
idx = releases.groupby('Name')['Ordinal'].idxmax()
latest = releases.loc[idx, ['System','Name','Version','Ordinal']]

result = latest.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4gV01X4T1kO0s1Eot49lGyhD': 'file_storage/call_4gV01X4T1kO0s1Eot49lGyhD.json', 'var_call_dok3dxMAkcsJR1MjJzyJPhSN': ['project_info', 'project_packageversion'], 'var_call_rMAa4eGug5bj0B0mAOwjzPA0': 'file_storage/call_rMAa4eGug5bj0B0mAOwjzPA0.json'}

exec(code, env_args)
