code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_Q8VX25UGhCBNv0SxO9lF6e6p, 'r') as f:
    npm_mit_release = json.load(f)
with open(var_call_S1luylOHGyzZ8YypfQlKQRHx, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_x8i6XYIKkzzJJly9AS2Kakjn, 'r') as f:
    proj_info = json.load(f)

# DataFrames
pkg_df = pd.DataFrame(npm_mit_release)  # System, Name, Version
pp_df = pd.DataFrame(proj_pkg)          # System, Name, Version, ProjectName
pi_df = pd.DataFrame(proj_info)         # Project_Information

# Extract ProjectName (owner/repo) and fork count from Project_Information
owner_repo = []
forks = []
for row in pi_df['Project_Information']:
    text = row
    m_repo = re.search(r"project ([-\w\.]+/[-\w\.]+)|named ([-\w\.]+/[-\w\.]+)|under the name ([-\w\.]+/[-\w\.]+)", text)
    repo = None
    if m_repo:
        repo = next(g for g in m_repo.groups() if g)
    m_fork = re.search(r"(\d+) forks", text)
    fork_cnt = int(m_fork.group(1)) if m_fork else None
    owner_repo.append(repo)
    forks.append(fork_cnt)

pi_df['ProjectName'] = owner_repo
pi_df['Forks'] = forks

# Join packages with project_packageversion on System, Name, Version
merged = pkg_df.merge(pp_df, on=['System','Name','Version'], how='inner')

# Deduplicate project names (a project may have multiple package versions); keep one row per project
merged_unique = merged[['ProjectName']].drop_duplicates()

# Join with project_info-derived forks
final = merged_unique.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='left')

# Drop projects without fork info
final = final.dropna(subset=['Forks'])

# Get top 5 by forks
top5 = final.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

from json import dumps
print("__RESULT__:")
print(dumps(result))"""

env_args = {'var_call_Q8VX25UGhCBNv0SxO9lF6e6p': 'file_storage/call_Q8VX25UGhCBNv0SxO9lF6e6p.json', 'var_call_S1luylOHGyzZ8YypfQlKQRHx': 'file_storage/call_S1luylOHGyzZ8YypfQlKQRHx.json', 'var_call_x8i6XYIKkzzJJly9AS2Kakjn': 'file_storage/call_x8i6XYIKkzzJJly9AS2Kakjn.json'}

exec(code, env_args)
