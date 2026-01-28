code = """import json
import pandas as pd
import re

# Load stored results (they may be file paths if results were large)
def load_var(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r') as f:
            return json.load(f)
    return var

packages = load_var(var_call_6auXgtRpKcvJu2SyJHZiQvOT)
proj_pkg = load_var(var_call_FtLbO9q0fvckjYaEAtwWwYdG)
proj_info = load_var(var_call_aeraRv0G6XSAVfKBkngn1N95)

df_packages = pd.DataFrame(packages)
df_proj_pkg = pd.DataFrame(proj_pkg)
df_proj_info = pd.DataFrame(proj_info)

# Merge packageinfo with project_packageversion on System, Name, Version
merged = pd.merge(df_packages, df_proj_pkg[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Build mapping from repo (owner/repo) to project information and forks
repo_info = {}
repo_regex = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
# patterns to find forks
fork_patterns = [re.compile(p, re.IGNORECASE) for p in [r"(\d{1,3}(?:,\d{3})*)\s+forks", r"forks count of\s*(\d{1,3}(?:,\d{3})*)", r"forked\s*(\d{1,3}(?:,\d{3})*)\s+times", r"and\s*(\d{1,3}(?:,\d{3})*)\s+forks", r"has been forked\s*(\d{1,3}(?:,\d{3})*)\s*times"]]

for rec in proj_info:
    pi = rec.get('Project_Information') or ''
    m = repo_regex.search(pi)
    if not m:
        continue
    repo = m.group(1)
    forks = None
    for pat in fork_patterns:
        m2 = pat.search(pi)
        if m2:
            forks_str = m2.group(1).replace(',', '')
            try:
                forks = int(forks_str)
                break
            except:
                forks = None
    # store the first seen project information; if multiple entries for same repo, keep the max forks
    if repo:
        if repo in repo_info:
            # update forks if larger
            existing = repo_info[repo]
            if forks is not None:
                if existing['forks'] is None or forks > existing['forks']:
                    existing['forks'] = forks
                    existing['Project_Information'] = pi
        else:
            repo_info[repo] = {'Project_Information': pi, 'forks': forks}

# For each merged ProjectName, get forks from mapping
merged['Repo'] = merged['ProjectName']

# Map forks
def get_forks(repo):
    info = repo_info.get(repo)
    return info['forks'] if info else None

merged['Forks'] = merged['Repo'].apply(get_forks)

# Filter ones with forks not None
with_forks = merged[merged['Forks'].notnull()].copy()
# Keep unique repos with their forks (take max if multiple)
repo_forks = with_forks.groupby('Repo', as_index=False)['Forks'].max()
# Sort desc and take top 5
top5 = repo_forks.sort_values('Forks', ascending=False).head(5)

# Prepare output list with project info text if available
result = []
for _, row in top5.iterrows():
    repo = row['Repo']
    forks = int(row['Forks'])
    pi = repo_info.get(repo, {}).get('Project_Information')
    result.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': pi})

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6auXgtRpKcvJu2SyJHZiQvOT': 'file_storage/call_6auXgtRpKcvJu2SyJHZiQvOT.json', 'var_call_FtLbO9q0fvckjYaEAtwWwYdG': 'file_storage/call_FtLbO9q0fvckjYaEAtwWwYdG.json', 'var_call_aeraRv0G6XSAVfKBkngn1N95': 'file_storage/call_aeraRv0G6XSAVfKBkngn1N95.json'}

exec(code, env_args)
