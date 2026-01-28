code = """import json
import pandas as pd
import re

# Load data from storage-provided variables (file paths or lists)

def load_var(v):
    # v can be a filepath string or already a list
    if isinstance(v, str):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            # fallback: try to parse as JSON string
            try:
                return json.loads(v)
            except:
                return []
    else:
        return v

pkg = load_var(var_call_DAdk8eI0MPidScnRYERN4hEz)
ppv = load_var(var_call_2gSQiwrP5YQSHAAa3V3d8Vha)
pinfo = load_var(var_call_xx327ibXZCtlav0t6mwzRYZH)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pinfo_df = pd.DataFrame(pinfo)

# Normalize columns
for df in [pkg_df, ppv_df]:
    if 'System' not in df.columns:
        df['System'] = 'NPM'

# Parse VersionInfo and UpstreamPublishedAt
import math

def parse_versioninfo(s):
    if not s or s == '':
        return {}
    try:
        return json.loads(s)
    except:
        # try to fix single quotes or trailing commas
        try:
            return json.loads(s.replace("'", '"'))
        except:
            return {}

pkg_df['VersionInfo_parsed'] = pkg_df['VersionInfo'].apply(lambda x: parse_versioninfo(x) if pd.notnull(x) else {})

# extract IsRelease
pkg_df['IsRelease'] = pkg_df['VersionInfo_parsed'].apply(lambda d: bool(d.get('IsRelease')) if isinstance(d, dict) else False)

# UpstreamPublishedAt may be string of float; convert to numeric
def to_num(x):
    try:
        return float(x)
    except:
        try:
            return float(str(x))
        except:
            return float('nan')

pkg_df['UpstreamPublishedAt_num'] = pkg_df['UpstreamPublishedAt'].apply(lambda x: to_num(x))

# Group by Name and pick latest release version if exists, else latest by published
latest_rows = []
for name, g in pkg_df.groupby('Name'):
    # prefer IsRelease True
    rels = g[g['IsRelease'] == True]
    if len(rels) > 0:
        sel = rels.loc[rels['UpstreamPublishedAt_num'].idxmax()]
    else:
        # pick latest overall
        sel = g.loc[g['UpstreamPublishedAt_num'].idxmax()]
    latest_rows.append({'Name': sel['Name'], 'Version': sel['Version']})

latest_df = pd.DataFrame(latest_rows)

# Merge with project_packageversion to get ProjectName
merged = pd.merge(latest_df, ppv_df, on=['Name', 'Version'], how='left')
# Keep only rows with a ProjectName
merged = merged[merged['ProjectName'].notnull()].copy()

# For each merged row, find matching Project_Information entry that contains the ProjectName
# Build a lookup from project_info text to stars
pinfo_df['text'] = pinfo_df['Project_Information'].astype(str)

# Function to extract stars from text
star_re = re.compile(r"([0-9][0-9,]*)\s+stars")

def extract_stars(text):
    if not isinstance(text, str):
        return 0
    m = star_re.search(text)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except:
            return 0
    # try alternative phrasing
    m2 = re.search(r"stars\s+count\s+of\s+([0-9][0-9,]*)", text)
    if m2:
        try:
            return int(m2.group(1).replace(',', ''))
        except:
            return 0
    return 0

pinfo_df['stars'] = pinfo_df['text'].apply(extract_stars)

# For faster search, create mapping from projectname -> stars by finding first matching entry
project_to_stars = {}
texts = pinfo_df['text'].tolist()
stars_list = pinfo_df['stars'].tolist()

for i, t in enumerate(texts):
    # attempt to find a substring pattern like 'project owner/repo'
    # We'll not build mapping here; instead we'll search per project in merged
    pass

# Now for each merged ProjectName, search pinfo entries for substring
def find_stars_for_project(projname):
    if not isinstance(projname, str):
        return 0
    for t, s in zip(texts, stars_list):
        if projname in t:
            return s
    # try alternative: if only repo name present without owner
    repo_part = projname.split('/')[-1]
    for t, s in zip(texts, stars_list):
        if ('/' + repo_part) in t or (repo_part + ' on GitHub' in t):
            return s
    return 0

merged['Stars'] = merged['ProjectName'].apply(find_stars_for_project)

# Select top 5 by Stars
top5 = merged.sort_values('Stars', ascending=False).head(5)

# Prepare results
results = []
for _, r in top5.iterrows():
    results.append({'Package': r['Name'], 'Version': r['Version'], 'ProjectName': r.get('ProjectName', None), 'Stars': int(r['Stars'])})

import json
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mIQ43AUsk83lOr35Oi1JcRr2': ['packageinfo'], 'var_call_aW6Ao9ldLfZuhTfwm9p9awwN': ['project_info', 'project_packageversion'], 'var_call_DAdk8eI0MPidScnRYERN4hEz': 'file_storage/call_DAdk8eI0MPidScnRYERN4hEz.json', 'var_call_2gSQiwrP5YQSHAAa3V3d8Vha': 'file_storage/call_2gSQiwrP5YQSHAAa3V3d8Vha.json', 'var_call_xx327ibXZCtlav0t6mwzRYZH': 'file_storage/call_xx327ibXZCtlav0t6mwzRYZH.json'}

exec(code, env_args)
