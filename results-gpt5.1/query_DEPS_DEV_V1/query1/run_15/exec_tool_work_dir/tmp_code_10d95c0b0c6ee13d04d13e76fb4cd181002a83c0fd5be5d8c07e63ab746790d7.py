code = """import json, re, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_34FFMFBpmJRPvES89jAS8WHm, 'r') as f:
    project_info = json.load(f)
with open(var_call_6FOoWAAf7zFMmS0GmvvcLkv5, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_DgFB5HuJFc0alAqBC22hlqcx, 'r') as f:
    pkginfo = json.load(f)

# DataFrames
pi_df = pd.DataFrame(project_info)
pp_df = pd.DataFrame(proj_pkg)
ki_df = pd.DataFrame(pkginfo)

# Keep only GitHub projects
pp_df = pp_df[pp_df['ProjectType'] == 'GITHUB']

# Determine latest release version per (System, Name) from packageinfo using VersionInfo Ordinal when IsRelease true
# Parse VersionInfo JSON-like
def parse_vi(s):
    try:
        return json.loads(s) if isinstance(s, str) else {}
    except Exception:
        return {}

vi = ki_df['VersionInfo'].apply(parse_vi)
ki_df = ki_df.join(pd.json_normalize(vi))

# Filter NPM and releases
ki_df = ki_df[(ki_df['System']=='NPM') & (ki_df['IsRelease']==True)]

# For each (Name), choose max Ordinal; tie-break with UpstreamPublishedAt
ki_df['Ordinal'] = pd.to_numeric(ki_df['Ordinal'], errors='coerce')
ki_df['UpstreamPublishedAt'] = pd.to_numeric(ki_df['UpstreamPublishedAt'], errors='coerce')
ki_df = ki_df.sort_values(['Name','Ordinal','UpstreamPublishedAt'], ascending=[True, False, False])
latest = ki_df.groupby('Name', as_index=False).first()[['Name','Version']]

# Join with project_packageversion on Name+Version (System NPM already in pp_df)
merged = pp_df.merge(latest, on=['Name','Version'])

# Now link to project_info via some key. project_info lacks explicit ProjectName, so we must extract owner/repo from text and match to ProjectName
# Extract repo from Project_Information pattern 'project owner/repo' or 'named owner/repo'
repo_pattern = re.compile(r"([\w.-]+/[\w.-]+)")

def extract_repo(text):
    if not isinstance(text, str):
        return None
    m = repo_pattern.search(text)
    return m.group(1) if m else None

pi_df['ProjectName'] = pi_df['Project_Information'].apply(extract_repo)

# Some rows may have multiple matches but regex takes first which should be owner/repo

# Parse stars from Project_Information: patterns like '38715 stars' or 'stars count of 3761'

star_pattern1 = re.compile(r"(\d[\d,]*)\s+stars")
star_pattern2 = re.compile(r"stars count of\s+(\d[\d,]*)")


def extract_stars(text):
    if not isinstance(text, str):
        return None
    m = star_pattern2.search(text)
    if m:
        return int(m.group(1).replace(',', ''))
    m = star_pattern1.search(text)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

pi_df['Stars'] = pi_df['Project_Information'].apply(extract_stars)

# Keep rows with repo and stars
pi_df_clean = pi_df.dropna(subset=['ProjectName','Stars'])

# Join merged package-version-project with project_info by ProjectName
full = merged.merge(pi_df_clean[['ProjectName','Stars']], on='ProjectName', how='inner')

# For each package Name, keep max Stars (project may appear multiple times)
full = full.sort_values(['Name','Stars'], ascending=[True, False])
full_top = full.groupby('Name', as_index=False).first()

# Top 5 by Stars
top5 = full_top.sort_values('Stars', ascending=False).head(5)[['Name','Version','Stars']]

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_34FFMFBpmJRPvES89jAS8WHm': 'file_storage/call_34FFMFBpmJRPvES89jAS8WHm.json', 'var_call_6FOoWAAf7zFMmS0GmvvcLkv5': 'file_storage/call_6FOoWAAf7zFMmS0GmvvcLkv5.json', 'var_call_DgFB5HuJFc0alAqBC22hlqcx': 'file_storage/call_DgFB5HuJFc0alAqBC22hlqcx.json'}

exec(code, env_args)
