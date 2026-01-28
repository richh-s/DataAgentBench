code = """import json
import pandas as pd
import re

# Load data from storage variables (they may be file paths or already lists)

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to a json
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_pNIjHE3o9a3zDzMzhZUv0Ubj)
ppv = load_var(var_call_OZHgFr7rS1jFcpaDCTB9gmFv)
pinfo = load_var(var_call_X1oS1P9R1bSZllGgiXvtHyNr)

df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)
df_pinfo = pd.DataFrame(pinfo)

# Merge packageinfo with project_packageversion on System, Name, Version
if not df_pkg.empty and not df_ppv.empty:
    merged = pd.merge(df_pkg, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')
else:
    merged = pd.DataFrame()

# Extract ProjectName list for matched packages
projects = merged['ProjectName'].dropna().unique().tolist()

# Parse project_info to extract repo name and forks count
repo_list = []
for rec in pinfo:
    pi = rec.get('Project_Information') or ''
    # find repo pattern owner/repo
    m = re.search(r"\b[\w.-]+/[\w.-]+\b", pi)
    repo = m.group(0) if m else None
    # find forks count - look for patterns like 'X forks', 'forks count of X', 'and X forks', 'forks: X'
    forks = None
    # common pattern: number followed by 'fork' (allow commas)
    m2 = re.search(r"([0-9][0-9,]*)\s*(?:forks|fork)\b", pi)
    if m2:
        forks = int(m2.group(1).replace(',',''))
    else:
        # try 'forks count of X'
        m3 = re.search(r"forks count of\s*([0-9][0-9,]*)", pi)
        if m3:
            forks = int(m3.group(1).replace(',',''))
    repo_list.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': pi})

df_repo = pd.DataFrame(repo_list)
# Drop entries without repo or forks
df_repo = df_repo.dropna(subset=['ProjectName'])
# Some repos may appear multiple times; take max forks per repo
# But first ensure Forks numeric; replace None with 0
df_repo['Forks'] = df_repo['Forks'].fillna(0).astype(int)

# Aggregate by ProjectName
agg = df_repo.groupby('ProjectName', as_index=False)['Forks'].max()

# Filter to projects that are linked from packages
agg_filtered = agg[agg['ProjectName'].isin(projects)]

# Get top 5 by forks
top5 = agg_filtered.sort_values('Forks', ascending=False).head(5)

# Prepare output list
out = []
for _, row in top5.iterrows():
    out.append({'ProjectName': row['ProjectName'], 'Forks': int(row['Forks'])})

# If fewer than 5, that's fine
result = json.dumps(out)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_pNIjHE3o9a3zDzMzhZUv0Ubj': 'file_storage/call_pNIjHE3o9a3zDzMzhZUv0Ubj.json', 'var_call_OZHgFr7rS1jFcpaDCTB9gmFv': 'file_storage/call_OZHgFr7rS1jFcpaDCTB9gmFv.json', 'var_call_X1oS1P9R1bSZllGgiXvtHyNr': 'file_storage/call_X1oS1P9R1bSZllGgiXvtHyNr.json'}

exec(code, env_args)
