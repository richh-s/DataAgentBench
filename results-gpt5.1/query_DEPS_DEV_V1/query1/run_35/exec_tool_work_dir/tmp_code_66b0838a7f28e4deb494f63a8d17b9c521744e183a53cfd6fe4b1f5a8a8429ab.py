code = """import pandas as pd, json, re

# Load latest NPM packages
file_latest = var_call_NuVHOKt1WoYdwM1fbGTElYN0
with open(file_latest, 'r') as f:
    latest_pkgs = json.load(f)
latest_df = pd.DataFrame(latest_pkgs)

# Load project_packageversion
file_pp = var_call_asYmvOEc29FNFqTBORTvbXwY
with open(file_pp, 'r') as f:
    pp_rows = json.load(f)
pp_df = pd.DataFrame(pp_rows)

# Join latest packages with project_packageversion on System, Name, Version
merged = latest_df.merge(pp_df, on=['System','Name','Version'], how='inner')

# Load project_info
file_pi = var_call_gYLi6u6xTJW8pKZLpKVGmgSy
with open(file_pi, 'r') as f:
    pi_rows = json.load(f)
pi_df = pd.DataFrame(pi_rows)

# Extract repo (owner/repo) from Project_Information text using pattern 'project <owner/repo>' or 'named <owner/repo>' or 'under the name <owner/repo>'
repo_pattern = re.compile(r"(?:project|named|under the name)\s+([\w.-]+/[\w.-]+)")

pi_df['Repo'] = pi_df['Project_Information'].apply(lambda txt: repo_pattern.search(txt).group(1) if isinstance(txt,str) and repo_pattern.search(txt) else None)

# Also extract stars count from 'stars' pattern like '1234 stars'
stars_pattern = re.compile(r"(\d[\d,]*)\s+stars")

def extract_stars(txt):
    if not isinstance(txt,str):
        return None
    m = stars_pattern.search(txt)
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

pi_df['Stars'] = pi_df['Project_Information'].apply(extract_stars)

# Map merged.ProjectName (owner/repo) to project_info via Repo
merged2 = merged.merge(pi_df[['Repo','Stars']], left_on='ProjectName', right_on='Repo', how='left')

# For each package Name, keep max Stars (in case multiple projects) and associated Version
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()

# Get top 5 by Stars
top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_A5OTjGZXfH3MHfKLXtw1q5xr': 'file_storage/call_A5OTjGZXfH3MHfKLXtw1q5xr.json', 'var_call_5FgCokRR1d3vHkLnGtAaBxUw': ['project_info', 'project_packageversion'], 'var_call_asYmvOEc29FNFqTBORTvbXwY': 'file_storage/call_asYmvOEc29FNFqTBORTvbXwY.json', 'var_call_gYLi6u6xTJW8pKZLpKVGmgSy': 'file_storage/call_gYLi6u6xTJW8pKZLpKVGmgSy.json', 'var_call_NuVHOKt1WoYdwM1fbGTElYN0': 'file_storage/call_NuVHOKt1WoYdwM1fbGTElYN0.json'}

exec(code, env_args)
