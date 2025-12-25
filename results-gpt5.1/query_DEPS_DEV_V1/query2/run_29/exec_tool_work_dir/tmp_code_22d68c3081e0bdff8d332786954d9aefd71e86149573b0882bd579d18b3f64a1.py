code = """import json, re, pandas as pd

# Load large results from files
with open(var_call_vZuHGE5We7Bg5WZCiumJ7iFs, 'r') as f:
    pkg_release_mit = json.load(f)
with open(var_call_nEuo6S2r1FhZjDTjRNulVd6f, 'r') as f:
    proj_pkg = json.load(f)
with open(var_call_jLPQLkptfj0ZRxXWHN4y43Nv, 'r') as f:
    proj_info = json.load(f)

pkg_df = pd.DataFrame(pkg_release_mit)[['System','Name','Version']].drop_duplicates()
proj_pkg_df = pd.DataFrame(proj_pkg)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# We only need unique projects
projects = merged['ProjectName'].dropna().unique()

info_df = pd.DataFrame(proj_info)

# Extract project name and forks from Project_Information using regex
pattern = re.compile(r"project ([^\s/]+/[^\s]+).*? (?:has|and has|and currently has|currently has)[^,]*?,[^,]*? (?:and )?(\d+) forks", re.IGNORECASE)

records = []
for row in info_df['Project_Information']:
    m = pattern.search(row)
    if m:
        name = m.group(1)
        forks = int(m.group(2))
        if name in projects:
            records.append({'ProjectName': name, 'Forks': forks})

if not records:
    result = []
else:
    forks_df = pd.DataFrame(records).drop_duplicates().groupby('ProjectName', as_index=False)['Forks'].max()
    top5 = forks_df.sort_values('Forks', ascending=False).head(5)
    result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_vZuHGE5We7Bg5WZCiumJ7iFs': 'file_storage/call_vZuHGE5We7Bg5WZCiumJ7iFs.json', 'var_call_nEuo6S2r1FhZjDTjRNulVd6f': 'file_storage/call_nEuo6S2r1FhZjDTjRNulVd6f.json', 'var_call_jLPQLkptfj0ZRxXWHN4y43Nv': 'file_storage/call_jLPQLkptfj0ZRxXWHN4y43Nv.json'}

exec(code, env_args)
