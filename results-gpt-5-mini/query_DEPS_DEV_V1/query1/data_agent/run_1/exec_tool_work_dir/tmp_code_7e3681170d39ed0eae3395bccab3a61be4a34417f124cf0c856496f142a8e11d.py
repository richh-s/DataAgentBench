code = """import json
import pandas as pd
import re

# Load query results from storage files
with open(var_call_pVJOV7XZJ1Opj79Po2pyqOfQ, 'r') as f:
    ppv = json.load(f)  # project_packageversion
with open(var_call_9V72fmMUWDPszr1yGa2erUjW, 'r') as f:
    pkg = json.load(f)  # packageinfo
with open(var_call_O3dKLlAEX812uYLWX9r2Gz3m, 'r') as f:
    proj = json.load(f)  # project_info

df_ppv = pd.DataFrame(ppv)
df_pkg = pd.DataFrame(pkg)
df_proj = pd.DataFrame(proj)

# Parse VersionInfo JSON in packageinfo to extract IsRelease and Ordinal
def parse_versioninfo(v):
    try:
        if v is None:
            return (False, None)
        # some entries may already be dicts
        if isinstance(v, dict):
            return (v.get('IsRelease', False), v.get('Ordinal'))
        # else string
        parsed = json.loads(v)
        return (parsed.get('IsRelease', False), parsed.get('Ordinal'))
    except Exception:
        # fallback: try to extract ordinal and IsRelease with regex
        isrel = '"IsRelease": true' in (v or "")
        m = re.search(r'"Ordinal"\s*:\s*(\d+)', v or "")
        ordv = int(m.group(1)) if m else None
        return (isrel, ordv)

df_pkg['parsed'] = df_pkg['VersionInfo'].apply(parse_versioninfo)
df_pkg['IsRelease'] = df_pkg['parsed'].apply(lambda x: x[0])
df_pkg['Ordinal'] = df_pkg['parsed'].apply(lambda x: x[1] if x[1] is not None else -1)

# Filter to NPM releases only
df_releases = df_pkg[(df_pkg['System']=='NPM') & (df_pkg['IsRelease']==True)].copy()

# For each package Name, pick the release with highest Ordinal
idx = df_releases.groupby('Name')['Ordinal'].idxmax().dropna()
# idx may contain floats; convert to int
idx = [int(i) for i in idx]
df_latest = df_releases.loc[idx, ['System','Name','Version']].drop_duplicates()

# Join with project_packageversion to get ProjectName
# Ensure ppv filtered to NPM and ProjectType GITHUB
df_ppv_f = df_ppv[(df_ppv['System']=='NPM') & (df_ppv['ProjectType'].str.upper()=='GITHUB')].copy()
# Merge on System, Name, Version
df_merged = pd.merge(df_latest, df_ppv_f, on=['System','Name','Version'], how='left')

# For each merged row, find corresponding project_info row where Project_Information contains ProjectName
# Build a mapping from Project_Information text to itself for faster search
proj_info_texts = df_proj['Project_Information'].astype(str).tolist()

def extract_stars_from_text(text):
    if not isinstance(text, str):
        return None
    # common patterns: 'X stars', 'stars count of X', 'a total of X stars', 'has garnered X stars'
    patterns = [r"([\d,]+)\s+stars",
                r"stars count of\s*([\d,]+)",
                r"total of\s*([\d,]+)\s+stars",
                r"garnered\s+(?:a\s+)?total of\s*([\d,]+)\s+stars",
                r"has\s+garnered\s+(?:a\s+total\s+of\s*)?([\d,]+)\s+stars",
                r"has\s+been\s+starred\s+([\d,]+)\s+times"
               ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            num = m.group(1).replace(',', '')
            try:
                return int(num)
            except:
                continue
    # fallback: sometimes phrasing like '... has 521 open issues, 38715 stars, and 5782 forks' -> find 'stars, and' pattern
    m = re.search(r"([\d,]+)\s*stars", text, flags=re.IGNORECASE)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            return None
    return None

results = []

for _, row in df_merged.iterrows():
    name = row['Name']
    version = row['Version']
    project_name = row.get('ProjectName')
    stars = None
    matched_proj_text = None
    if isinstance(project_name, str) and project_name:
        # search for project_name in project_info texts
        for t in proj_info_texts:
            if project_name in t:
                matched_proj_text = t
                stars = extract_stars_from_text(t)
                break
    # append only if we found stars
    if stars is not None:
        results.append({'Name': name, 'Version': version, 'Project': project_name, 'Stars': stars})

# If no results found, return empty
if not results:
    out = []
else:
    # sort by Stars desc and take top 5
    results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)
    top5 = results_sorted[:5]
    out = top5

import json as _json
print("__RESULT__:")
print(_json.dumps(out))"""

env_args = {'var_call_pVJOV7XZJ1Opj79Po2pyqOfQ': 'file_storage/call_pVJOV7XZJ1Opj79Po2pyqOfQ.json', 'var_call_9V72fmMUWDPszr1yGa2erUjW': 'file_storage/call_9V72fmMUWDPszr1yGa2erUjW.json', 'var_call_O3dKLlAEX812uYLWX9r2Gz3m': 'file_storage/call_O3dKLlAEX812uYLWX9r2Gz3m.json'}

exec(code, env_args)
