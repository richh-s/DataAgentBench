code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_ikF56cBFZVYmeQVKFV438xxh)
ppv = load(var_call_dsfMQ7mhiFUiK7euiu0BApv2)
pi = load(var_call_dD7Oyq7Hms4RwbC2PEC2OgmD)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest version per package by max UpstreamPublishedAt (ties: max Version lexicographically)
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest = pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False]) \
              .drop_duplicates(subset=['Name'], keep='first')[['System','Name','Version']]

# join to project mapping (same system/name/version)
merged = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse project name and stars from Project_Information
# create mapping from ProjectName -> stars
pat = re.compile(r"project\s+([^\s]+/[^\s]+).*?([0-9][0-9,]*)\s+stars", re.IGNORECASE)
proj_stars = {}
for s in pi_df['Project_Information'].dropna().astype(str):
    m = pat.search(s)
    if not m:
        continue
    pname = m.group(1).strip().strip(',').strip('.')
    stars = int(m.group(2).replace(',',''))
    if pname not in proj_stars or stars > proj_stars[pname]:
        proj_stars[pname] = stars

merged['Stars'] = merged['ProjectName'].map(proj_stars)
merged = merged.dropna(subset=['Stars'])

# if multiple repos per package, take max stars
best = merged.sort_values(['Name','Stars'], ascending=[True, False]).drop_duplicates('Name', keep='first')

# top 5 by stars
out = best.sort_values('Stars', ascending=False).head(5)[['Name','Version','ProjectName','Stars']]
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ikF56cBFZVYmeQVKFV438xxh': 'file_storage/call_ikF56cBFZVYmeQVKFV438xxh.json', 'var_call_dsfMQ7mhiFUiK7euiu0BApv2': 'file_storage/call_dsfMQ7mhiFUiK7euiu0BApv2.json', 'var_call_dD7Oyq7Hms4RwbC2PEC2OgmD': 'file_storage/call_dD7Oyq7Hms4RwbC2PEC2OgmD.json'}

exec(code, env_args)
