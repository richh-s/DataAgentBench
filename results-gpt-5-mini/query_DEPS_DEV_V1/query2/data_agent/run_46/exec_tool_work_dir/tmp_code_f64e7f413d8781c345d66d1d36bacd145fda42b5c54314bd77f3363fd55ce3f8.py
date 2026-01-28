code = """import json, re, pandas as pd

# Load data from storage file paths
with open(var_call_EmY2MMWLU310N648ykkb29Eq, 'r') as f:
    pkg = json.load(f)
with open(var_call_7OPk2ZbexW45C42qiR26SEnu, 'r') as f:
    ppv = json.load(f)
with open(var_call_N5K2JvUxJ7AabmF0ZbFHxIFY, 'r') as f:
    proj = json.load(f)

# DataFrames
df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)
df_proj = pd.DataFrame(proj)

# Merge packageinfo matches with project_packageversion
if not df_pkg.empty and not df_ppv.empty:
    merged = pd.merge(df_pkg, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
else:
    merged = pd.DataFrame(columns=['System','Name','Version','ProjectName'])

unique_projects = merged['ProjectName'].dropna().unique().tolist()

# Build mapping from repo (owner/repo) to forks count by parsing Project_Information
repo_forks = {}
for pi in df_proj['Project_Information'].dropna().astype(str):
    # extract repo path
    m = re.search(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', pi)
    if not m:
        continue
    repo = m.group(1)
    forks = None
    # Try several patterns to extract forks
    patterns = [
        r'forks count of\s*[:\s]*([0-9,]+)',
        r'\bforks\b\s*[:\s]*([0-9,]+)',
        r'been forked\s*([0-9,]+)\s*times',
        r'forked\s*([0-9,]+)\s*times',
        r'(?:has|and has|and been forked|and has been forked)[^\d\n\r]*([0-9,]+)\s*forks',
        r'([0-9,]+)\s+forks'
    ]
    for pat in patterns:
        mm = re.search(pat, pi, flags=re.IGNORECASE)
        if mm:
            forks = mm.group(1)
            break
    if forks:
        try:
            forks = int(forks.replace(',', ''))
        except:
            forks = 0
    else:
        # fallback: look for any number near 'fork'
        mm = re.search(r'([0-9,]+)\s*(?:forks|forked)', pi, flags=re.IGNORECASE)
        if mm:
            forks = int(mm.group(1).replace(',', ''))
        else:
            forks = 0
    # store max forks if multiple entries
    if repo in repo_forks:
        repo_forks[repo] = max(repo_forks[repo], forks)
    else:
        repo_forks[repo] = forks

# Compile list of projects from merged data with forks
rows = []
for repo in unique_projects:
    forks = int(repo_forks.get(repo, 0))
    rows.append({'ProjectName': repo, 'Forks': forks})

# Sort and take top 5
rows_sorted = sorted(rows, key=lambda x: x['Forks'], reverse=True)[:5]

# Output as JSON string
print("__RESULT__:")
print(json.dumps(rows_sorted))"""

env_args = {'var_call_EmY2MMWLU310N648ykkb29Eq': 'file_storage/call_EmY2MMWLU310N648ykkb29Eq.json', 'var_call_7OPk2ZbexW45C42qiR26SEnu': 'file_storage/call_7OPk2ZbexW45C42qiR26SEnu.json', 'var_call_N5K2JvUxJ7AabmF0ZbFHxIFY': 'file_storage/call_N5K2JvUxJ7AabmF0ZbFHxIFY.json'}

exec(code, env_args)
