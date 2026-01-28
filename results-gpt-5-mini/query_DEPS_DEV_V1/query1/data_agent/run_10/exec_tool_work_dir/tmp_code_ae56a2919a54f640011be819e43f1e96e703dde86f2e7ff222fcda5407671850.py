code = """import json
import pandas as pd
import re

# Load data from storage variables (could be file paths or direct lists)
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

pkg_latest = load_var(var_call_rM3ozB2CBCGHbR9kJ5IwgnpD)
ppv = load_var(var_call_m386EwnYYJVHBcLDiEWAgK5a)
pinfo = load_var(var_call_Jm8ovCr7acBFaBDmybQFdnQb)

# Create dataframes
df_latest = pd.DataFrame(pkg_latest)
# keep only relevant columns and drop duplicates by Name (in case multiple identical rows)
df_latest = df_latest[['System','Name','Version','UpstreamPublishedAt']].drop_duplicates()

df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']]
# filter NPM just in case
df_ppv = df_ppv[df_ppv['System']=='NPM']

# Merge to get ProjectName for latest versions
df_merged = pd.merge(df_latest, df_ppv, on=['System','Name','Version'], how='inner')

# Build mapping from project path (owner/repo) -> stars by parsing project_info
proj_stars = {}
star_re = re.compile(r"([\d,]+)\s+stars", re.IGNORECASE)
path_re = re.compile(r"([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)")
for rec in pinfo:
    info = rec.get('Project_Information') or ''
    if not info or not isinstance(info, str):
        continue
    # find path
    path_match = path_re.search(info)
    if not path_match:
        continue
    path = path_match.group(1)
    # find stars
    star_match = star_re.search(info)
    if star_match:
        stars = int(star_match.group(1).replace(',',''))
    else:
        # no explicit stars found -> 0
        stars = 0
    # store the largest stars if duplicates
    if path in proj_stars:
        proj_stars[path] = max(proj_stars[path], stars)
    else:
        proj_stars[path] = stars

# For merged rows, map ProjectName to stars; if multiple rows per package, keep max stars
rows = []
for _, r in df_merged.iterrows():
    name = r['Name']
    version = r['Version']
    project = r['ProjectName']
    stars = proj_stars.get(project)
    if stars is None:
        # try case-insensitive lookup or partial match
        stars = 0
        for k,v in proj_stars.items():
            if k.lower() == project.lower():
                stars = v
                break
    rows.append({'Name': name, 'Version': version, 'ProjectName': project, 'Stars': int(stars)})

if not rows:
    result = []
else:
    df_final = pd.DataFrame(rows)
    # If multiple entries per package (shouldn't), take max stars
    df_final = df_final.groupby(['Name','Version','ProjectName'], as_index=False).agg({'Stars':'max'})
    # Now get top 5 by Stars
    df_top = df_final.sort_values('Stars', ascending=False).head(5)
    result = df_top[['Name','Version','Stars','ProjectName']].to_dict(orient='records')

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rM3ozB2CBCGHbR9kJ5IwgnpD': 'file_storage/call_rM3ozB2CBCGHbR9kJ5IwgnpD.json', 'var_call_m386EwnYYJVHBcLDiEWAgK5a': 'file_storage/call_m386EwnYYJVHBcLDiEWAgK5a.json', 'var_call_Jm8ovCr7acBFaBDmybQFdnQb': 'file_storage/call_Jm8ovCr7acBFaBDmybQFdnQb.json'}

exec(code, env_args)
