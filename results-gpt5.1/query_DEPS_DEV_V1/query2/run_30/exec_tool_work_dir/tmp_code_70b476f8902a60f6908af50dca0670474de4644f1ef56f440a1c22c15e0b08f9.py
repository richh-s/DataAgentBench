code = """import json, pandas as pd, re

# Load packageinfo filtered result
pkg_path = var_call_uNP0oNserpM4z0CALFfhiAvU
with open(pkg_path, 'r') as f:
    pkg = json.load(f)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()

# Load project_packageversion
ppv_path = var_call_UKw8GG8A0SRZINVmWiMADpvg
with open(ppv_path, 'r') as f:
    ppv = json.load(f)

df_ppv = pd.DataFrame(ppv)

# inner join on System, Name, Version
merged = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')

# keep unique projects
projects = merged[['ProjectName']].drop_duplicates()

# Load project_info text
pi_path = var_call_d0vW1UNCiDkXUY2hLv8fmDmr
with open(pi_path, 'r') as f:
    pi = json.load(f)

df_pi = pd.DataFrame(pi)

# Extract repo name and fork count from Project_Information
repo_pat = re.compile(r"project ([^ ]+/[^ ]+) on GitHub", re.IGNORECASE)
repo_pat2 = re.compile(r"hosted on GitHub under the name ([^, ]+)", re.IGNORECASE)
repo_pat3 = re.compile(r"named ([^, ]+) on GitHub", re.IGNORECASE)

fork_pat = re.compile(r"(\d+) forks")

records = []
for text in df_pi['Project_Information']:
    if not isinstance(text, str):
        continue
    repo = None
    m = repo_pat.search(text)
    if m:
        repo = m.group(1)
    if not repo:
        m = repo_pat2.search(text)
        if m:
            repo = m.group(1)
    if not repo:
        m = repo_pat3.search(text)
        if m:
            repo = m.group(1)
    if not repo:
        # pattern like "The project lodash/lodash on GitHub"
        m = re.search(r"project ([^ ]+/[^ ]+) is hosted on GitHub", text, re.IGNORECASE)
        if m:
            repo = m.group(1)
    if not repo:
        continue
    fm = fork_pat.search(text)
    if not fm:
        continue
    forks = int(fm.group(1))
    records.append({'ProjectName': repo, 'Forks': forks})

proj_forks = pd.DataFrame(records).drop_duplicates(subset=['ProjectName'])

# match only projects linked from NPM MIT release packages
proj_linked = projects.merge(proj_forks, on='ProjectName', how='inner')

# get top 5 by forks
top5 = proj_linked.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uNP0oNserpM4z0CALFfhiAvU': 'file_storage/call_uNP0oNserpM4z0CALFfhiAvU.json', 'var_call_r3QjFw2pITXbZTXR2nXN221b': ['project_info', 'project_packageversion'], 'var_call_ha6175AZUf0dXJQH77haukV6': [], 'var_call_zMKVTaScVU6pFBURRxiRNJMo': {'num_packages': 176998}, 'var_call_UKw8GG8A0SRZINVmWiMADpvg': 'file_storage/call_UKw8GG8A0SRZINVmWiMADpvg.json', 'var_call_d0vW1UNCiDkXUY2hLv8fmDmr': 'file_storage/call_d0vW1UNCiDkXUY2hLv8fmDmr.json'}

exec(code, env_args)
