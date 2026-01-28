code = """import json, re, pandas as pd

# Load data from storage file paths
with open(var_call_EmY2MMWLU310N648ykkb29Eq, 'r') as f:
    pkg = json.load(f)
with open(var_call_7OPk2ZbexW45C42qiR26SEnu, 'r') as f:
    ppv = json.load(f)
with open(var_call_N5K2JvUxJ7AabmF0ZbFHxIFY, 'r') as f:
    proj = json.load(f)

# Create DataFrames
_df_pkg = pd.DataFrame(pkg)
_df_ppv = pd.DataFrame(ppv)
_df_proj = pd.DataFrame(proj)

# Merge packageinfo matches with project_packageversion
if not _df_pkg.empty and not _df_ppv.empty:
    merged = pd.merge(_df_pkg, _df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
else:
    merged = pd.DataFrame(columns=['System','Name','Version','ProjectName'])

unique_projects = merged['ProjectName'].dropna().unique().tolist()

# Helper to extract number near 'fork'
def extract_number_near_fork(text):
    t = text.lower()
    idx = t.find('fork')
    if idx == -1:
        return 0
    # look left for number
    left = t[:idx]
    # scan leftwards to find last run of digits and commas
    i = len(left)-1
    while i >= 0 and (left[i].isdigit() or left[i] == ','):
        i -= 1
    left_num = left[i+1:].strip()
    if left_num:
        try:
            return int(left_num.replace(',', ''))
        except:
            pass
    # look right for number
    right = t[idx:]
    m = re.search(r'([0-9,]+)', right)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            return 0
    return 0

# Build repo->forks mapping
repo_forks = {}
for entry in _df_proj['Project_Information'].dropna().astype(str):
    m = re.search('([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', entry)
    if not m:
        continue
    repo = m.group(1)
    forks = extract_number_near_fork(entry)
    if repo in repo_forks:
        repo_forks[repo] = max(repo_forks[repo], forks)
    else:
        repo_forks[repo] = forks

# Compile rows for projects linked to packages
rows = []
for repo in unique_projects:
    fcount = int(repo_forks.get(repo, 0))
    rows.append({'ProjectName': repo, 'Forks': fcount})

# Sort and select top 5
rows_sorted = sorted(rows, key=lambda x: x['Forks'], reverse=True)[:5]

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(rows_sorted))"""

env_args = {'var_call_EmY2MMWLU310N648ykkb29Eq': 'file_storage/call_EmY2MMWLU310N648ykkb29Eq.json', 'var_call_7OPk2ZbexW45C42qiR26SEnu': 'file_storage/call_7OPk2ZbexW45C42qiR26SEnu.json', 'var_call_N5K2JvUxJ7AabmF0ZbFHxIFY': 'file_storage/call_N5K2JvUxJ7AabmF0ZbFHxIFY.json'}

exec(code, env_args)
