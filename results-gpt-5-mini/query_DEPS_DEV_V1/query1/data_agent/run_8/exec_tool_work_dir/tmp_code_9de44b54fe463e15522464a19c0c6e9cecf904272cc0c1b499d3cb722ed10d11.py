code = """import json
import pandas as pd
import re

# Load JSON from stored file paths
with open(var_call_r04VcrGqvfZ0QMtfHEQrVRuB, 'r') as f:
    latest_records = json.load(f)
with open(var_call_OSlYN3fUEm9xBk7srvxCkpH4, 'r') as f:
    projver_records = json.load(f)
with open(var_call_rbjtOrzGIRLURSYjtgNNd6bA, 'r') as f:
    projinfo_records = json.load(f)

# DataFrames
 df_latest = pd.DataFrame(latest_records)
df_projver = pd.DataFrame(projver_records)
df_projinfo = pd.DataFrame(projinfo_records)

# Merge latest versions with project mappings
if 'Name' not in df_latest.columns or 'Version' not in df_latest.columns:
    raise SystemExit('Expected Name and Version in latest package records')

df_map = pd.merge(df_latest, df_projver[['System','Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# Patterns to extract stars
patterns = [re.compile('([0-9][0-9,]*)\\s+stars', re.IGNORECASE),
            re.compile('stars count of\\s*([0-9][0-9,]*)', re.IGNORECASE),
            re.compile('total of\\s*([0-9][0-9,]*)\\s+stars', re.IGNORECASE),
            re.compile('has garnered.*?([0-9][0-9,]*)\\s+stars', re.IGNORECASE)]

proj_stars = {}
for pn in df_map['ProjectName'].dropna().unique():
    pn_str = str(pn)
    matches = df_projinfo[df_projinfo['Project_Information'].astype(str).str.contains(pn_str, na=False)]
    best = 0
    if not matches.empty:
        for text in matches['Project_Information'].astype(str):
            found = False
            for pat in patterns:
                m = pat.search(text)
                if m:
                    num = int(m.group(1).replace(',', ''))
                    if num > best:
                        best = num
                    found = True
            if not found:
                m2 = re.search('([0-9][0-9,]*)[^\n\r]{0,20}?stars', text, re.IGNORECASE)
                if m2:
                    num = int(m2.group(1).replace(',', ''))
                    if num > best:
                        best = num
    proj_stars[pn_str] = best

# Aggregate per package
results = []
for (name, version), group in df_map.groupby(['Name','Version']):
    project_names = group['ProjectName'].dropna().astype(str).unique()
    max_stars = 0
    for pn in project_names:
        max_stars = max(max_stars, proj_stars.get(pn, 0))
    results.append({'Name': name, 'Version': version, 'Stars': int(max_stars)})

results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)
top5 = results_sorted[:5]

out = json.dumps(top5)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4YhPTB6U6nz5GrDAJSdpl10Y': ['packageinfo'], 'var_call_WPlwlWeUDwtz9xUlXTPFhb3U': ['project_info', 'project_packageversion'], 'var_call_r04VcrGqvfZ0QMtfHEQrVRuB': 'file_storage/call_r04VcrGqvfZ0QMtfHEQrVRuB.json', 'var_call_OSlYN3fUEm9xBk7srvxCkpH4': 'file_storage/call_OSlYN3fUEm9xBk7srvxCkpH4.json', 'var_call_rbjtOrzGIRLURSYjtgNNd6bA': 'file_storage/call_rbjtOrzGIRLURSYjtgNNd6bA.json'}

exec(code, env_args)
