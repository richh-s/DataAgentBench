code = """import json, re, pandas as pd

# load big results
pkg_path = var_call_P0h8HiLoqELOduJhGIv31jIb
ppv_path = var_call_BXWtcuaMpzV1276KydjYv0kN
pi_path = var_call_Wux4DxduFwCCYCOfEu4Xr6Na

with open(pkg_path, 'r', encoding='utf-8') as f:
    pkg = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppv = json.load(f)
with open(pi_path, 'r', encoding='utf-8') as f:
    pi = json.load(f)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
proj_names = set(merged['ProjectName'].dropna().unique().tolist())

# parse ProjectName and fork count from Project_Information text
rx = re.compile(r"project\s+([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+).+?(?:has|and has|with)\s+(?:\d+[\s\w,]*,\s*)?(?:\d+[\s\w,]*stars,\s*and\s*)?([0-9,]+)\s+forks", re.IGNORECASE)
# More robust: separately extract name, then forks
rx_name = re.compile(r"project\s+(?:named\s+)?([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)", re.IGNORECASE)
rx_forks = re.compile(r"([0-9,]+)\s+forks", re.IGNORECASE)

rows = []
for rec in pi:
    txt = rec.get('Project_Information') or ''
    mname = rx_name.search(txt)
    if not mname:
        continue
    pname = mname.group(1)
    if pname not in proj_names:
        continue
    mf = rx_forks.search(txt)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',',''))
    rows.append({'ProjectName': pname, 'Forks': forks})

proj_df = pd.DataFrame(rows).drop_duplicates()
# for safety, take max forks per project
proj_df = proj_df.groupby('ProjectName', as_index=False)['Forks'].max()

# Top 5 by forks
top5 = proj_df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_P0h8HiLoqELOduJhGIv31jIb': 'file_storage/call_P0h8HiLoqELOduJhGIv31jIb.json', 'var_call_BXWtcuaMpzV1276KydjYv0kN': 'file_storage/call_BXWtcuaMpzV1276KydjYv0kN.json', 'var_call_Wux4DxduFwCCYCOfEu4Xr6Na': 'file_storage/call_Wux4DxduFwCCYCOfEu4Xr6Na.json'}

exec(code, env_args)
