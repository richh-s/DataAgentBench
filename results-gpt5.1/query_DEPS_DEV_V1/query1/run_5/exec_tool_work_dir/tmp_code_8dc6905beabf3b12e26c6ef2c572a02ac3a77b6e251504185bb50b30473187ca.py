code = """import json, re, pandas as pd

# Load subset: to reduce, read limited rows via chunks-like approach not available, so sample from files
with open(var_call_reQe3voOFXCGwHsgeXKqqOGp, 'r') as f:
    npm_pkg = json.load(f)
with open(var_call_pp27ENnx8w5BB21HQKUh5NIQ, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_hdWiOu7sZx2YSo53HBsZeiTF, 'r') as f:
    proj_info = json.load(f)

pkg_df = pd.DataFrame(npm_pkg)[['System','Name','Version','VersionInfo']]
proj_pkg_df = pd.DataFrame(proj_pkg)
proj_info_df = pd.DataFrame(proj_info)

# Filter early to shrink size
pkg_df = pkg_df[pkg_df['System']=='NPM']
proj_pkg_df = proj_pkg_df[(proj_pkg_df['System']=='NPM') & (proj_pkg_df['ProjectType']=='GITHUB') & (proj_pkg_df['RelationType']=='SOURCE_REPO_TYPE')]

import ast

def parse_vi(x):
    try:
        d = ast.literal_eval(x) if isinstance(x,str) else (x or {})
        return d.get('Ordinal'), d.get('IsRelease')
    except Exception:
        return None, None

pkg_df[['Ordinal','IsRelease']] = pkg_df['VersionInfo'].apply(lambda x: pd.Series(parse_vi(x)))
rel = pkg_df[pkg_df['IsRelease']==True].copy()
rel.sort_values(['Name','Ordinal'], ascending=[True,False], inplace=True)
latest_rel = rel.drop_duplicates(subset=['Name'], keep='first')

merged = latest_rel.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

repo_pat = re.compile(r"project ([\w.-]+/[\w.-]+)")
stars_pat = re.compile(r"(\d+[\d,]*) stars")

def extract_repo(info):
    if not isinstance(info,str):
        return None
    m = repo_pat.search(info)
    return m.group(1) if m else None

def extract_stars(info):
    if not isinstance(info,str):
        return None
    m = stars_pat.search(info)
    if not m:
        return None
    s = m.group(1).replace(',','')
    try:
        return int(s)
    except ValueError:
        return None

proj_info_df['Repo'] = proj_info_df['Project_Information'].apply(extract_repo)
proj_info_df['Stars'] = proj_info_df['Project_Information'].apply(extract_stars)

merged2 = merged.merge(proj_info_df[['Repo','Stars']], left_on='ProjectName', right_on='Repo', how='left')
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()
agg = agg.dropna(subset=['Stars'])
agg.sort_values('Stars', ascending=False, inplace=True)
result = agg.head(5).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_reQe3voOFXCGwHsgeXKqqOGp': 'file_storage/call_reQe3voOFXCGwHsgeXKqqOGp.json', 'var_call_J8h2UwIxWqaqMc9EYAsW82ES': ['project_info', 'project_packageversion'], 'var_call_pp27ENnx8w5BB21HQKUh5NIQ': 'file_storage/call_pp27ENnx8w5BB21HQKUh5NIQ.json', 'var_call_hdWiOu7sZx2YSo53HBsZeiTF': 'file_storage/call_hdWiOu7sZx2YSo53HBsZeiTF.json'}

exec(code, env_args)
