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

# Build DataFrames
df_pkgs = pd.DataFrame(pkgs)
df_ppv = pd.DataFrame(ppvs)
df_pi = pd.DataFrame(pis)

# Parse VersionInfo and UpstreamPublishedAt

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

# Attach
df_pkgs['IsRelease'] = is_release_list
df_pkgs['Ordinal'] = ordinal_list
df_pkgs['UpstreamPublishedAt_num'] = upstream_list

# Filter NPM releases

df_releases = df_pkgs[(df_pkgs['IsRelease']==True) & (df_pkgs['System']=='NPM')].copy()

# For performance, we'll group and compute latest index using idxmax on UpstreamPublishedAt_num

# If UpstreamPublishedAt_num is null for some groups, fallback to Ordinal later

grp = df_releases.groupby('Name')

# Compute max upstream and ordinal per group
max_up = grp['UpstreamPublishedAt_num'].max()
max_ord = grp['Ordinal'].max()

# Build a dataframe of latest by choosing by UpstreamPublishedAt_num when available
latest_idx = []
for name, group in grp:
    if pd.notnull(max_up.loc[name]):
        # choose row with this max upstream
        idxmax = group['UpstreamPublishedAt_num'].idxmax()
    elif pd.notnull(max_ord.loc[name]):
        idxmax = group['Ordinal'].idxmax()
    else:
        idxmax = group.index[0]
    latest_idx.append(idxmax)

latest_rows = df_releases.loc[latest_idx].reset_index(drop=True)

# Keep only System, Name, Version
latest = latest_rows[['System','Name','Version']]

# Merge with project_packageversion
merged = pd.merge(latest, df_ppv[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

# Some packages may map to multiple projects; keep non-null ProjectName
merged_nonnull = merged.dropna(subset=['ProjectName']).copy()

# For each merged row, find project info text that contains the ProjectName
pi_texts = [r.get('Project_Information','') for r in pis]

import re

def extract_stars(text):
    if not text:
        return 0
    m = re.search(r'([0-9][0-9,]*)\s+stars', text, re.I)
    if m:
        return int(m.group(1).replace(',',''))
    m2 = re.search(r'has garnered a total of\s*([0-9,]+)\s*stars', text, re.I)
    if m2:
        return int(m2.group(1).replace(',',''))
    return 0

stars = []
for idx, row in merged_nonnull.iterrows():
    pname = row['ProjectName']
    found = None
    for t in pi_texts:
        if pname in t:
            found = t
            break
    if not found and '/' in pname:
        owner, repo = pname.split('/',1)
        for t in pi_texts:
            if owner in t and repo in t:
                found = t
                break
    s = extract_stars(found)
    stars.append(s)

merged_nonnull['Stars'] = stars

# Some ProjectName appear multiple times due to multiple package names mapping; group by package Name and take max stars
best_per_pkg = merged_nonnull.groupby('Name', as_index=False).agg({'Version':'first','ProjectName':'first','Stars':'max'})

# Now pick top 5 by Stars
top5 = best_per_pkg.sort_values(by='Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CJZhajwS3qMiYjKY8nUHfTm1': ['packageinfo'], 'var_call_FtqMybgYmGGAyxyivBimhT9W': ['project_info', 'project_packageversion'], 'var_call_FivGpH4t0NfQFAUPFyBGHV1V': 'file_storage/call_FivGpH4t0NfQFAUPFyBGHV1V.json', 'var_call_41iMZj8Uk64lYGbt4pIv7PWr': 'file_storage/call_41iMZj8Uk64lYGbt4pIv7PWr.json', 'var_call_5glgSpqrtkeEL66qVt9GP4oC': 'file_storage/call_5glgSpqrtkeEL66qVt9GP4oC.json', 'var_call_9te9Jq5qzFkU6vu8uxpd78Kp': {'pkg_count': 661372, 'ppv_count': 597602, 'pi_count': 770, 'pkg_first_keys': ['System', 'Name', 'Version', 'VersionInfo', 'UpstreamPublishedAt'], 'ppv_first_keys': ['System', 'Name', 'Version', 'ProjectName'], 'pi_first_keys': ['Project_Information'], 'pkg_sample0': {'System': 'NPM', 'Name': '@ecl/twig-component-carousel', 'Version': '3.11.1', 'VersionInfo': '{\n  "IsRelease": true,\n  "Ordinal": 29\n}', 'UpstreamPublishedAt': '1699345351000000.0'}, 'ppv_sample0': {'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, 'pi_sample0': {'Project_Information': 'The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.'}}}

exec(code, env_args)
