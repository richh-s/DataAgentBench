code = """import json
import re
import pandas as pd

# Load data from previous query results stored as file paths
with open(var_call_NDuKreuNXkIt8A6rStif2uHN, 'r') as f:
    pkg_latest = json.load(f)
with open(var_call_7Qddoysmxqm5IHts58UR0fjU, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_thYKR6evmV98EfaslaKPQ8KN, 'r') as f:
    proj_info = json.load(f)

# Convert to DataFrame
df_pkg = pd.DataFrame(pkg_latest)
df_projpkg = pd.DataFrame(proj_pkg)
df_projinfo = pd.DataFrame(proj_info)

# Keep only relevant columns
df_pkg = df_pkg[['System','Name','Version']]

# Merge to find project names for latest package versions
merged = pd.merge(df_pkg, df_projpkg, on=['System','Name','Version'], how='left')

# Function to extract stars from Project_Information text
star_patterns = [
    r'has\s+([\d,]+)\s+stars',
    r'stars count of\s+([\d,]+)',
    r'([\d,]+)\s+stars',
    r'stars, and\s+([\d,]+)\s+forks'  # fallback
]

def extract_stars(text):
    if not isinstance(text, str):
        return None
    for pat in star_patterns:
        m = re.search(pat, text)
        if m:
            num = m.group(1)
            num = num.replace(',', '')
            try:
                return int(num)
            except:
                continue
    return None

# Build mapping from ProjectName to stars by searching Project_Information text
projinfo_texts = df_projinfo['Project_Information'].fillna('').tolist()
projinfo_list = df_projinfo.to_dict(orient='records')

# For efficient search, create list of tuples (project_info_text, stars)
proj_texts_with_stars = []
for rec in projinfo_list:
    txt = rec.get('Project_Information') or ''
    stars = extract_stars(txt)
    proj_texts_with_stars.append((txt, stars))

# For each merged row with a ProjectName, try to find matching project_info row where ProjectName appears in Project_Information
results = []
for _, row in merged.iterrows():
    pkg_name = row['Name']
    version = row['Version']
    projname = row.get('ProjectName')
    stars = None
    matched_projinfo = None
    if isinstance(projname, str):
        # search for the ProjectName string in project_info texts
        for txt, st in proj_texts_with_stars:
            if projname in txt:
                stars = st
                matched_projinfo = txt
                break
    # Append result
    results.append({'Name': pkg_name, 'Version': version, 'ProjectName': projname, 'Stars': stars, 'Project_Information': matched_projinfo})

# Aggregate per package name: choose the maximum stars among possible project matches
agg = {}
for r in results:
    name = r['Name']
    if name not in agg:
        agg[name] = {'Name': name, 'Version': r['Version'], 'Stars': r['Stars'], 'ProjectName': r['ProjectName']}
    else:
        # prefer higher stars
        cur_stars = agg[name]['Stars']
        new_stars = r['Stars']
        if new_stars is not None and (cur_stars is None or new_stars > cur_stars):
            agg[name] = {'Name': name, 'Version': r['Version'], 'Stars': new_stars, 'ProjectName': r['ProjectName']}

# Create list and filter out packages without star info
agg_list = list(agg.values())
# Remove entries with None stars
agg_with_stars = [a for a in agg_list if a['Stars'] is not None]

# Sort by Stars desc and take top 5
top5 = sorted(agg_with_stars, key=lambda x: x['Stars'], reverse=True)[:5]

# Prepare output: list of dicts with Name, Version, Stars, ProjectName
out = [{'Name': t['Name'], 'Version': t['Version'], 'Stars': int(t['Stars']), 'ProjectName': t['ProjectName']} for t in top5]

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_NDuKreuNXkIt8A6rStif2uHN': 'file_storage/call_NDuKreuNXkIt8A6rStif2uHN.json', 'var_call_7Qddoysmxqm5IHts58UR0fjU': 'file_storage/call_7Qddoysmxqm5IHts58UR0fjU.json', 'var_call_thYKR6evmV98EfaslaKPQ8KN': 'file_storage/call_thYKR6evmV98EfaslaKPQ8KN.json'}

exec(code, env_args)
