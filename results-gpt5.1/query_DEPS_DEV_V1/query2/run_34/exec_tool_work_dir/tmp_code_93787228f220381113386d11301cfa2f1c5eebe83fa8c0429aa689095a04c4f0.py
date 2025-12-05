code = """import json, re, pandas as pd

# Load large results from files
with open(var_call_fU0BrHKBpicGPQ6b8wV0GDVU, 'r') as f:
    npm_mit_release = json.load(f)
with open(var_call_pNwh98KS4YYTC2GcvgB7wHdN, 'r') as f:
    project_packageversion = json.load(f)
with open(var_call_a07Aro5c3Rz2uMdvPoUdccBX, 'r') as f:
    project_info = json.load(f)

# DataFrames
pkg_df = pd.DataFrame(npm_mit_release)
ppv_df = pd.DataFrame(project_packageversion)
info_df = pd.DataFrame(project_info)

# Join NPM MIT release packages with project_packageversion on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Extract GitHub owner/repo and fork count from Project_Information
pattern_repo = re.compile(r"project ([\w.-]+\/[\w.-]+)")
pattern_forks = re.compile(r"(\d+) forks")

repos = []
forks = []
for txt in info_df['Project_Information']:
    m_repo = pattern_repo.search(txt)
    m_forks = pattern_forks.search(txt)
    if m_repo and m_forks:
        repos.append(m_repo.group(1))
        forks.append(int(m_forks.group(1)))
    else:
        repos.append(None)
        forks.append(None)

info_df['ProjectName'] = repos
info_df['Forks'] = forks

# Drop rows without parsed data
info_df = info_df.dropna(subset=['ProjectName','Forks'])

# Join merged package-projects with project info on ProjectName
full = merged.merge(info_df[['ProjectName','Forks']], on='ProjectName', how='inner')

# Unique projects and their fork counts (max in case of duplicates)
proj_forks = full.groupby('ProjectName')['Forks'].max().reset_index()

# Top 5 by forks
top5 = proj_forks.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fU0BrHKBpicGPQ6b8wV0GDVU': 'file_storage/call_fU0BrHKBpicGPQ6b8wV0GDVU.json', 'var_call_pNwh98KS4YYTC2GcvgB7wHdN': 'file_storage/call_pNwh98KS4YYTC2GcvgB7wHdN.json', 'var_call_a07Aro5c3Rz2uMdvPoUdccBX': 'file_storage/call_a07Aro5c3Rz2uMdvPoUdccBX.json'}

exec(code, env_args)
