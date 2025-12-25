code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_fyNJFBxNt3ixTQtoEZcsZwM2, 'r') as f:
    npm_packages = json.load(f)
with open(var_call_5YlA6ghvtXNN7cscZQkw8efa, 'r') as f:
    project_pkg = json.load(f)
with open(var_call_Ue52u6vzSE2q9m7TVLR27CtG, 'r') as f:
    project_info = json.load(f)

# Filter NPM packages: MIT license and IsRelease true
pkg_df = pd.DataFrame(npm_packages)

def has_mit(lic_str):
    try:
        arr = json.loads(lic_str)
    except Exception:
        return False
    return any(isinstance(x, str) and x.upper() == 'MIT' for x in arr)

def is_release(vinfo_str):
    try:
        obj = json.loads(vinfo_str)
    except Exception:
        return False
    return bool(obj.get('IsRelease'))

pkg_df = pkg_df[pkg_df['Licenses'].apply(has_mit) & pkg_df['VersionInfo'].apply(is_release)]

# Join with project_packageversion on System, Name, Version
pp_df = pd.DataFrame(project_pkg)
merged = pkg_df.merge(pp_df, on=['System','Name','Version'], how='inner')

# Extract project name and forks from project_info text
pi_df = pd.DataFrame(project_info)

proj_records = []
for row in pi_df['Project_Information']:
    text = row
    # project name
    m_name = re.search(r"project (?:is hosted on GitHub under the name |is a GitHub repository named |is hosted on GitHub and currently has|is hosted on GitHub under the name |on GitHub, named |named |on GitHub is|on GitHub currently has|on GitHub has|on GitHub currently)", text)
    # Simpler: capture owner/repo before ' on GitHub' or ' is hosted on GitHub'
    m = re.search(r"project ([^ ]+/[^ ]+) on GitHub", text)
    if not m:
        m = re.search(r"named ([^ ]+/[^ ]+)", text)
    if not m:
        m = re.search(r"under the name ([^ ]+/[^ ]+)", text)
    if not m:
        continue
    name = m.group(1).strip(',')
    # forks count
    m_forks = re.search(r"(\d+) forks", text)
    if not m_forks:
        continue
    forks = int(m_forks.group(1))
    proj_records.append({'ProjectName': name, 'Forks': forks})

proj_df = pd.DataFrame(proj_records).drop_duplicates(subset=['ProjectName'])

# Map merged packages to project forks
merged2 = merged.merge(proj_df, on='ProjectName', how='inner')

# Among all such packages, group by project and take max forks (forks is per project, so just unique)
proj_rank = merged2[['ProjectName','Forks']].drop_duplicates().sort_values('Forks', ascending=False).head(5)

result = proj_rank.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fyNJFBxNt3ixTQtoEZcsZwM2': 'file_storage/call_fyNJFBxNt3ixTQtoEZcsZwM2.json', 'var_call_5YlA6ghvtXNN7cscZQkw8efa': 'file_storage/call_5YlA6ghvtXNN7cscZQkw8efa.json', 'var_call_Ue52u6vzSE2q9m7TVLR27CtG': 'file_storage/call_Ue52u6vzSE2q9m7TVLR27CtG.json'}

exec(code, env_args)
