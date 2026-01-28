code = """import json
import pandas as pd
import re

# Load data from storage-provided variables

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

pkg = load_var(var_call_DAdk8eI0MPidScnRYERN4hEz)
ppv = load_var(var_call_2gSQiwrP5YQSHAAa3V3d8Vha)
pinfo = load_var(var_call_xx327ibXZCtlav0t6mwzRYZH)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pinfo_df = pd.DataFrame(pinfo)

# Parse VersionInfo and UpstreamPublishedAt
import math

def parse_versioninfo(s):
    if pd.isnull(s):
        return {}
    try:
        return json.loads(s)
    except:
        try:
            return json.loads(s.replace("'", '"'))
        except:
            return {}

pkg_df['VersionInfo_parsed'] = pkg_df.get('VersionInfo', pd.Series([None]*len(pkg_df))).apply(parse_versioninfo)
pkg_df['IsRelease'] = pkg_df['VersionInfo_parsed'].apply(lambda d: bool(d.get('IsRelease')) if isinstance(d, dict) else False)

def to_num(x):
    try:
        return float(x)
    except:
        try:
            return float(str(x))
        except:
            return float('nan')

pkg_df['UpstreamPublishedAt_num'] = pkg_df.get('UpstreamPublishedAt', pd.Series([None]*len(pkg_df))).apply(to_num)

# Group by Name and pick latest release version if exists, else latest by published
latest_rows = []
for name, g in pkg_df.groupby('Name'):
    g = g.reset_index(drop=True)
    # prefer IsRelease True
    rels = g[g['IsRelease'] == True]
    sel = None
    def pick_latest(frame):
        # choose row with max UpstreamPublishedAt_num, fallback to first
        if len(frame) == 0:
            return None
        if frame['UpstreamPublishedAt_num'].notnull().any():
            idx = frame['UpstreamPublishedAt_num'].idxmax()
            return frame.loc[idx]
        else:
            return frame.iloc[0]
    if len(rels) > 0:
        sel = pick_latest(rels)
    else:
        sel = pick_latest(g)
    if sel is not None:
        latest_rows.append({'Name': sel['Name'], 'Version': sel['Version']})

latest_df = pd.DataFrame(latest_rows)

# Merge with project_packageversion to get ProjectName
# project_packageversion may have duplicates; keep first mapping per Name+Version
ppv_df = ppv_df[['System','Name','Version','ProjectType','ProjectName']]
merged = pd.merge(latest_df, ppv_df, on=['Name', 'Version'], how='left')
merged = merged[merged['ProjectName'].notnull()].copy()

# Prepare project_info text and extract stars
pinfo_df['text'] = pinfo_df['Project_Information'].astype(str)
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
    # alternative patterns
    m2 = re.search(r"stars\s+count\s+of\s+([0-9][0-9,]*)", text)
    if m2:
        try:
            return int(m2.group(1).replace(',', ''))
        except:
            return 0
    return 0

pinfo_df['stars'] = pinfo_df['text'].apply(extract_stars)
texts = pinfo_df['text'].tolist()
stars_list = pinfo_df['stars'].tolist()

# Find stars for project name by substring match
from functools import lru_cache
@lru_cache(maxsize=None)
def find_stars_for_project(projname):
    if not isinstance(projname, str):
        return 0
    for t, s in zip(texts, stars_list):
        if projname in t:
            return s
    repo_part = projname.split('/')[-1]
    for t, s in zip(texts, stars_list):
        if ('/' + repo_part) in t or (repo_part + ' on GitHub' in t) or (repo_part + ' on GitHub' in t):
            return s
    return 0

merged['Stars'] = merged['ProjectName'].apply(find_stars_for_project)

# Some ProjectName entries might be null; drop them
merged = merged[merged['Stars'] >= 0]

# Get top 5 by Stars
top5 = merged.sort_values('Stars', ascending=False).drop_duplicates(['Name']).head(5)

results = []
for _, r in top5.iterrows():
    results.append({'Package': str(r['Name']), 'Version': str(r['Version']), 'ProjectName': str(r['ProjectName']), 'Stars': int(r['Stars'])})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_mIQ43AUsk83lOr35Oi1JcRr2': ['packageinfo'], 'var_call_aW6Ao9ldLfZuhTfwm9p9awwN': ['project_info', 'project_packageversion'], 'var_call_DAdk8eI0MPidScnRYERN4hEz': 'file_storage/call_DAdk8eI0MPidScnRYERN4hEz.json', 'var_call_2gSQiwrP5YQSHAAa3V3d8Vha': 'file_storage/call_2gSQiwrP5YQSHAAa3V3d8Vha.json', 'var_call_xx327ibXZCtlav0t6mwzRYZH': 'file_storage/call_xx327ibXZCtlav0t6mwzRYZH.json'}

exec(code, env_args)
