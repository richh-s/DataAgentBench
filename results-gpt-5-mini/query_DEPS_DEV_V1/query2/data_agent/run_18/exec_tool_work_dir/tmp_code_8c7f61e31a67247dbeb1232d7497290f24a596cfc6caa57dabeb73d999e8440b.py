code = """import json
import re
import pandas as pd

# Load data from storage file paths
with open(var_call_gzcMwmKdqOLhapGIM61ZnhnK, 'r') as f:
    package_rows = json.load(f)
with open(var_call_vVkrkAzeJQB6ComjllVkzvv4, 'r') as f:
    project_package_rows = json.load(f)
with open(var_call_DNnE37F40mGema7rMgvPjvpZ, 'r') as f:
    project_info_rows = json.load(f)

pkg_df = pd.DataFrame(package_rows)
ppv_df = pd.DataFrame(project_package_rows)
pi_df = pd.DataFrame(project_info_rows)

# Ensure columns exist
for df, name in [(pkg_df, 'pkg_df'), (ppv_df, 'ppv_df'), (pi_df, 'pi_df')]:
    if df.empty:
        pass

# Merge package records with project_packageversion on System, Name, Version
merged = pd.merge(pkg_df, ppv_df, on=['System', 'Name', 'Version'], how='inner')

# Get unique project names from merged
merged = merged[merged['ProjectName'].notnull()]
merged['ProjectName_lc'] = merged['ProjectName'].str.lower()
unique_projects = merged[['ProjectName_lc']].drop_duplicates().reset_index(drop=True)

# Parse project_info to extract repo and forks
repos = []
for row in project_info_rows:
    info = row.get('Project_Information') or ''
    info_lc = info.lower()
    # find repo pattern owner/repo
    repo_match = re.search(r'([a-z0-9_.-]+\/[a-z0-9_.-]+)', info_lc)
    repo = repo_match.group(1) if repo_match else None
    # find forks number - look for 'forks' or 'forked' patterns
    forks = None
    m = re.search(r'(\d[\d,]*)\s*(?:forks|forked)', info_lc)
    if m:
        forks = int(m.group(1).replace(',', ''))
    else:
        m2 = re.search(r'forked\s*(\d[\d,]*)\s*times', info_lc)
        if m2:
            forks = int(m2.group(1).replace(',', ''))
    repos.append({'repo': repo, 'forks': forks, 'info': info})

repos_df = pd.DataFrame(repos)
repos_df = repos_df[repos_df['repo'].notnull()]

# Join unique_projects with repos_df on lowercased repo
unique_projects = unique_projects.merge(repos_df, left_on='ProjectName_lc', right_on='repo', how='left')

# Keep only those with forks not null
unique_projects = unique_projects[unique_projects['forks'].notnull()]

# Sort by forks desc and take top 5
top5 = unique_projects.sort_values('forks', ascending=False).head(5)

# Prepare result list
result = []
for _, r in top5.iterrows():
    result.append({'ProjectName': r['ProjectName_lc'], 'Forks': int(r['forks']), 'Project_Information': r['info']})

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_gzcMwmKdqOLhapGIM61ZnhnK': 'file_storage/call_gzcMwmKdqOLhapGIM61ZnhnK.json', 'var_call_vVkrkAzeJQB6ComjllVkzvv4': 'file_storage/call_vVkrkAzeJQB6ComjllVkzvv4.json', 'var_call_DNnE37F40mGema7rMgvPjvpZ': 'file_storage/call_DNnE37F40mGema7rMgvPjvpZ.json'}

exec(code, env_args)
