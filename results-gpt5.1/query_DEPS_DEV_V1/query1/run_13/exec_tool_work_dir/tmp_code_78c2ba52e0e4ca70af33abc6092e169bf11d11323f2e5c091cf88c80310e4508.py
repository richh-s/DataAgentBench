code = """import json, re, pandas as pd, os

# Load latest NPM packages
path_latest = var_call_PkJ3hOod9EiIKSsALs0pM3dP
with open(path_latest, 'r') as f:
    latest_pkgs = json.load(f)
latest_df = pd.DataFrame(latest_pkgs)

# Load NPM project-package mappings
path_proj_pkg = var_call_1n32ekisfd9So9lyi46cJH5j
with open(path_proj_pkg, 'r') as f:
    proj_pkg = json.load(f)
proj_pkg_df = pd.DataFrame(proj_pkg)

# Keep only mappings for latest versions by merging on System, Name, Version
merged = pd.merge(latest_df, proj_pkg_df, on=['System','Name','Version'], how='inner')

# Extract repo and star count from Project_Information text
path_proj_info = var_call_L278KyoLiIt7VdQOcHZkFtVO
with open(path_proj_info, 'r') as f:
    proj_info = json.load(f)
proj_info_df = pd.DataFrame(proj_info)

# Regex to capture `owner/repo` and `<number> stars`
repo_re = re.compile(r"project ([\w.-]+/[\w.-]+)")
stars_re = re.compile(r"(\d+) stars")

repos = []
stars = []
for info in proj_info_df['Project_Information']:
    m_repo = repo_re.search(info)
    m_stars = stars_re.search(info)
    if m_repo and m_stars:
        repos.append(m_repo.group(1))
        stars.append(int(m_stars.group(1)))
    else:
        repos.append(None)
        stars.append(None)

proj_info_df['ProjectName'] = repos
proj_info_df['Stars'] = stars

# Join with merged on ProjectName
full = pd.merge(merged, proj_info_df[['ProjectName','Stars']], on='ProjectName', how='left')

# For each package Name, keep max Stars (some packages may map to same repo or multiple? use max)
pkg_stars = full.groupby(['Name']).agg({'Stars':'max', 'Version':'first'}).reset_index()

# Get top 5 by Stars
top5 = pkg_stars.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IaPCtaNdkDCd1NLG8PLWOOeb': 'file_storage/call_IaPCtaNdkDCd1NLG8PLWOOeb.json', 'var_call_ombGlHUWTJ5HLFCdkGbhraJs': ['project_info', 'project_packageversion'], 'var_call_1n32ekisfd9So9lyi46cJH5j': 'file_storage/call_1n32ekisfd9So9lyi46cJH5j.json', 'var_call_PkJ3hOod9EiIKSsALs0pM3dP': 'file_storage/call_PkJ3hOod9EiIKSsALs0pM3dP.json', 'var_call_L278KyoLiIt7VdQOcHZkFtVO': 'file_storage/call_L278KyoLiIt7VdQOcHZkFtVO.json'}

exec(code, env_args)
