code = """import json, re, pandas as pd

# Load data from previous tool outputs (large results stored as file paths)
path_pairs = var_call_iz4384JLpjQN4hA64l5XRruR
path_proj_pkg = var_call_pWrhDs21fM26iU5y23P5sPp5
path_proj_info = var_call_WMTArFAC4jwQYN050yX5gqFM

with open(path_pairs, 'r', encoding='utf-8') as f:
    pairs = json.load(f)
with open(path_proj_pkg, 'r', encoding='utf-8') as f:
    proj_pkg = json.load(f)
with open(path_proj_info, 'r', encoding='utf-8') as f:
    proj_info = json.load(f)

# DataFrames
df_pairs = pd.DataFrame(pairs)
df_proj_pkg = pd.DataFrame(proj_pkg)

# Merge on Name and Version
merged = pd.merge(df_pairs, df_proj_pkg, on=['Name', 'Version'], how='inner')
# Get unique ProjectName values
project_names = merged['ProjectName'].dropna().unique().tolist()

# Build mapping from repo (owner/repo) to project_info record and forks
repo_to_info = {}

repo_pattern = re.compile(r'([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
forks_pattern = re.compile(r'([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s+forks', re.IGNORECASE)

for rec in proj_info:
    info_text = rec.get('Project_Information') or ''
    # find repo
    m = repo_pattern.search(info_text)
    repo = m.group(1) if m else None
    # find forks
    mf = forks_pattern.search(info_text)
    forks = 0
    if mf:
        forks = int(mf.group(1).replace(',', ''))
    # if repo found, map
    if repo:
        repo_to_info[repo.lower()] = {'Project_Information': info_text, 'Forks': forks, 'Licenses': rec.get('Licenses'), 'Description': rec.get('Description'), 'Homepage': rec.get('Homepage')}
    else:
        # also attempt to index by repo name if possible: try to find pattern like 'The project <owner>/<repo>' earlier, but skip
        pass

# For project_names, try to find matching info
results = []
for pn in project_names:
    key = pn.lower()
    entry = None
    if key in repo_to_info:
        entry = repo_to_info[key]
    else:
        # try match by repo name only
        owner_repo = key.split('/')
        if len(owner_repo) == 2:
            owner, repo_only = owner_repo
            # try find any repo in repo_to_info that endswith '/repo_only'
            for r, info in repo_to_info.items():
                if r.endswith('/' + repo_only):
                    entry = info
                    break
    forks = entry['Forks'] if entry else 0
    proj_info_text = entry['Project_Information'] if entry else None
    results.append({'ProjectName': pn, 'Forks': forks, 'Project_Information': proj_info_text})

# Aggregate by ProjectName in case multiple package versions map to same project
df_res = pd.DataFrame(results)
df_agg = df_res.groupby('ProjectName', as_index=False).agg({'Forks': 'max', 'Project_Information': 'first'})
# Sort desc by Forks
df_sorted = df_agg.sort_values('Forks', ascending=False).head(5)

out = df_sorted.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_tYSqXN27S3qNNzfXJjqkaExN': 'file_storage/call_tYSqXN27S3qNNzfXJjqkaExN.json', 'var_call_iz4384JLpjQN4hA64l5XRruR': 'file_storage/call_iz4384JLpjQN4hA64l5XRruR.json', 'var_call_pWrhDs21fM26iU5y23P5sPp5': 'file_storage/call_pWrhDs21fM26iU5y23P5sPp5.json', 'var_call_WMTArFAC4jwQYN050yX5gqFM': 'file_storage/call_WMTArFAC4jwQYN050yX5gqFM.json'}

exec(code, env_args)
