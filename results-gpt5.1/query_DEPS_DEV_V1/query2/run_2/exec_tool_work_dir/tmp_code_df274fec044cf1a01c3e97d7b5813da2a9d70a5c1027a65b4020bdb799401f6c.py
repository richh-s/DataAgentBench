code = """import json, pandas as pd

# Load full results from files
with open(var_call_D1UpwAMEpwjKsTlXwHcIBL24, 'r') as f:
    pkgs = json.load(f)
with open(var_call_B5XMGoZEPZjbD54VWhNxV3UG, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_YnZ2wiV46qCjl3gfCd0Ga6W6, 'r') as f:
    proj_info = json.load(f)

pkgs_df = pd.DataFrame(pkgs)[['System','Name','Version']].drop_duplicates()
proj_pkg_df = pd.DataFrame(proj_pkg)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkgs_df.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

pi_df = pd.DataFrame(proj_info)
# Extract project name and fork count from Project_Information
import re

names = []
forks = []
for txt in pi_df['Project_Information'].astype(str):
    m_name = re.search(r"project ([^\s/]+/[^\s]+)|name[d]? ([^\s/]+/[^\s,]+)", txt)
    if m_name:
        name = m_name.group(1) or m_name.group(2)
    else:
        name = None
    m_fork = re.search(r"(\d+) forks", txt)
    fork = int(m_fork.group(1)) if m_fork else None
    names.append(name)
    forks.append(fork)

pi_df['ProjectName'] = names
pi_df['Forks'] = forks

pi_df = pi_df.dropna(subset=['ProjectName','Forks']).drop_duplicates(subset=['ProjectName'])

joined = merged.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='inner')
# Among all such projects, 5 highest fork counts (unique by project)
proj_forks = joined[['ProjectName','Forks']].drop_duplicates().sort_values('Forks', ascending=False).head(5)

result = proj_forks.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_D1UpwAMEpwjKsTlXwHcIBL24': 'file_storage/call_D1UpwAMEpwjKsTlXwHcIBL24.json', 'var_call_kGo4VyU2L301NEQkUgKmIQ1v': ['project_info', 'project_packageversion'], 'var_call_B5XMGoZEPZjbD54VWhNxV3UG': 'file_storage/call_B5XMGoZEPZjbD54VWhNxV3UG.json', 'var_call_YnZ2wiV46qCjl3gfCd0Ga6W6': 'file_storage/call_YnZ2wiV46qCjl3gfCd0Ga6W6.json'}

exec(code, env_args)
