code = """import json, pandas as pd, os

path_latest = var_call_8vSmLIS9rGnkF249dKccWpnx
with open(path_latest, 'r') as f:
    latest = json.load(f)
latest_df = pd.DataFrame(latest)

path_ppv = var_call_rMAa4eGug5bj0B0mAOwjzPA0
with open(path_ppv, 'r') as f:
    ppv = json.load(f)
ppv_df = pd.DataFrame(ppv)

merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
merged = merged[['System','Name','Version','ProjectName']].drop_duplicates()

result = merged.to_json(orient='records')
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4gV01X4T1kO0s1Eot49lGyhD': 'file_storage/call_4gV01X4T1kO0s1Eot49lGyhD.json', 'var_call_dok3dxMAkcsJR1MjJzyJPhSN': ['project_info', 'project_packageversion'], 'var_call_rMAa4eGug5bj0B0mAOwjzPA0': 'file_storage/call_rMAa4eGug5bj0B0mAOwjzPA0.json', 'var_call_8vSmLIS9rGnkF249dKccWpnx': 'file_storage/call_8vSmLIS9rGnkF249dKccWpnx.json'}

exec(code, env_args)
