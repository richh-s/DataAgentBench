code = """import json, pandas as pd, re

# load large json files
pkg_path = var_call_IUrDFHuO1a8K3JIVdX8YuuV0
ppv_path = var_call_FvpxTPB9pEfLiDdGEELxBAle

with open(pkg_path, 'r', encoding='utf-8') as f:
    pkg = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

joined = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = joined['ProjectName'].dropna().drop_duplicates().tolist()

# output list of project names for next query
print('__RESULT__:')
print(json.dumps({'projects': projects, 'n_projects': len(projects)}))"""

env_args = {'var_call_IUrDFHuO1a8K3JIVdX8YuuV0': 'file_storage/call_IUrDFHuO1a8K3JIVdX8YuuV0.json', 'var_call_FvpxTPB9pEfLiDdGEELxBAle': 'file_storage/call_FvpxTPB9pEfLiDdGEELxBAle.json'}

exec(code, env_args)
