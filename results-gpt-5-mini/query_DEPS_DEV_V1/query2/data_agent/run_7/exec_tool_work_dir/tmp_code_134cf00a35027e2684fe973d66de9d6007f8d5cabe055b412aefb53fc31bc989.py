code = """import json
import pandas as pd
import re

# Load query results from storage variables (file paths)
with open(var_call_WP0QgvUXBGzndFHNwByxIEyu, 'r') as f:
    pkg_records = json.load(f)
with open(var_call_fqznU0TxJFLK3Yzy4SKeKJZG, 'r') as f:
    ppv_records = json.load(f)
with open(var_call_qcP1LhpfPW603FyG3wH2e8Jh, 'r') as f:
    pinfo_records = json.load(f)

pkg_df = pd.DataFrame(pkg_records)
ppv_df = pd.DataFrame(ppv_records)
pinfo_df = pd.DataFrame(pinfo_records)

# Ensure strings
for col in ['System','Name','Version']:
    if col in pkg_df.columns:
        pkg_df[col] = pkg_df[col].astype(str)
    if col in ppv_df.columns:
        ppv_df[col] = ppv_df[col].astype(str)

# Join packageinfo rows with project_packageversion on System, Name, Version
merged = pd.merge(pkg_df, ppv_df, on=['System','Name','Version'], how='inner')

# Get unique ProjectName values for NPM GitHub projects related to MIT release packages
project_names = merged['ProjectName'].dropna().astype(str).unique().tolist()
project_names_lc = [p.strip().lower() for p in project_names]

# Parse project_info to extract repo name and fork counts
repo_to_forks = {}
repo_to_stars = {}

repo_pattern = re.compile(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
stars_pattern = re.compile(r"([0-9,]+)\s+stars")
forks_pattern = re.compile(r"([0-9,]+)\s+forks")

for rec in pinfo_records:
    pi = rec.get('Project_Information') or ''
    if not isinstance(pi, str):
        continue
    pi_lc = pi.lower()
    # find repo
    m = repo_pattern.search(pi)
    if not m:
        continue
    repo = m.group(1).strip().lower()
    # find forks and stars
    mf = forks_pattern.search(pi_lc)
    ms = stars_pattern.search(pi_lc)
    if mf:
        forks = int(mf.group(1).replace(',',''))
    else:
        # try alternative phrasing: 'and X forks.' or 'forked X times' - simple fallback: find last number
        nums = re.findall(r"([0-9,]+)", pi_lc)
        forks = int(nums[-1].replace(',','')) if nums else None
    if ms:
        stars = int(ms.group(1).replace(',',''))
    else:
        stars = None
    repo_to_forks[repo] = forks
    repo_to_stars[repo] = stars

# Match project_names to parsed repos
results = []
for orig, lc in zip(project_names, project_names_lc):
    forks = repo_to_forks.get(lc)
    stars = repo_to_stars.get(lc)
    if forks is None:
        # try more flexible matching: find any parsed repo that endswith the project name
        for repo, f in repo_to_forks.items():
            if repo.endswith('/' + lc.split('/')[-1]):
                forks = f
                stars = repo_to_stars.get(repo)
                break
    if forks is None:
        continue
    results.append({'ProjectName': orig, 'Forks': forks, 'Stars': stars})

# Deduplicate by ProjectName, keep max forks if duplicates
dfr = pd.DataFrame(results)
if dfr.empty:
    top5 = []
else:
    dfr = dfr.sort_values(['Forks','Stars'], ascending=[False, False])
    dfr = dfr.drop_duplicates(subset=['ProjectName'])
    top5 = dfr.head(5)[['ProjectName','Forks','Stars']].to_dict(orient='records')

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_WP0QgvUXBGzndFHNwByxIEyu': 'file_storage/call_WP0QgvUXBGzndFHNwByxIEyu.json', 'var_call_fqznU0TxJFLK3Yzy4SKeKJZG': 'file_storage/call_fqznU0TxJFLK3Yzy4SKeKJZG.json', 'var_call_qcP1LhpfPW603FyG3wH2e8Jh': 'file_storage/call_qcP1LhpfPW603FyG3wH2e8Jh.json'}

exec(code, env_args)
