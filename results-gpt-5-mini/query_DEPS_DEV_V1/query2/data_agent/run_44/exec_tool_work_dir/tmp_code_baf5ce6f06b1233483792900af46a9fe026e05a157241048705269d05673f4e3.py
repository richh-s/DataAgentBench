code = """import pandas as pd
import json
import re

df_pkg = pd.read_json(var_call_eZTWND63B9Ut5HlwIDSFC7V7)
df_projver = pd.read_json(var_call_vYGlZ0TX6a8k7YP3TkaDHMqV)
df_projinfo = pd.read_json(var_call_fbiTpSQdrZQvcL68NGf3VaXF)

# Merge to get ProjectName for MIT & IsRelease packages
merged = pd.merge(df_pkg[['System','Name','Version']], df_projver[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')
proj_names = merged['ProjectName'].dropna().astype(str).unique().tolist()
# Normalize project names: remove leading/trailing spaces and leading slashes
proj_set = set([pn.strip().lstrip('/') for pn in proj_names if '/' in pn])

# Prepare regex patterns for repo and forks
repo_pattern = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
fork_patterns = [re.compile(r'forks count of ([\d,]+)', re.IGNORECASE),
                 re.compile(r'([\d,]+) forks', re.IGNORECASE),
                 re.compile(r'has been forked ([\d,]+)', re.IGNORECASE),
                 re.compile(r'forked ([\d,]+)', re.IGNORECASE),
                 re.compile(r'forks: ([\d,]+)', re.IGNORECASE)]

repo_forks = {}
repo_info = {}

for idx, row in df_projinfo.iterrows():
    info = str(row.get('Project_Information','') or '')
    # find all repo-like tokens
    repos = repo_pattern.findall(info)
    if not repos:
        # sometimes text says 'is named owner/repo' with punctuation; still captured by pattern
        continue
    # try to find forks
    forks = None
    for p in fork_patterns:
        m = p.search(info)
        if m:
            try:
                forks = int(m.group(1).replace(',',''))
                break
            except:
                pass
    # if no forks found, leave as None
    for r in repos:
        rnorm = r.strip().lstrip('/')
        if rnorm in proj_set:
            # update mapping
            if forks is None:
                val = repo_forks.get(rnorm)
                # keep existing if exists, else set to None/0
                if val is None:
                    repo_forks.setdefault(rnorm, None)
            else:
                existing = repo_forks.get(rnorm)
                if existing is None or existing is None:
                    repo_forks[rnorm] = forks
                else:
                    repo_forks[rnorm] = max(existing, forks)
            # keep sample info
            if rnorm not in repo_info:
                repo_info[rnorm] = info

# Convert None forks to 0
for k in list(repo_forks.keys()):
    if repo_forks[k] is None:
        repo_forks[k] = 0

# If some project names from proj_set were not found in project_info, add them with forks=0
for pn in proj_set:
    if pn not in repo_forks:
        repo_forks[pn] = 0
        repo_info[pn] = ''

# Get top 5 by forks
items = sorted(repo_forks.items(), key=lambda x: x[1], reverse=True)
top5 = []
for repo, forks in items[:5]:
    top5.append({'repo': repo, 'forks': forks, 'info': repo_info.get(repo,'')})

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_eZTWND63B9Ut5HlwIDSFC7V7': 'file_storage/call_eZTWND63B9Ut5HlwIDSFC7V7.json', 'var_call_vYGlZ0TX6a8k7YP3TkaDHMqV': 'file_storage/call_vYGlZ0TX6a8k7YP3TkaDHMqV.json', 'var_call_hE4No6ehI7Zq0OEf0b1kbyrR': 'file_storage/call_hE4No6ehI7Zq0OEf0b1kbyrR.json', 'var_call_fbiTpSQdrZQvcL68NGf3VaXF': 'file_storage/call_fbiTpSQdrZQvcL68NGf3VaXF.json'}

exec(code, env_args)
