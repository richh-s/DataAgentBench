code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_zrluJU3ZETPcFFrWrV6bwh6x, 'r') as f:
    latest_pkg = json.load(f)
with open(var_call_ZpPIHO070TBScmHqfH3e0QiQ, 'r') as f:
    pkg_map = json.load(f)
with open(var_call_F1Cr1axxD8GaZB9t17l1WRvC, 'r') as f:
    proj_info = json.load(f)

# DataFrames
df_latest = pd.DataFrame(latest_pkg)
# Ensure columns exist
if df_latest.empty:
    df_latest = pd.DataFrame(columns=['Name','Version'])
else:
    df_latest = df_latest[['Name','Version']]

df_map = pd.DataFrame(pkg_map)
if 'System' in df_map.columns:
    df_map = df_map[df_map['System']=='NPM']
else:
    df_map = df_map

# Merge latest packages with mapping to get ProjectName(s)
# There may be multiple project mappings per package
merged = pd.merge(df_latest, df_map[['System','Name','Version','ProjectName']], on=['Name','Version'], how='left')

# Prepare project_info DataFrame and extract stars
df_proj = pd.DataFrame(proj_info)
if df_proj.empty:
    df_proj = pd.DataFrame(columns=['Project_Information'])

# Extract stars using regex from Project_Information
stars_list = []
for pi in df_proj['Project_Information'].fillna(''):
    m = re.search(r"([\d,]+)\s+stars", pi)
    if m:
        stars = int(m.group(1).replace(',', ''))
    else:
        # try alternative phrasing like 'a total of X stars' (still contains 'stars')
        m2 = re.search(r"([\d,]+)\s+star", pi)
        if m2:
            stars = int(m2.group(1).replace(',', ''))
        else:
            stars = None
    stars_list.append(stars)

if 'Project_Information' in df_proj.columns:
    df_proj = df_proj.assign(Stars=stars_list)
else:
    df_proj = pd.DataFrame({'Project_Information': [], 'Stars': []})

# For each merged row, find matching project_info rows by checking if ProjectName substring is in Project_Information
# Build mapping from ProjectName -> max stars found in project_info
project_names = merged['ProjectName'].dropna().unique().tolist()
projname_to_stars = {}
for pn in project_names:
    max_stars = None
    if pn is None:
        projname_to_stars[pn] = None
        continue
    for idx, row in df_proj.iterrows():
        pi = row.get('Project_Information', '') or ''
        s = row.get('Stars')
        if pn in pi:
            if s is not None:
                if (max_stars is None) or (s > max_stars):
                    max_stars = s
    projname_to_stars[pn] = max_stars

# Now compute for each package the maximum stars across its associated ProjectNames
pkg_star_records = []
for name, g in merged.groupby(['Name','Version']):
    Name, Version = name
    project_names = g['ProjectName'].dropna().unique().tolist()
    stars_vals = [projname_to_stars.get(pn) for pn in project_names if projname_to_stars.get(pn) is not None]
    stars = max(stars_vals) if stars_vals else 0
    pkg_star_records.append({'Name': Name, 'Version': Version, 'Stars': int(stars), 'ProjectNames': project_names})

# Get top 5 by Stars
top5 = sorted(pkg_star_records, key=lambda x: x['Stars'], reverse=True)[:5]

# Prepare result
result = top5

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vEKisZqJWopddbWQzMRd4RTg': ['packageinfo'], 'var_call_eYZ4JKovm4apy0FR8ztQOSAQ': ['project_info', 'project_packageversion'], 'var_call_zrluJU3ZETPcFFrWrV6bwh6x': 'file_storage/call_zrluJU3ZETPcFFrWrV6bwh6x.json', 'var_call_ZpPIHO070TBScmHqfH3e0QiQ': 'file_storage/call_ZpPIHO070TBScmHqfH3e0QiQ.json', 'var_call_F1Cr1axxD8GaZB9t17l1WRvC': 'file_storage/call_F1Cr1axxD8GaZB9t17l1WRvC.json'}

exec(code, env_args)
