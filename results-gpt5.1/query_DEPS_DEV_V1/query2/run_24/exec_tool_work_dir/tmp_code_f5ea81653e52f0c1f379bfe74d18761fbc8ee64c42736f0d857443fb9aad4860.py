code = """import json, re, pandas as pd

# Load full MIT NPM release package list
with open(var_call_rMIqyhTrZYLysVDyYbjyKasa, 'r') as f:
    mit_packages = json.load(f)

# Load project-package mapping with project info
with open(var_call_LDMuiowbymiiNWSFGFBgOL4I, 'r') as f:
    proj_map = json.load(f)

mit_df = pd.DataFrame(mit_packages)
proj_df = pd.DataFrame(proj_map)

# Join on System, Name, Version
merged = mit_df.merge(proj_df, on=['System','Name','Version'], how='inner')

# Extract fork count from Project_Information using regex like 'forks' or 'fork count'
pattern = re.compile(r'(?:forks count of|forks,|and)([^0-9]*)(?P<forks>[0-9]+)\s*forks?', re.IGNORECASE)

fork_counts = []
for info in merged['Project_Information']:
    m = re.search(r"forks count of (\d+)", info)
    if not m:
        m = re.search(r"(\d+) forks", info)
    if not m:
        m = re.search(r"(\d+) fork", info)
    forks = int(m.group(1)) if m else 0
    fork_counts.append(forks)

merged['Forks'] = fork_counts

# Aggregate by ProjectName to avoid duplicates across versions
agg = merged.groupby('ProjectName', as_index=False).agg({'Forks':'max'})

# Get top 5 by forks
 top5 = agg.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rMIqyhTrZYLysVDyYbjyKasa': 'file_storage/call_rMIqyhTrZYLysVDyYbjyKasa.json', 'var_call_KznPzLmgmC0MvCy5ZWeH1WVd': ['project_info', 'project_packageversion'], 'var_call_LDMuiowbymiiNWSFGFBgOL4I': 'file_storage/call_LDMuiowbymiiNWSFGFBgOL4I.json'}

exec(code, env_args)
