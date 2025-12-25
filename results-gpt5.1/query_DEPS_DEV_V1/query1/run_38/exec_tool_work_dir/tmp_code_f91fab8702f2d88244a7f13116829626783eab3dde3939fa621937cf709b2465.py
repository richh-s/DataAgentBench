code = """import json, pandas as pd, re

# Load full results from files
with open(var_call_WRLhzQCyFYyvVDQSm7tEkJM0, 'r') as f:
    npm_pkgs = json.load(f)
with open(var_call_dvI9yc7PknXFT5wQN9GcFFBp, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_98IyLgVcIf89HTD3Y4D209mG, 'r') as f:
    proj_info = json.load(f)

npm_pkgs_df = pd.DataFrame(npm_pkgs)[['Name','Version']].drop_duplicates()
proj_pkg_df = pd.DataFrame(proj_pkg)[['Name','Version','ProjectName']].drop_duplicates()

# Keep only package versions that have a mapped project
merged = pd.merge(npm_pkgs_df, proj_pkg_df, on=['Name','Version'])

# For each Name, keep the latest Version using packageinfo row order as proxy (assuming UpstreamPublishedAt not required here)
# Since npm_pkgs_df came from full table without order guarantee, instead compute latest by lexical sort of Version per Name as best-effort.
merged['Version_sort'] = merged['Version'].astype(str)
merged_latest = merged.sort_values(['Name','Version_sort']).groupby('Name', as_index=False).tail(1)

# Parse Project_Information to extract repo and star count
pi_df = pd.DataFrame(proj_info)

repos = []
stars = []
for info in pi_df['Project_Information']:
    m_repo = re.search(r"project ([\w.-]+/[\w.-]+)", info)
    repo = m_repo.group(1) if m_repo else None
    m_star = re.search(r"(\d[\d,]*) stars", info)
    star = int(m_star.group(1).replace(',', '')) if m_star else None
    repos.append(repo)
    stars.append(star)

pi_df['ProjectName'] = repos
pi_df['Stars'] = stars

# Join latest package versions to project info via ProjectName
latest_with_repo = pd.merge(merged_latest, pi_df[['ProjectName','Stars']], on='ProjectName', how='left')

# Drop rows without star info
latest_with_repo = latest_with_repo.dropna(subset=['Stars'])

# Rank by Stars and take top 5
latest_with_repo = latest_with_repo.sort_values('Stars', ascending=False)
result_df = latest_with_repo[['Name','Version','ProjectName','Stars']].drop_duplicates(subset=['Name']).head(5)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_WRLhzQCyFYyvVDQSm7tEkJM0': 'file_storage/call_WRLhzQCyFYyvVDQSm7tEkJM0.json', 'var_call_6gD0DiXP3ciVLVAoTn6OG8aj': ['project_info', 'project_packageversion'], 'var_call_dvI9yc7PknXFT5wQN9GcFFBp': 'file_storage/call_dvI9yc7PknXFT5wQN9GcFFBp.json', 'var_call_98IyLgVcIf89HTD3Y4D209mG': 'file_storage/call_98IyLgVcIf89HTD3Y4D209mG.json'}

exec(code, env_args)
