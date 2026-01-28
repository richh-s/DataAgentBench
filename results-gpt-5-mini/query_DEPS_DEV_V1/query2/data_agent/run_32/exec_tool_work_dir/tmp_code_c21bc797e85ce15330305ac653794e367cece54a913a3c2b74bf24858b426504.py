code = """import json
import re
import pandas as pd
from pathlib import Path

# load datasets from storage file paths
pkg_path = Path(var_call_tYJGnLjOEUsz6pVEjgeBGswM)
proj_pkg_path = Path(var_call_lQepeGgCp45JkrLCZQDaUcde)
proj_info_path = Path(var_call_ipkWVA5Deps1rge7bvsYHRhM)

with open(pkg_path, 'r') as f:
    pkg = json.load(f)
with open(proj_pkg_path, 'r') as f:
    proj_pkg = json.load(f)
with open(proj_info_path, 'r') as f:
    proj_info = json.load(f)

df_pkg = pd.DataFrame(pkg)
df_proj_pkg = pd.DataFrame(proj_pkg)
df_proj_info = pd.DataFrame(proj_info)

# Merge on System, Name, Version
merged = pd.merge(df_pkg, df_proj_pkg, on=['System','Name','Version'], how='inner')

# Consider only GitHub projects
merged = merged[merged['ProjectType'].str.upper() == 'GITHUB']

# Unique ProjectName values
proj_names = merged['ProjectName'].dropna().unique().tolist()

# function to extract forks count from Project_Information text
def extract_forks(text):
    if not isinstance(text, str):
        return None
    # try pattern: stars ... forks
    m = re.search(r'([0-9,]+)\s+stars.*?([0-9,]+)\s+forks', text, flags=re.IGNORECASE|re.DOTALL)
    if m:
        return int(m.group(2).replace(',',''))
    # try pattern: ([number]) forks
    m = re.search(r'([0-9,]+)\s+forks', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    # try 'forks count of X'
    m = re.search(r'forks count of\s*([0-9,]+)', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    # try 'has been forked X times' or 'forked X times'
    m = re.search(r'forked\s*([0-9,]+)\s*times', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    m = re.search(r'has been forked\s*([0-9,]+)', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    # try 'and has X forks' or 'has X forks'
    m = re.search(r'has\s*([0-9,]+)\s*forks', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',',''))
    return None

# Build lookup from project_info: for faster search, create mapping of Project_Information texts
proj_info_texts = df_proj_info['Project_Information'].fillna('').tolist()

results = []
for pname in proj_names:
    # find project_info entries that contain the exact owner/repo
    matches = [t for t in proj_info_texts if pname in t]
    chosen = matches[0] if matches else None
    forks = None
    if chosen:
        forks = extract_forks(chosen)
    else:
        # try matching by repo name only (after slash)
        repo_only = pname.split('/')[-1]
        matches2 = [t for t in proj_info_texts if repo_only in t]
        chosen = matches2[0] if matches2 else None
        if chosen:
            forks = extract_forks(chosen)
    if forks is not None:
        results.append({'project': pname, 'forks': forks, 'project_info': chosen})

# Sort and get top 5
results_sorted = sorted(results, key=lambda x: x['forks'], reverse=True)
top5 = results_sorted[:5]

# Prepare JSON output
out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tYJGnLjOEUsz6pVEjgeBGswM': 'file_storage/call_tYJGnLjOEUsz6pVEjgeBGswM.json', 'var_call_33UDpr9cxAjr6lKWmOvP4Oqr': 'file_storage/call_33UDpr9cxAjr6lKWmOvP4Oqr.json', 'var_call_lQepeGgCp45JkrLCZQDaUcde': 'file_storage/call_lQepeGgCp45JkrLCZQDaUcde.json', 'var_call_ipkWVA5Deps1rge7bvsYHRhM': 'file_storage/call_ipkWVA5Deps1rge7bvsYHRhM.json'}

exec(code, env_args)
