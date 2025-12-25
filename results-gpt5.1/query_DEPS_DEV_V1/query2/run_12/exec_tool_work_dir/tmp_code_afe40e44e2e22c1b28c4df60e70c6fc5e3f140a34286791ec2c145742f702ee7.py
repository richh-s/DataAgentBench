code = """import json, pandas as pd

# Load packageinfo result
file_path = var_call_NvL6eggWltcKIkWG7JOxyvX8
with open(file_path, 'r') as f:
    package_rows = json.load(f)

pkg_df = pd.DataFrame(package_rows)

# Load project_packageversion result
file_path2 = var_call_f5IEvN9xegl779N5iZngAYBO
with open(file_path2, 'r') as f:
    proj_pkg_rows = json.load(f)

proj_pkg_df = pd.DataFrame(proj_pkg_rows)

# Join on System, Name, Version
merged = pkg_df.merge(proj_pkg_df, on=['System', 'Name', 'Version'], how='inner')

# Extract project name from Project_Information text and fork count using simple parsing
file_path3 = var_call_1vhCtrjLwMAGrgGZHX95NaWu
with open(file_path3, 'r') as f:
    proj_info_rows = json.load(f)

info_df = pd.DataFrame(proj_info_rows)

# Function to parse repo and forks from the Project_Information string
import re

def parse_info(text):
    # Try to find owner/repo pattern
    m = re.search(r'project ([\w.-]+/[\w.-]+)', text)
    repo = m.group(1) if m else None
    # Try to find forks count like "123 forks"
    m2 = re.search(r'(\d[\d,]*) forks', text)
    forks = int(m2.group(1).replace(',', '')) if m2 else None
    return repo, forks

info_df['repo'], info_df['forks'] = zip(*info_df['Project_Information'].map(parse_info))

# Drop rows without repo or forks
info_df = info_df.dropna(subset=['repo', 'forks'])

# Now map ProjectName (owner/repo) to forks
forks_map = info_df.drop_duplicates('repo').set_index('repo')['forks']

merged['forks'] = merged['ProjectName'].map(forks_map)

# Drop rows without forks
merged = merged.dropna(subset=['forks'])

# Get top 5 projects by forks (unique ProjectName)
proj_forks = merged.groupby('ProjectName')['forks'].max().reset_index()

top5 = proj_forks.sort_values('forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NvL6eggWltcKIkWG7JOxyvX8': 'file_storage/call_NvL6eggWltcKIkWG7JOxyvX8.json', 'var_call_w4Lvdgu3BBFlJERHw0UnMHTx': ['project_info', 'project_packageversion'], 'var_call_f5IEvN9xegl779N5iZngAYBO': 'file_storage/call_f5IEvN9xegl779N5iZngAYBO.json', 'var_call_1vhCtrjLwMAGrgGZHX95NaWu': 'file_storage/call_1vhCtrjLwMAGrgGZHX95NaWu.json'}

exec(code, env_args)
