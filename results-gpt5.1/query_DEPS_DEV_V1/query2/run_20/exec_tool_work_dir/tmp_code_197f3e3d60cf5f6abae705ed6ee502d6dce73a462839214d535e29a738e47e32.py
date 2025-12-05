code = """import json, re, pandas as pd

# Load full results from JSON files
with open(var_call_y0LBqYPm2rNCvmkSX1wO9EwJ, 'r') as f:
    npm_mit_release = json.load(f)
with open(var_call_gQmlhY617CeTBKHnj2y158bx, 'r') as f:
    project_pkg = json.load(f)
with open(var_call_zdbeL1pgUvMLIYUlvhgzmQAZ, 'r') as f:
    project_info = json.load(f)

# DataFrames
npm_df = pd.DataFrame(npm_mit_release)
proj_pkg_df = pd.DataFrame(project_pkg)
proj_info_df = pd.DataFrame(project_info)

# First join NPM MIT release packages with project_packageversion on System, Name, Version
merged = pd.merge(npm_df, proj_pkg_df, on=['System','Name','Version'], how='inner')

# We now have ProjectName for relevant package versions. Deduplicate by ProjectName
projects = merged[['ProjectName']].drop_duplicates().reset_index(drop=True)

# Parse Project_Information to extract project name and fork count using regex
name_pattern = re.compile(r"project ([^\s/]+/[^\s, ]+)")
forks_pattern = re.compile(r"(\d+) forks")

records = []
for row in proj_info_df.itertuples(index=False):
    info = row.Project_Information
    name_match = name_pattern.search(info)
    forks_match = forks_pattern.search(info)
    if not name_match or not forks_match:
        continue
    project_name = name_match.group(1)
    forks = int(forks_match.group(1))
    records.append({'ProjectName': project_name, 'Forks': forks})

proj_metrics_df = pd.DataFrame(records).drop_duplicates(subset=['ProjectName'])

# Join our relevant project list with metrics on ProjectName
final = pd.merge(projects, proj_metrics_df, on='ProjectName', how='inner')

# Get top 5 by Forks
Top5 = final.sort_values('Forks', ascending=False).head(5)

result = Top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_y0LBqYPm2rNCvmkSX1wO9EwJ': 'file_storage/call_y0LBqYPm2rNCvmkSX1wO9EwJ.json', 'var_call_gQmlhY617CeTBKHnj2y158bx': 'file_storage/call_gQmlhY617CeTBKHnj2y158bx.json', 'var_call_zdbeL1pgUvMLIYUlvhgzmQAZ': 'file_storage/call_zdbeL1pgUvMLIYUlvhgzmQAZ.json'}

exec(code, env_args)
