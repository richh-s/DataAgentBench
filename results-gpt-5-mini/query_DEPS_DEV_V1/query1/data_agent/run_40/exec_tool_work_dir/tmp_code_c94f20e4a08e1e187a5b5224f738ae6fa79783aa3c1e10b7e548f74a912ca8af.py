code = """import json
import pandas as pd
import re

# Load results from previous tool calls. These variables contain file paths to JSON results.
with open(var_call_XdoTwD23hLmeCmzOUKHxvAYl, 'r') as f:
    pkg_latest = json.load(f)
with open(var_call_EnalKBWIhNc1lJ6D9Qq386xc, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_5Rg8Xubr7AHVkabgOO16tWVG, 'r') as f:
    proj_info = json.load(f)

df_pkg = pd.DataFrame(pkg_latest)
df_proj_pkg = pd.DataFrame(proj_pkg)
df_proj_info = pd.DataFrame(proj_info)

# Merge latest package releases with project_packageversion on System, Name, Version
merged = pd.merge(df_pkg, df_proj_pkg, on=["System", "Name", "Version"] , how='inner')

# We'll extract stars by matching ProjectName in Project_Information and parsing numbers
# Preprocess project_info Project_Information to a list of (ProjectNameCandidate, stars)
# For faster matching, create lowercase Project_Information
proj_info_records = []
for rec in proj_info:
    info = rec.get('Project_Information') or ''
    lic = rec.get('Licenses')
    desc = rec.get('Description')
    homepage = rec.get('Homepage')
    # attempt to extract stars
    stars = 0
    # patterns to find stars
    patterns = [r"([0-9][0-9,]+)\s+stars",
                r"stars count of\s+([0-9][0-9,]+)",
                r"a total of\s+([0-9][0-9,]+)\s+stars",
                r"has garnered significant attention, with a total of\s+([0-9][0-9,]+)\s+stars",
                r"has garnered a total of\s+([0-9][0-9,]+)\s+stars"]
    for pat in patterns:
        m = re.search(pat, info, flags=re.IGNORECASE)
        if m:
            num = m.group(1)
            stars = int(num.replace(',', ''))
            break
    # fallback: look for '\\d+' before 'stars'
    if stars == 0:
        m = re.search(r"([0-9]+)\s+stars", info, flags=re.IGNORECASE)
        if m:
            stars = int(m.group(1))
    proj_info_records.append({
        'Project_Information': info,
        'stars': stars
    })

# For each merged row, find matching project_info row(s) where ProjectName appears in Project_Information
results = []
for _, row in merged.iterrows():
    pkg_name = row['Name']
    pkg_version = row['Version']
    project_name = row['ProjectName']
    # find matches in proj_info_records
    matched_stars = []
    for rec in proj_info_records:
        if project_name and project_name in (rec['Project_Information'] or ''):
            matched_stars.append(rec['stars'])
    if matched_stars:
        stars = max(matched_stars)
    else:
        # try looser match: check if last part of project_name (repo) appears
        repo = project_name.split('/')[-1] if isinstance(project_name, str) and '/' in project_name else None
        loose_matches = []
        if repo:
            for rec in proj_info_records:
                if repo and repo in (rec['Project_Information'] or ''):
                    loose_matches.append(rec['stars'])
        if loose_matches:
            stars = max(loose_matches)
        else:
            stars = 0
    results.append({
        'Name': pkg_name,
        'Version': pkg_version,
        'ProjectName': project_name,
        'Stars': int(stars)
    })

# For packages that map to multiple projects (multiple rows), keep the max stars per package
df_results = pd.DataFrame(results)
if df_results.empty:
    top5 = []
else:
    agg = df_results.groupby(['Name', 'Version'], as_index=False).agg({'Stars': 'max', 'ProjectName': lambda x: ','.join(sorted(set(x.dropna())))})
    agg_sorted = agg.sort_values(by='Stars', ascending=False)
    top5 = agg_sorted.head(5).to_dict(orient='records')

import json
print("__RESULT__:")
print(json.dumps(top5, ensure_ascii=False))"""

env_args = {'var_call_Wd2fS4to8xRg9DAwY8BpOKnu': ['packageinfo'], 'var_call_fxEDVVrsoesPF5TQxqRx8EeD': ['project_info', 'project_packageversion'], 'var_call_XdoTwD23hLmeCmzOUKHxvAYl': 'file_storage/call_XdoTwD23hLmeCmzOUKHxvAYl.json', 'var_call_EnalKBWIhNc1lJ6D9Qq386xc': 'file_storage/call_EnalKBWIhNc1lJ6D9Qq386xc.json', 'var_call_5Rg8Xubr7AHVkabgOO16tWVG': 'file_storage/call_5Rg8Xubr7AHVkabgOO16tWVG.json'}

exec(code, env_args)
