code = """import pandas as pd
import json
import re

# Read the large JSON result file paths provided in storage
pck_path = var_call_9RxvN1ms11PAi3Z2GfMMtlMd
ppv_path = var_call_EcIJ2eetWqFLydiCAGYVIT2o
pinfo_path = var_call_3o5dX0GZKJoHEIx7XkqnSff8

# Load data
df_pck = pd.read_json(pck_path)
df_ppv = pd.read_json(ppv_path)
df_pinfo = pd.read_json(pinfo_path)

# Filter project_packageversion to GITHUB only and relevant System
df_ppv = df_ppv[df_ppv['ProjectType'].str.upper() == 'GITHUB']

# Merge package rows (already filtered for NPM MIT releases) with project_packageversion on System, Name, Version
merged = pd.merge(df_pck, df_ppv, on=['System','Name','Version'], how='inner')

# Get unique ProjectName values
proj_names = merged['ProjectName'].dropna().unique().tolist()

# Parse project_info to extract repo (owner/repo) and forks count
repo_list = []
for idx, row in df_pinfo.iterrows():
    info = row.get('Project_Information', '')
    if not isinstance(info, str):
        continue
    # find repo pattern owner/repo
    repo_match = re.search(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)', info)
    repo = repo_match.group(1) if repo_match else None
    # find forks number near the word forks or forked
    forks = None
    m = re.search(r'([0-9,]+)\s*(?:forks|forked|fork)\b', info, flags=re.IGNORECASE)
    if m:
        forks = int(m.group(1).replace(',',''))
    else:
        # fallback: look for 'forks count of X' patterns
        m2 = re.search(r'forks count of\s*([0-9,]+)', info, flags=re.IGNORECASE)
        if m2:
            forks = int(m2.group(1).replace(',',''))
    if repo:
        repo_list.append({'repo': repo, 'forks': forks if forks is not None else 0, 'info': info})

# Build mapping repo -> forks (if multiple entries take max forks)
repo_df = pd.DataFrame(repo_list)
if repo_df.empty:
    repo_map = {}
else:
    repo_map = repo_df.groupby('repo').agg({'forks':'max','info': 'first'}).to_dict(orient='index')

# For each project name from merge, get forks
results = []
for pn in proj_names:
    entry = repo_map.get(pn)
    forks = entry['forks'] if entry else 0
    info = entry['info'] if entry else None
    results.append({'ProjectName': pn, 'Forks': int(forks) if forks is not None else 0, 'Project_Information': info})

# Aggregate by ProjectName (in case duplicates) and take max forks
res_df = pd.DataFrame(results)
if res_df.empty:
    top5 = []
else:
    res_df = res_df.groupby('ProjectName').agg({'Forks':'max','Project_Information':'first'}).reset_index()
    res_df = res_df.sort_values('Forks', ascending=False)
    top5 = res_df.head(5).to_dict(orient='records')

# Print result in required format as JSON string
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(top5).replace("'", "\\'") + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_9RxvN1ms11PAi3Z2GfMMtlMd': 'file_storage/call_9RxvN1ms11PAi3Z2GfMMtlMd.json', 'var_call_EcIJ2eetWqFLydiCAGYVIT2o': 'file_storage/call_EcIJ2eetWqFLydiCAGYVIT2o.json', 'var_call_3o5dX0GZKJoHEIx7XkqnSff8': 'file_storage/call_3o5dX0GZKJoHEIx7XkqnSff8.json'}

exec(code, env_args)
