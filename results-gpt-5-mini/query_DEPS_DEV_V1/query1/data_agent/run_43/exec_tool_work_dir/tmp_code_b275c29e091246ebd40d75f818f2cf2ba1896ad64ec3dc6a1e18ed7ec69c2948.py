code = """import json
import pandas as pd
import re

pkg_path = var_call_FivGpH4t0NfQFAUPFyBGHV1V
ppv_path = var_call_41iMZj8Uk64lYGbt4pIv7PWr
pi_path = var_call_5glgSpqrtkeEL66qVt9GP4oC

with open(pkg_path, 'r', encoding='utf-8') as f:
    pkgs = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppvs = json.load(f)
with open(pi_path, 'r', encoding='utf-8') as f:
    pis = json.load(f)

# DataFrames
if isinstance(pkgs, list) and len(pkgs)>0 and isinstance(pkgs[0], dict):
    df_pkgs = pd.DataFrame(pkgs)
else:
    df_pkgs = pd.DataFrame()

if isinstance(ppvs, list) and len(ppvs)>0 and isinstance(ppvs[0], dict):
    df_ppv = pd.DataFrame(ppvs)
else:
    df_ppv = pd.DataFrame()

if isinstance(pis, list) and len(pis)>0 and isinstance(pis[0], dict):
    df_pi = pd.DataFrame(pis)
else:
    df_pi = pd.DataFrame()

# Ensure columns exist
for col in ['System','Name','Version','VersionInfo','UpstreamPublishedAt']:
    if col not in df_pkgs.columns:
        df_pkgs[col] = None
for col in ['System','Name','Version','ProjectName']:
    if col not in df_ppv.columns:
        df_ppv[col] = None

# Fill System with 'NPM' where missing
if 'System' in df_pkgs.columns:
    df_pkgs['System'] = df_pkgs['System'].fillna('NPM')
if 'System' in df_ppv.columns:
    df_ppv['System'] = df_ppv['System'].fillna('NPM')

# Parse VersionInfo

def parse_versioninfo(vi):
    try:
        data = json.loads(vi)
    except Exception:
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

if len(df_pkgs)>0:
    df_pkgs['IsRelease'] = is_release_list
    df_pkgs['Ordinal'] = ordinal_list
    df_pkgs['UpstreamPublishedAt_num'] = upstream_list
else:
    df_pkgs['IsRelease'] = pd.Series(dtype=bool)
    df_pkgs['Ordinal'] = pd.Series(dtype=float)
    df_pkgs['UpstreamPublishedAt_num'] = pd.Series(dtype=float)

# Filter NPM releases
if 'System' in df_pkgs.columns:
    df_releases = df_pkgs[(df_pkgs['IsRelease']==True) & (df_pkgs['System']=='NPM')].copy()
else:
    df_releases = df_pkgs[df_pkgs['IsRelease']==True].copy()

# pick latest per Name

def pick_latest(group):
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

if len(df_releases)>0:
    latest_rows = df_releases.groupby('Name', as_index=False).apply(lambda g: pick_latest(g)).reset_index(drop=True)
    if isinstance(latest_rows, pd.Series):
        latest_rows = latest_rows.to_frame().T
else:
    latest_rows = pd.DataFrame(columns=df_releases.columns)

# Ensure System present
if 'System' not in latest_rows.columns:
    latest_rows['System'] = 'NPM'
else:
    latest_rows['System'] = latest_rows['System'].fillna('NPM')

# Ensure df_ppv System filled
if 'System' not in df_ppv.columns:
    df_ppv['System'] = 'NPM'
else:
    df_ppv['System'] = df_ppv['System'].fillna('NPM')

# Prepare minimal latest
latest = latest_rows[['System','Name','Version']].drop_duplicates()

# Merge on System, Name, Version
merge_on = ['System','Name','Version']
for col in merge_on:
    if col not in df_ppv.columns:
        df_ppv[col] = None

merged = pd.merge(latest, df_ppv[['System','Name','Version','ProjectName']], on=merge_on, how='left')

# Deduplicate
merged = merged.drop_duplicates(subset=['Name'])

pi_texts = [r.get('Project_Information','') for r in pis]

stars_list = []
matched_project_info = []
for idx, row in merged.iterrows():
    pname = row.get('ProjectName')
    found_text = None
    if pname and isinstance(pname, str):
        for text in pi_texts:
            if pname in text:
                found_text = text
                break
    if found_text is None and pname and '/' in pname:
        owner, repo = pname.split('/',1)
        for text in pi_texts:
            if owner in text and repo in text:
                found_text = text
                break
    matched_project_info.append(found_text)
    stars = 0
    if found_text:
        m = re.search(r'([0-9][0-9,]*)\s+stars', found_text, re.I)
        if m:
            try:
                stars = int(m.group(1).replace(',',''))
            except:
                stars = 0
        else:
            m2 = re.search(r'has garnered a total of\s*([0-9,]+)\s*stars', found_text, re.I)
            if m2:
                try:
                    stars = int(m2.group(1).replace(',',''))
                except:
                    stars = 0
    stars_list.append(int(stars))

merged['Project_Information'] = matched_project_info
merged['Stars'] = stars_list

merged_nonull = merged.dropna(subset=['ProjectName']).copy()

top5 = merged_nonull.sort_values(by='Stars', ascending=False).head(5)

result = []
for _, r in top5.iterrows():
    result.append({'Name': r['Name'], 'Version': r['Version'], 'ProjectName': r['ProjectName'], 'Stars': int(r['Stars'])})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CJZhajwS3qMiYjKY8nUHfTm1': ['packageinfo'], 'var_call_FtqMybgYmGGAyxyivBimhT9W': ['project_info', 'project_packageversion'], 'var_call_FivGpH4t0NfQFAUPFyBGHV1V': 'file_storage/call_FivGpH4t0NfQFAUPFyBGHV1V.json', 'var_call_41iMZj8Uk64lYGbt4pIv7PWr': 'file_storage/call_41iMZj8Uk64lYGbt4pIv7PWr.json', 'var_call_5glgSpqrtkeEL66qVt9GP4oC': 'file_storage/call_5glgSpqrtkeEL66qVt9GP4oC.json'}

exec(code, env_args)
