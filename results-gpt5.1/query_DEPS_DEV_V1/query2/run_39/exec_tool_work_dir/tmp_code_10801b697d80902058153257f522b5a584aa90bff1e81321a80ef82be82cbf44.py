code = """import json, re, pandas as pd

with open(var_call_uftyPqYc1gi2yOLindNNkhPJ, 'r') as f:
    packageinfo = json.load(f)
with open(var_call_FLgVZuWzRVn5Bmob9mPxxi5T, 'r') as f:
    project_package = json.load(f)
with open(var_call_PFuJZsCp94u4I1i3fQBocBjm, 'r') as f:
    project_info = json.load(f)

pkg_df = pd.DataFrame(packageinfo)
proj_pkg_df = pd.DataFrame(project_package)
proj_info_df = pd.DataFrame(project_info)

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease') if isinstance(x, str) else None)
pkg_df['HasMIT'] = pkg_df['Licenses'].apply(lambda x: 'MIT' in json.loads(x) if isinstance(x, str) and x.strip() else False)

filtered_pkg = pkg_df[(pkg_df['IsRelease'] == True) & (pkg_df['HasMIT'])][['System','Name','Version']]

merged = filtered_pkg.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# Extract project name and forks from Project_Information
pattern = re.compile(r"project ([^\s/]+/[^\s]+).*?forks? count of (\d+)|project ([^\s/]+/[^\s]+).*? (\d+) forks|named ([^\s/]+/[^\s]+).*? (\d+) forks|under the name ([^\s/]+/[^\s]+).*? (\d+) forks", re.IGNORECASE)

def extract_name_forks(text):
    m = pattern.search(text)
    if not m:
        return None, None
    groups = m.groups()
    # Try to find repo and forks among captured groups
    repo = None
    forks = None
    for i, g in enumerate(groups):
        if g is None:
            continue
        if '/' in g and repo is None:
            repo = g
        elif g.isdigit() and forks is None:
            forks = int(g)
    return repo, forks

proj_info_df['Repo'], proj_info_df['Forks'] = zip(*proj_info_df['Project_Information'].map(extract_name_forks))

proj_info_df = proj_info_df.dropna(subset=['Repo','Forks'])

merged2 = merged.merge(proj_info_df[['Repo','Forks']], left_on='ProjectName', right_on='Repo', how='inner')

# For each project, take max forks (they should be same per repo)
proj_forks = merged2.groupby('ProjectName')['Forks'].max().reset_index()

top5 = proj_forks.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uftyPqYc1gi2yOLindNNkhPJ': 'file_storage/call_uftyPqYc1gi2yOLindNNkhPJ.json', 'var_call_FLgVZuWzRVn5Bmob9mPxxi5T': 'file_storage/call_FLgVZuWzRVn5Bmob9mPxxi5T.json', 'var_call_PFuJZsCp94u4I1i3fQBocBjm': 'file_storage/call_PFuJZsCp94u4I1i3fQBocBjm.json'}

exec(code, env_args)
