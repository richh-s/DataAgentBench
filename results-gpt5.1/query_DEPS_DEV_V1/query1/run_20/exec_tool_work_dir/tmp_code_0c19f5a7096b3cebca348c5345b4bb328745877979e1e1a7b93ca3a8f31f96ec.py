code = """import json, re, pandas as pd

# Load full NPM package list
with open(var_call_vc3ZNB4lGj1qBAMaGgqqhpRt, 'r') as f:
    npm_pkgs = json.load(f)

# Load full project_packageversion
with open(var_call_I9CwfGcsslPptuEmsSWc6Ae8, 'r') as f:
    proj_pkg = json.load(f)

# Load full project_info
with open(var_call_U8ISmtnzdoJJ1KPQ2vxqtIus, 'r') as f:
    proj_info = json.load(f)

npm_df = pd.DataFrame(npm_pkgs)[['System','Name','Version']].drop_duplicates()
pp_df = pd.DataFrame(proj_pkg)[['System','Name','Version','ProjectName']].drop_duplicates()

# Determine latest version per (System, Name) based on UpstreamPublishedAt would be ideal but not available here, so approximate via max Version lexicographically.
# Join to restrict to NPM packages present in project_packageversion
merged = pd.merge(npm_df, pp_df, on=['System','Name','Version'], how='inner')

# latest version per package name within NPM where we have a project mapping
merged['Version_sort'] = merged['Version'].astype(str)
latest = merged.sort_values('Version_sort').groupby(['System','Name'], as_index=False).tail(1)

pi_df = pd.DataFrame(proj_info)

# Extract repo name, stars from Project_Information text
repo_re = re.compile(r"project ([^\s]+/[^\s]+)")
stars_re = re.compile(r"(\d[\d,]*) stars")

def parse_info(text):
    repo = None
    m = repo_re.search(text)
    if m:
        repo = m.group(1)
    stars = None
    m2 = stars_re.search(text)
    if m2:
        stars = int(m2.group(1).replace(',', ''))
    return repo, stars

pi_df['repo'], pi_df['stars'] = zip(*pi_df['Project_Information'].map(parse_info))

# Join latest packages to project_info via ProjectName == repo
latest = latest.rename(columns={'ProjectName':'repo'})
full = pd.merge(latest, pi_df[['repo','stars']], on='repo', how='left')

# Filter to those with stars not null
full = full.dropna(subset=['stars'])

# Get top 5 by stars
top5 = full.sort_values('stars', ascending=False).head(5)[['Name','Version','stars']]

result = top5.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_vc3ZNB4lGj1qBAMaGgqqhpRt': 'file_storage/call_vc3ZNB4lGj1qBAMaGgqqhpRt.json', 'var_call_huyVsrU6Mf7CtoGdPD2CwRiw': ['project_info', 'project_packageversion'], 'var_call_I9CwfGcsslPptuEmsSWc6Ae8': 'file_storage/call_I9CwfGcsslPptuEmsSWc6Ae8.json', 'var_call_U8ISmtnzdoJJ1KPQ2vxqtIus': 'file_storage/call_U8ISmtnzdoJJ1KPQ2vxqtIus.json'}

exec(code, env_args)
