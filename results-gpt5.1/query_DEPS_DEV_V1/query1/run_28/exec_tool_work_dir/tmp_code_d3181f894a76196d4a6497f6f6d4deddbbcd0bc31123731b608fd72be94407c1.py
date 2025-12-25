code = """import json, pandas as pd
from pathlib import Path

pkg_path = Path(var_call_igw0vnQyiIWpC8CwsHKHnA96)
proj_pkg_path = Path(var_call_f4LnjOGibCJFwKWjgSXlIFya)
proj_info_path = Path(var_call_n263Yzq5PfY7My5835HUv9Hm)

with pkg_path.open() as f:
    pkg = json.load(f)
with proj_pkg_path.open() as f:
    proj_pkg = json.load(f)
with proj_info_path.open() as f:
    proj_info_raw = json.load(f)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version','VersionInfo']]

pkg_df['VersionInfo'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x,str) else x)
pkg_df = pkg_df[pkg_df['VersionInfo'].apply(lambda d: d.get('IsRelease', False))]

pkg_df['Ordinal'] = pkg_df['VersionInfo'].apply(lambda d: d.get('Ordinal', 0))
latest_pkg = pkg_df.sort_values('Ordinal', ascending=False).drop_duplicates(subset=['System','Name'], keep='first')
latest_pkg = latest_pkg[['System','Name','Version']]

proj_pkg_df = pd.DataFrame(proj_pkg)

# Avoid KeyError by using .loc with existing columns list
cols_needed = [c for c in ['System','Name','Version','ProjectName'] if c in proj_pkg_df.columns]
proj_pkg_df = proj_pkg_df[proj_pkg_df['System']=='NPM'][cols_needed]

merged = latest_pkg.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

import re
records = []
for row in proj_info_raw:
    text = row.get('Project_Information','')
    m_name = re.search(r'project\s+([\w.-]+/[\w.-]+)', text)
    m_stars = re.search(r'(?:has|a)\s+([0-9,]+)\s+stars', text)
    if not m_name or not m_stars:
        continue
    name = m_name.group(1)
    stars = int(m_stars.group(1).replace(',',''))
    records.append({'ProjectName': name, 'Stars': stars})
proj_info_df = pd.DataFrame(records).drop_duplicates(subset=['ProjectName'], keep='first')

if 'ProjectName' in merged.columns:
    full = merged.merge(proj_info_df, on='ProjectName', how='inner')
    full_sorted = full.sort_values('Stars', ascending=False)
    result = full_sorted.head(5)[['Name','Version','Stars']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_igw0vnQyiIWpC8CwsHKHnA96': 'file_storage/call_igw0vnQyiIWpC8CwsHKHnA96.json', 'var_call_gEXA7kVIEwvWGLakqqnPG8rB': ['project_info', 'project_packageversion'], 'var_call_f4LnjOGibCJFwKWjgSXlIFya': 'file_storage/call_f4LnjOGibCJFwKWjgSXlIFya.json', 'var_call_n263Yzq5PfY7My5835HUv9Hm': 'file_storage/call_n263Yzq5PfY7My5835HUv9Hm.json', 'var_call_6L6Yfy4FSZNi3NG65oMJhM7Y': [], 'var_call_7q64WtYC0Z9UotmJNz3ge0Ay': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType'], 'var_call_j0c5HliQYMZdc0Mw6VnVsejI': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'var_call_3x52whQ5tWlotFmXoe8h832c': {'columns': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType'], 'projectname_in_columns': True}}

exec(code, env_args)
