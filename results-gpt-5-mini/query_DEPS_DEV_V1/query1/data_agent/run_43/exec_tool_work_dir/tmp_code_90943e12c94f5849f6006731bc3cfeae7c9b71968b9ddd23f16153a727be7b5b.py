code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
pkg_path = var_call_FivGpH4t0NfQFAUPFyBGHV1V
ppv_path = var_call_41iMZj8Uk64lYGbt4pIv7PWr
pi_path = var_call_5glgSpqrtkeEL66qVt9GP4oC

with open(pkg_path, 'r', encoding='utf-8') as f:
    pkgs = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppvs = json.load(f)
with open(pi_path, 'r', encoding='utf-8') as f:
    pis = json.load(f)

df_pkgs = pd.DataFrame(pkgs)
df_ppv = pd.DataFrame(ppvs)
df_pi = pd.DataFrame(pis)

# Parse VersionInfo and UpstreamPublishedAt
import math

def parse_versioninfo(vi):
    try:
        data = json.loads(vi)
    except Exception:
        # try to extract fields manually
        data = {}
        if isinstance(vi, str):
            m = re.search(r'"IsRelease"\s*:\s*(true|false)', vi, re.I)
            if m:
                data['IsRelease'] = m.group(1).lower()=='true'
            m2 = re.search(r'"Ordinal"\s*:\s*([0-9]+)', vi)
            if m2:
                data['Ordinal'] = int(m2.group(1))
    return data

is_release_list = []
ordinal_list = []
upstream_list = []
for idx, row in df_pkgs.iterrows():
    vi = row.get('VersionInfo')
    parsed = parse_versioninfo(vi) if vi is not None else {}
    is_release = parsed.get('IsRelease') if 'IsRelease' in parsed else None
    ordinal = parsed.get('Ordinal') if 'Ordinal' in parsed else None
    # UpstreamPublishedAt may be string; convert to float if possible
    up = row.get('UpstreamPublishedAt')
    up_num = None
    try:
        if up is not None and up != '':
            up_num = float(up)
    except Exception:
        up_num = None
    is_release_list.append(bool(is_release))
    ordinal_list.append(int(ordinal) if ordinal is not None else None)
    upstream_list.append(up_num)

df_pkgs['IsRelease'] = is_release_list
df_pkgs['Ordinal'] = ordinal_list
df_pkgs['UpstreamPublishedAt_num'] = upstream_list

# Keep only releases
df_releases = df_pkgs[df_pkgs['IsRelease'] == True].copy()

# For each package Name, pick the latest by UpstreamPublishedAt_num (fall back to Ordinal)

def pick_latest(group):
    # prefer max UpstreamPublishedAt_num
    if group['UpstreamPublishedAt_num'].notnull().any():
        g = group.copy()
        g['up'] = g['UpstreamPublishedAt_num'].fillna(-1)
        return g.loc[g['up'].idxmax()]
    elif group['Ordinal'].notnull().any():
        g = group.copy()
        g['ord'] = g['Ordinal'].fillna(-1)
        return g.loc[g['ord'].idxmax()]
    else:
        return group.iloc[0]

latest_rows = df_releases.groupby('Name', as_index=False).apply(lambda g: pick_latest(g)).reset_index(drop=True)
# latest_rows may have extra index; ensure it's dataframe
if isinstance(latest_rows, pd.Series):
    latest_rows = latest_rows.to_frame().T

# Select relevant columns
latest = latest_rows[['System','Name','Version']].drop_duplicates()

# Join with project_packageversion to get ProjectName
# ensure ppv has System, Name, Version
if not {'System','Name','Version','ProjectName'}.issubset(df_ppv.columns):
    # if ProjectName missing, create empty
    df_ppv['ProjectName'] = df_ppv.get('ProjectName', None)

# Merge and if multiple ProjectName for same package-version, take first
merged = pd.merge(latest, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')
merged = merged.drop_duplicates(subset=['Name'])

# Build a lookup from Project_Information texts
pi_texts = [r.get('Project_Information','') for r in pis]

# For each merged row, find matching Project_Information that contains the ProjectName
stars_list = []
matched_project_info = []
for idx, row in merged.iterrows():
    pname = row.get('ProjectName')
    found_text = None
    if pname and isinstance(pname, str):
        # project info entries likely contain the project path somewhere
        for text in pi_texts:
            if pname in text:
                found_text = text
                break
    # If not found by direct substring, try searching for repo name only (part after /)
    if found_text is None and pname and '/' in pname:
        repo = pname.split('/',1)[1]
        for text in pi_texts:
            if repo in text and pname.split('/')[0] in text:
                found_text = text
                break
    # If still not found, leave None
    matched_project_info.append(found_text)
    stars = 0
    if found_text:
        m = re.search(r'([0-9][0-9,]*)\s+stars', found_text, re.I)
        if m:
            stars = int(m.group(1).replace(',',''))
        else:
            # try alternative phrasing
            m2 = re.search(r'has garnered a total of\s*([0-9,]+)\s*stars', found_text, re.I)
            if m2:
                stars = int(m2.group(1).replace(',',''))
    stars_list.append(int(stars))

merged['Project_Information'] = matched_project_info
merged['Stars'] = stars_list

# Some merged rows may have no ProjectName; drop those
merged_nonull = merged.dropna(subset=['ProjectName']).copy()

# Sort by Stars desc and take top 5
top5 = merged_nonull.sort_values(by='Stars', ascending=False).head(5)

result = []
for _, r in top5.iterrows():
    result.append({'Name': r['Name'], 'Version': r['Version'], 'ProjectName': r['ProjectName'], 'Stars': int(r['Stars'])})

# If less than 5 found, still return whatever
import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_CJZhajwS3qMiYjKY8nUHfTm1': ['packageinfo'], 'var_call_FtqMybgYmGGAyxyivBimhT9W': ['project_info', 'project_packageversion'], 'var_call_FivGpH4t0NfQFAUPFyBGHV1V': 'file_storage/call_FivGpH4t0NfQFAUPFyBGHV1V.json', 'var_call_41iMZj8Uk64lYGbt4pIv7PWr': 'file_storage/call_41iMZj8Uk64lYGbt4pIv7PWr.json', 'var_call_5glgSpqrtkeEL66qVt9GP4oC': 'file_storage/call_5glgSpqrtkeEL66qVt9GP4oC.json'}

exec(code, env_args)
