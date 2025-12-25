code = """import json, pandas as pd
from pathlib import Path

# Load full results from JSON files
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

# Parse VersionInfo JSON and keep only IsRelease==true
pkg_df['VersionInfo'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x) if isinstance(x,str) else x)
pkg_df = pkg_df[pkg_df['VersionInfo'].apply(lambda d: d.get('IsRelease', False))]

# Determine latest release per (System,Name) using Ordinal
pkg_df['Ordinal'] = pkg_df['VersionInfo'].apply(lambda d: d.get('Ordinal', 0))
latest_pkg = pkg_df.sort_values('Ordinal', ascending=False).drop_duplicates(subset=['System','Name'], keep='first')
latest_pkg = latest_pkg[['System','Name','Version']]

proj_pkg_df = pd.DataFrame(proj_pkg)
proj_pkg_df = proj_pkg_df[proj_pkg_df['System']=='NPM'][['System','Name','Version','ProjectName']]

# Join latest packages with project_packageversion
merged = latest_pkg.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# Parse project_info to get ProjectName and stars
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

# Join merged with project_info on ProjectName
full = merged.merge(proj_info_df, on='ProjectName', how='inner')

# For each package Name, keep the max Stars (in case multiple projects, unlikely)
full_sorted = full.sort_values('Stars', ascending=False)

# Top 5 by stars
top5 = full_sorted.head(5)[['Name','Version','Stars']]

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_igw0vnQyiIWpC8CwsHKHnA96': 'file_storage/call_igw0vnQyiIWpC8CwsHKHnA96.json', 'var_call_gEXA7kVIEwvWGLakqqnPG8rB': ['project_info', 'project_packageversion'], 'var_call_f4LnjOGibCJFwKWjgSXlIFya': 'file_storage/call_f4LnjOGibCJFwKWjgSXlIFya.json', 'var_call_n263Yzq5PfY7My5835HUv9Hm': 'file_storage/call_n263Yzq5PfY7My5835HUv9Hm.json'}

exec(code, env_args)
