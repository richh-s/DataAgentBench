code = """import pandas as pd
import json
import re

pck_path = var_call_9RxvN1ms11PAi3Z2GfMMtlMd
ppv_path = var_call_EcIJ2eetWqFLydiCAGYVIT2o
pinfo_path = var_call_3o5dX0GZKJoHEIx7XkqnSff8

# Load data
df_pck = pd.read_json(pck_path)
df_ppv = pd.read_json(ppv_path)
df_pinfo = pd.read_json(pinfo_path)

# Keep only GITHUB projects
df_ppv = df_ppv[df_ppv['ProjectType'].str.upper() == 'GITHUB']

# Merge on System, Name, Version
merged = pd.merge(df_pck, df_ppv, on=['System', 'Name', 'Version'], how='inner')

# Unique project names
proj_names = merged['ProjectName'].dropna().unique().tolist()

# Parse project_info to map repo -> forks
repo_map = {}
for info in df_pinfo['Project_Information'].dropna().astype(str):
    # find first owner/repo pattern
    mrepo = re.search(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)', info)
    if not mrepo:
        continue
    repo = mrepo.group(1)
    # find forks number
    mf = re.search(r'([0-9,]+)\s*(?:forks|forked|fork)\b', info, flags=re.IGNORECASE)
    forks = 0
    if mf:
        try:
            forks = int(mf.group(1).replace(',', ''))
        except:
            forks = 0
    # keep max forks if multiple entries
    if repo in repo_map:
        if forks > repo_map[repo]['forks']:
            repo_map[repo]['forks'] = forks
            repo_map[repo]['info'] = info
    else:
        repo_map[repo] = {'forks': forks, 'info': info}

# Build results for proj_names
results = []
for pn in proj_names:
    entry = repo_map.get(pn)
    forks = entry['forks'] if entry else 0
    info = entry['info'] if entry else None
    results.append({'ProjectName': pn, 'Forks': int(forks), 'Project_Information': info})

res_df = pd.DataFrame(results)
if not res_df.empty:
    res_df = res_df.groupby('ProjectName', as_index=False).agg({'Forks':'max', 'Project_Information':'first'})
    res_df = res_df.sort_values('Forks', ascending=False)
    top5 = res_df.head(5).to_dict(orient='records')
else:
    top5 = []

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_9RxvN1ms11PAi3Z2GfMMtlMd': 'file_storage/call_9RxvN1ms11PAi3Z2GfMMtlMd.json', 'var_call_EcIJ2eetWqFLydiCAGYVIT2o': 'file_storage/call_EcIJ2eetWqFLydiCAGYVIT2o.json', 'var_call_3o5dX0GZKJoHEIx7XkqnSff8': 'file_storage/call_3o5dX0GZKJoHEIx7XkqnSff8.json'}

exec(code, env_args)
