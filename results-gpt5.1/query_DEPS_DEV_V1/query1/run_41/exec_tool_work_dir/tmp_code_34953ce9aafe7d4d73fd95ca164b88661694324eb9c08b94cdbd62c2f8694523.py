code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_25iXL5WNJaGx7PwfL64iPYVE, 'r') as f:
    packageinfo = json.load(f)
with open(var_call_ckGYBA853OEXIvZTukQClaTA, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_4n90QtXa2bPSdecMj7MDqZv5, 'r') as f:
    proj_info = json.load(f)

pkg_df = pd.DataFrame(packageinfo)[['System','Name','Version']]
# get latest version per (System, Name) by UpstreamPublishedAt if available; fallback to max Version lexicographically
# Reload packageinfo with UpstreamPublishedAt
pkg_full = pd.DataFrame(packageinfo)

if 'UpstreamPublishedAt' in pkg_full.columns:
    pkg_full['UpstreamPublishedAt'] = pd.to_numeric(pkg_full['UpstreamPublishedAt'], errors='coerce')
    pkg_full_sorted = pkg_full.sort_values(['System','Name','UpstreamPublishedAt','Version'], ascending=[True, True, True, True])
    latest_pkg = pkg_full_sorted.loc[pkg_full_sorted.groupby(['System','Name'])['UpstreamPublishedAt'].idxmax()][['System','Name','Version']]
else:
    latest_pkg = pkg_df.sort_values(['System','Name','Version']).groupby(['System','Name']).tail(1)

latest_pkg = latest_pkg[latest_pkg['System']=='NPM']

proj_pkg_df = pd.DataFrame(proj_pkg)
proj_pkg_df = proj_pkg_df[proj_pkg_df['System']=='NPM']

# join latest packages with project_packageversion on System, Name, Version
merged = latest_pkg.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

info_df = pd.DataFrame(proj_info)

# Extract owner/repo and stars from Project_Information
owner_repo_pattern = re.compile(r"project ([^/\s]+/[^\s]+)")
stars_pattern = re.compile(r"(\d[\d,]*) stars")

def parse_info(text):
    if not isinstance(text,str):
        return None, None
    m_repo = owner_repo_pattern.search(text)
    m_stars = stars_pattern.search(text)
    repo = m_repo.group(1) if m_repo else None
    stars = int(m_stars.group(1).replace(',','')) if m_stars else None
    return repo, stars

info_df[['ProjectName','Stars']] = info_df['Project_Information'].apply(lambda t: pd.Series(parse_info(t)))

# join merged with info_df on ProjectName
full = merged.merge(info_df[['ProjectName','Stars']], on='ProjectName', how='left')

# aggregate by package (System, Name) taking max Stars (some packages may map to multiple projects)
pkg_stars = full.groupby(['Name'])['Stars'].max().reset_index()

# drop missing stars
pkg_stars = pkg_stars.dropna(subset=['Stars'])

# get top 5 by stars
top5 = pkg_stars.sort_values('Stars', ascending=False).head(5)

# get versions for these packages from latest_pkg
top5_with_versions = top5.merge(latest_pkg[['Name','Version']], on='Name', how='left').drop_duplicates(subset=['Name'])

result = top5_with_versions.sort_values('Stars', ascending=False).to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_25iXL5WNJaGx7PwfL64iPYVE': 'file_storage/call_25iXL5WNJaGx7PwfL64iPYVE.json', 'var_call_ckGYBA853OEXIvZTukQClaTA': 'file_storage/call_ckGYBA853OEXIvZTukQClaTA.json', 'var_call_4n90QtXa2bPSdecMj7MDqZv5': 'file_storage/call_4n90QtXa2bPSdecMj7MDqZv5.json'}

exec(code, env_args)
