code = """import json, pandas as pd, re

# load dataframes from previous steps
path_latest = var_call_k7fTG0DADa9BlcxEkolQSVLZ
with open(path_latest) as f:
    latest = pd.DataFrame(json.load(f))

path_pkgproj = var_call_MaFRQXk2ytbZgVdx1cnXHz1b
with open(path_pkgproj) as f:
    pkgproj = pd.DataFrame(json.load(f))

path_projinfo = var_call_dx7zPprI8MH25z5NsKaz4Ewh
with open(path_projinfo) as f:
    projinfo = pd.DataFrame(json.load(f))

# filter to latest versions only
latest_pkgproj = pkgproj.merge(latest, on=['System','Name','Version'], how='inner')

# parse stars from Project_Information
star_re = re.compile(r"has(?: garnered)?(?: an open issues count of \d+,)?(?: a total of)? ?([0-9,]+) stars|stars count of ([0-9,]+)|has received ([0-9,]+) stars|currently has ([0-9,]+) stars")

def extract_stars(text):
    if not isinstance(text, str):
        return None
    m = star_re.search(text)
    if not m:
        return None
    for g in m.groups():
        if g:
            return int(g.replace(',', ''))
    return None

projinfo['Stars'] = projinfo['Project_Information'].apply(extract_stars)

# Project_Information also includes repo name in form 'owner/repo'
name_re = re.compile(r"project ([-\w\.]+/[-\w\.]+) |")

# simpler: extract first occurrence of pattern like word/word
repo_re = re.compile(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

def extract_repo(text):
    if not isinstance(text, str):
        return None
    m = repo_re.search(text)
    return m.group(1) if m else None

projinfo['ProjectName'] = projinfo['Project_Information'].apply(extract_repo)

# merge latest package->project with project info on ProjectName
merged = latest_pkgproj.merge(projinfo[['ProjectName','Stars']], on='ProjectName', how='left')

# drop rows without star info
merged = merged.dropna(subset=['Stars'])

# for each package (Name), we want its GitHub project's stars; there might be multiple projects, take max stars per package latest version
agg = merged.groupby(['Name','Version']).agg({'Stars':'max'}).reset_index()

# get top 5 by stars
top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dPgVOSdxo3BEWb3C9qHFSwGZ': 'file_storage/call_dPgVOSdxo3BEWb3C9qHFSwGZ.json', 'var_call_zcurF4o6Wv4G3zX2pC4DFbCU': ['project_info', 'project_packageversion'], 'var_call_MaFRQXk2ytbZgVdx1cnXHz1b': 'file_storage/call_MaFRQXk2ytbZgVdx1cnXHz1b.json', 'var_call_k7fTG0DADa9BlcxEkolQSVLZ': 'file_storage/call_k7fTG0DADa9BlcxEkolQSVLZ.json', 'var_call_R822j2kfu6cketct0h5qXRU5': {'count_latest': 16614, 'count_mapped': 31822}, 'var_call_dx7zPprI8MH25z5NsKaz4Ewh': 'file_storage/call_dx7zPprI8MH25z5NsKaz4Ewh.json'}

exec(code, env_args)
