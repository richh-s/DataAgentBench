code = """import json
import pandas as pd
import re

# Load JSON from stored file paths
with open(var_call_r04VcrGqvfZ0QMtfHEQrVRuB, 'r', encoding='utf-8') as f:
    latest_records = json.load(f)
with open(var_call_OSlYN3fUEm9xBk7srvxCkpH4, 'r', encoding='utf-8') as f:
    projver_records = json.load(f)
with open(var_call_rbjtOrzGIRLURSYjtgNNd6bA, 'r', encoding='utf-8') as f:
    projinfo_records = json.load(f)

# Create DataFrames
_df_latest = pd.DataFrame(latest_records)
_df_projver = pd.DataFrame(projver_records)
_df_projinfo = pd.DataFrame(projinfo_records)

# Ensure required columns
if 'Name' not in _df_latest.columns or 'Version' not in _df_latest.columns:
    raise SystemExit('Expected Name and Version in latest package records')
if not {'System','Name','Version','ProjectName'}.issubset(_df_projver.columns):
    raise SystemExit('project_packageversion missing expected columns')

# Convert to strings
_df_latest['Name'] = _df_latest['Name'].astype(str)
_df_latest['Version'] = _df_latest['Version'].astype(str)
_df_projver['Name'] = _df_projver['Name'].astype(str)
_df_projver['Version'] = _df_projver['Version'].astype(str)

# Merge to map packages to GitHub project names
_df_map = pd.merge(_df_latest[['Name','Version']], _df_projver[['System','Name','Version','ProjectName']], on=['Name','Version'], how='inner')

# Build mapping from ProjectName to stars by searching Project_Information text
proj_stars = {}
all_texts = _df_projinfo['Project_Information'].astype(str).tolist()

for pn in _df_map['ProjectName'].dropna().unique():
    pn_str = str(pn)
    best = 0
    # find project_info entries that mention this project name
    matches = [t for t in all_texts if pn_str in t]
    for text in matches:
        txt = text.lower()
        # find occurrences of 'star' and look for numbers near it
        idx = txt.find('star')
        while idx != -1:
            start = max(0, idx-40)
            end = min(len(txt), idx+40)
            window = txt[start:end]
            nums = re.findall('[0-9][0-9,]*', window)
            for n in nums:
                try:
                    val = int(n.replace(',', ''))
                    if val > best:
                        best = val
                except:
                    pass
            idx = txt.find('star', idx+1)
    proj_stars[pn_str] = best

# Aggregate max stars per package (Name,Version)
results = []
for (name, version), group in _df_map.groupby(['Name','Version']):
    project_names = group['ProjectName'].dropna().astype(str).unique()
    max_stars = 0
    for pn in project_names:
        max_stars = max(max_stars, proj_stars.get(pn, 0))
    results.append({'Name': name, 'Version': version, 'Stars': int(max_stars)})

# Sort and take top 5
results_sorted = sorted(results, key=lambda x: x['Stars'], reverse=True)
top5 = results_sorted[:5]

# Print in required format
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_4YhPTB6U6nz5GrDAJSdpl10Y': ['packageinfo'], 'var_call_WPlwlWeUDwtz9xUlXTPFhb3U': ['project_info', 'project_packageversion'], 'var_call_r04VcrGqvfZ0QMtfHEQrVRuB': 'file_storage/call_r04VcrGqvfZ0QMtfHEQrVRuB.json', 'var_call_OSlYN3fUEm9xBk7srvxCkpH4': 'file_storage/call_OSlYN3fUEm9xBk7srvxCkpH4.json', 'var_call_rbjtOrzGIRLURSYjtgNNd6bA': 'file_storage/call_rbjtOrzGIRLURSYjtgNNd6bA.json'}

exec(code, env_args)
