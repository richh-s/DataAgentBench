code = """import json, pandas as pd

# Load full data from JSON files
import_path1 = var_call_kORJ31RF9Xg13UWrlGfmzQQA
import_path2 = var_call_Q2ecjeuh7yRa305pycn4BkgR
import_path3 = var_call_YTwudGHOdetGJLrARJSNSh5w

with open(import_path1, 'r') as f:
    pkg_release = json.load(f)
with open(import_path2, 'r') as f:
    proj_pkgver = json.load(f)
with open(import_path3, 'r') as f:
    proj_info = json.load(f)

pkg_df = pd.DataFrame(pkg_release)
ppv_df = pd.DataFrame(proj_pkgver)
pi_df = pd.DataFrame(proj_info)

# Join NPM MIT release packages with project_packageversion on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Filter to GitHub projects only (if ProjectType exists)
if 'ProjectType' in merged.columns:
    merged = merged[merged['ProjectType'] == 'GITHUB']

# Project_Information text contains forks count; extract it via regex
import re

pi_df = pi_df.copy()

# Extract repo name owner/repo and forks count
project_names = []
fork_counts = []
for info in pi_df['Project_Information']:
    # repo pattern: something like 'project owner/repo' or 'named owner/repo'
    m_repo = re.search(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", info)
    project_names.append(m_repo.group(1) if m_repo else None)
    m_forks = re.search(r"(\d+) forks", info)
    fork_counts.append(int(m_forks.group(1)) if m_forks else None)

pi_df['ProjectName'] = project_names
pi_df['Forks'] = fork_counts

# Merge to attach fork counts
full = merged.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='left')

# Drop entries without fork info
full = full.dropna(subset=['Forks'])

# For each distinct project, take max Forks (should be same across rows)
proj_forks = full.groupby('ProjectName')['Forks'].max().reset_index()

# Top 5 by forks
top5 = proj_forks.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kORJ31RF9Xg13UWrlGfmzQQA': 'file_storage/call_kORJ31RF9Xg13UWrlGfmzQQA.json', 'var_call_Q2ecjeuh7yRa305pycn4BkgR': 'file_storage/call_Q2ecjeuh7yRa305pycn4BkgR.json', 'var_call_YTwudGHOdetGJLrARJSNSh5w': 'file_storage/call_YTwudGHOdetGJLrARJSNSh5w.json'}

exec(code, env_args)
