code = """import json
import re
import pandas as pd

# Load data from storage file paths
with open(var_call_rmpVmFZPxmjQG2AMtBUSQ5dm, 'r', encoding='utf-8') as f:
    pkg_rows = json.load(f)
with open(var_call_FsaVPbm5D7t5ekow5fVKVghq, 'r', encoding='utf-8') as f:
    map_rows = json.load(f)
with open(var_call_2t1SYJw48dAdfuhCsZUneRXN, 'r', encoding='utf-8') as f:
    proj_rows = json.load(f)

# DataFrames
df_pkg = pd.DataFrame(pkg_rows)
df_map = pd.DataFrame(map_rows)
df_proj = pd.DataFrame(proj_rows)

# Merge packages with project mapping on System, Name, Version
merged = pd.merge(df_pkg, df_map[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Keep unique ProjectNames
project_names = merged['ProjectName'].dropna().astype(str).unique()

# Helper to extract forks from Project_Information text
def extract_forks(text):
    if not isinstance(text, str):
        return None
    patterns = [
        r"([\d,]+)\s+forks",
        r"forks count of\s*[:]?\s*([\d,]+)",
        r"forks count[:]?\s*([\d,]+)",
        r"forked\s*[:]?\s*([\d,]+)\s*times",
        r"has been forked\s*([\d,]+)",
        r"has garnered.*?([\d,]+)\s*forks",
        r"and\s*([\d,]+)\s*forks",
        r"([\d,]+)\s*forks?[,\.]",
        r"forks[:]?\s*([\d,]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    # Sometimes phrased like "has been forked 12 times"
    m = re.search(r"forked\D*([\d,]+)", text, flags=re.IGNORECASE)
    if m:
        num = m.group(1).replace(',', '')
        try:
            return int(num)
        except:
            pass
    return None

# Build lookup of project_info texts
proj_info_texts = df_proj['Project_Information'].fillna('').astype(str).tolist()

# For faster matching, create list of tuples (Project_Information, forks)
proj_info_parsed = []
for info in proj_info_texts:
    forks = extract_forks(info)
    proj_info_parsed.append({'info': info, 'forks': forks})

# For each project_name, find matching project_info entries where project_name appears in info text
results = []
for pname in project_names:
    matches = [p for p in proj_info_parsed if pname in p['info']]
    if not matches:
        # try matching only repo name (after slash) if full not found
        if '/' in pname:
            repo_only = pname.split('/',1)[1]
            matches = [p for p in proj_info_parsed if repo_only in p['info']]
    if not matches:
        continue
    # choose max forks among matches (treat None as -1)
    max_forks = None
    chosen_info = None
    for m in matches:
        fcount = m['forks']
        if fcount is None:
            continue
        if max_forks is None or fcount > max_forks:
            max_forks = fcount
            chosen_info = m['info']
    # If no numeric forks found, try to pick any match with forks None and set to 0
    if max_forks is None:
        # if any match exists, set forks to 0 and pick the first info
        chosen_info = matches[0]['info']
        max_forks = 0
    results.append({'ProjectName': pname, 'Forks': max_forks, 'Project_Information': chosen_info})

# Deduplicate by ProjectName (already unique) and sort by Forks desc
results_sorted = sorted(results, key=lambda x: x['Forks'] if x['Forks'] is not None else -1, reverse=True)

top5 = results_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_rmpVmFZPxmjQG2AMtBUSQ5dm': 'file_storage/call_rmpVmFZPxmjQG2AMtBUSQ5dm.json', 'var_call_FsaVPbm5D7t5ekow5fVKVghq': 'file_storage/call_FsaVPbm5D7t5ekow5fVKVghq.json', 'var_call_2t1SYJw48dAdfuhCsZUneRXN': 'file_storage/call_2t1SYJw48dAdfuhCsZUneRXN.json'}

exec(code, env_args)
