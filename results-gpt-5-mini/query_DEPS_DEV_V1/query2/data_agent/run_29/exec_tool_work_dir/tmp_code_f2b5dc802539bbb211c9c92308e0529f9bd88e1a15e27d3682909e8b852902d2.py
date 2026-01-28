code = """import json
import pandas as pd
import re

# Load data from previous tool calls (could be JSON lists or file paths)
def load_var(v):
    if isinstance(v, str):
        # it's a file path to a JSON file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_dwLdhFFCIwjkVFEjdmq8yHc1)
ppv = load_var(var_call_tT2wGBgpfA2tB5vVmx1L1wWt)
pinfo = load_var(var_call_2UA4BofQr2qGrsP1G85VO0iI)

df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)
df_pinfo = pd.DataFrame(pinfo)

# Ensure columns exist
for c in ['System','Name','Version']:
    if c not in df_pkg.columns:
        df_pkg[c] = None
    if c not in df_ppv.columns:
        df_ppv[c] = None

# Merge package rows with project_packageversion on System, Name, Version
# Some Name may have different normalization; do exact match as instructed
merged = pd.merge(df_pkg[['System','Name','Version']], df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='inner')

# Unique projects
projects = merged['ProjectName'].dropna().unique().tolist()

# Helper to extract fork count from Project_Information text
patterns = [
    r"([0-9][0-9,]*)\s+forks",
    r"forks count of\s*([0-9][0-9,]*)",
    r"has been forked\s*([0-9][0-9,]*)\s*times",
    r"forked\s*([0-9][0-9,]*)\s*times",
    r"([0-9][0-9,]*)\s+forks,",
    r"([0-9][0-9,]*)\s+forks\.",
    r"([0-9][0-9,]*)\s+fork",
]

proj_to_forks = {}

for proj in projects:
    # find project_info rows containing the proj string
    mask = df_pinfo['Project_Information'].fillna('').str.contains(proj, regex=False)
    matches = df_pinfo[mask]
    forks = None
    info_text = None
    if not matches.empty:
        # Try each matched row to extract forks
        for txt in matches['Project_Information'].fillna(''):
            info_text = txt
            found = None
            for pat in patterns:
                m = re.search(pat, txt)
                if m:
                    num = m.group(1)
                    # remove commas
                    try:
                        val = int(num.replace(',',''))
                        found = val
                        break
                    except:
                        continue
            if found is not None:
                forks = found
                break
    # If not found via direct match, try to extract owner/repo from project_info and map
    if forks is None:
        # try to extract owner/repo from proj itself or project_info entries
        # As fallback, attempt to find any project_info that mentions the repo owner (before '/')
        owner = proj.split('/')[0] if isinstance(proj,str) and '/' in proj else None
        if owner:
            mask2 = df_pinfo['Project_Information'].fillna('').str.contains(owner, regex=False)
            matches2 = df_pinfo[mask2]
            for txt in matches2['Project_Information'].fillna(''):
                for pat in patterns:
                    m = re.search(pat, txt)
                    if m:
                        try:
                            forks = int(m.group(1).replace(',',''))
                            info_text = txt
                            break
                        except:
                            continue
                if forks is not None:
                    break
    if forks is None:
        # default to 0 if not found
        forks = 0
    proj_to_forks[proj] = {'Forks': forks, 'Project_Information': info_text}

# Prepare sorted list
items = [{'ProjectName': k, 'Forks': v['Forks']} for k,v in proj_to_forks.items()]
items_sorted = sorted(items, key=lambda x: x['Forks'], reverse=True)

top5 = items_sorted[:5]

import json
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_dwLdhFFCIwjkVFEjdmq8yHc1': 'file_storage/call_dwLdhFFCIwjkVFEjdmq8yHc1.json', 'var_call_tT2wGBgpfA2tB5vVmx1L1wWt': 'file_storage/call_tT2wGBgpfA2tB5vVmx1L1wWt.json', 'var_call_2UA4BofQr2qGrsP1G85VO0iI': 'file_storage/call_2UA4BofQr2qGrsP1G85VO0iI.json'}

exec(code, env_args)
