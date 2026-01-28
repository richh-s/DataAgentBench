code = """import json
import pandas as pd
import re

# Helper to load data whether it's a list or a path to a json file

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

# Load datasets from storage variables
pkgs = load_var(var_call_2t9lxC29vjmmakFNhooHpDH9)
maps = load_var(var_call_LAdGdj4UhADHgHu0p0EvkftK)
infos = load_var(var_call_keQt0AtL656DkzIoGrJb0oSG)

# Convert to DataFrames
df_pkgs = pd.DataFrame(pkgs)
df_maps = pd.DataFrame(maps)
df_infos = pd.DataFrame(infos)

# Deduplicate package rows by System+Name+Version (keep first)
df_pkgs = df_pkgs.drop_duplicates(subset=['System','Name','Version'])

# Merge with mapping to get ProjectName
merged = pd.merge(df_pkgs, df_maps[['System','Name','Version','ProjectName']], on=['System','Name','Version'], how='left')

# Build repo -> stars mapping from project_info by parsing Project_Information
repo_stars = {}
for pi in df_infos['Project_Information'].dropna().astype(str):
    # try to find repo owner/name pattern
    repo_match = re.search(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)', pi)
    if not repo_match:
        continue
    repo = repo_match.group(1)
    # find stars number
    stars_match = re.search(r'([0-9\,]+)\s*stars', pi)
    if not stars_match:
        # sometimes phrasing like 'a total of 2,534 stars'
        stars_match = re.search(r'total of\s*([0-9\,]+)\s*stars', pi)
    stars = None
    if stars_match:
        try:
            stars = int(stars_match.group(1).replace(',',''))
        except:
            stars = None
    # store the max stars if duplicate repos
    if repo in repo_stars:
        if stars is not None and (repo_stars[repo] is None or stars > repo_stars[repo]):
            repo_stars[repo] = stars
    else:
        repo_stars[repo] = stars

# Map ProjectName to stars in merged
def get_stars_for_project(pn):
    if pd.isna(pn):
        return None
    return repo_stars.get(pn)

merged['Stars'] = merged['ProjectName'].apply(get_stars_for_project)

# Keep only rows with a stars value (non-null)
valid = merged[merged['Stars'].notna()].copy()

# Convert Stars to int (they should be already)
valid['Stars'] = valid['Stars'].astype(int)

# For packages that map to multiple rows, keep the max stars per package name (though they should be unique)
# Group by Name and take the row with max Stars
idx = valid.groupby('Name')['Stars'].idxmax()
best = valid.loc[idx]

# Sort by Stars desc and take top 5
top5 = best.sort_values('Stars', ascending=False).head(5)

# Prepare output
output = []
for _, row in top5.iterrows():
    output.append({
        'Name': row['Name'],
        'Version': row['Version'],
        'ProjectName': row.get('ProjectName') if not pd.isna(row.get('ProjectName')) else None,
        'Stars': int(row['Stars'])
    })

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_0ll8xzwkF86LQNtMjlXRbbT9': ['packageinfo'], 'var_call_3g5TTybKNngTDbTJpRK1IhtL': ['project_info', 'project_packageversion'], 'var_call_2t9lxC29vjmmakFNhooHpDH9': 'file_storage/call_2t9lxC29vjmmakFNhooHpDH9.json', 'var_call_LAdGdj4UhADHgHu0p0EvkftK': 'file_storage/call_LAdGdj4UhADHgHu0p0EvkftK.json', 'var_call_keQt0AtL656DkzIoGrJb0oSG': 'file_storage/call_keQt0AtL656DkzIoGrJb0oSG.json'}

exec(code, env_args)
