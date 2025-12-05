code = """import pandas as pd, json, re, os

# Load latest NPM package versions
file_latest = var_call_Rwkfoq0N8biVd5TunbP3EyKb
with open(file_latest, 'r') as f:
    latest_pkgs = json.load(f)
latest_df = pd.DataFrame(latest_pkgs)

# Load NPM project_packageversion
file_ppv = var_call_wVcuCjNnDqo8wehZKF0ZdTp6
with open(file_ppv, 'r') as f:
    ppv = json.load(f)
ppv_df = pd.DataFrame(ppv)

# Join latest NPM package versions with project_packageversion on System, Name, Version
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# We only care about GITHUB projects
merged = merged[merged['ProjectType'] == 'GITHUB']

# ProjectName is repo path; we'll match to project_info via that string being inside Project_Information

file_pinfo = var_call_siP8WXBH2VKuziRKdXl5RWxF
with open(file_pinfo, 'r') as f:
    pinfo = json.load(f)
pi_df = pd.DataFrame(pinfo)

# Extract repo "owner/repo" and stars from Project_Information using regex
repo_pattern = re.compile(r"project ([\w.-]+/[\w.-]+) on GitHub", re.IGNORECASE)
stars_pattern = re.compile(r"(\d[\d,]*) stars")

repos = []
stars = []
for text in pi_df['Project_Information'].astype(str):
    m_repo = repo_pattern.search(text)
    if not m_repo:
        # alternative phrasing: "named owner/repo" or "hosted on GitHub under the name owner/repo"
        m_repo = re.search(r"named ([\w.-]+/[\w.-]+)", text)
    if not m_repo:
        m_repo = re.search(r"under the name ([\w.-]+/[\w.-]+)", text)
    repo = m_repo.group(1) if m_repo else None
    m_stars = stars_pattern.search(text)
    star = int(m_stars.group(1).replace(',', '')) if m_stars else None
    repos.append(repo)
    stars.append(star)

pi_df['Repo'] = repos
pi_df['Stars'] = stars

pi_repos = pi_df.dropna(subset=['Repo', 'Stars'])[['Repo','Stars']]

# Join merged packages with repo stars
merged['Repo'] = merged['ProjectName']
merged2 = merged.merge(pi_repos, left_on='Repo', right_on='Repo', how='inner')

# Now compute for each package Name its star count (assuming single repo per Name/Version). Use Stars directly.

pkg_pop = merged2[['Name','Version','Stars']].drop_duplicates()

# Get top 5 by Stars
top5 = pkg_pop.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

import json as _json
out = _json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_n3hHVcOaNDEvIoNK6zRDhj1J': 'file_storage/call_n3hHVcOaNDEvIoNK6zRDhj1J.json', 'var_call_dld2sHB5YJisR0GdydadjFPq': ['project_info', 'project_packageversion'], 'var_call_wVcuCjNnDqo8wehZKF0ZdTp6': 'file_storage/call_wVcuCjNnDqo8wehZKF0ZdTp6.json', 'var_call_siP8WXBH2VKuziRKdXl5RWxF': 'file_storage/call_siP8WXBH2VKuziRKdXl5RWxF.json', 'var_call_Rwkfoq0N8biVd5TunbP3EyKb': 'file_storage/call_Rwkfoq0N8biVd5TunbP3EyKb.json'}

exec(code, env_args)
