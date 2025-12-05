code = """import json, pandas as pd

# Load full results from files
with open(var_call_IdaBf5ZiflnR5fBKoranIEAM, 'r') as f:
    npm_packages = json.load(f)
with open(var_call_sZRURfzS7sKCTgIIp9WLE8hb, 'r') as f:
    project_pkg = json.load(f)
with open(var_call_gadv179HlKtfatnfq22ixkYi, 'r') as f:
    project_info = json.load(f)

# DataFrames
pkg_df = pd.DataFrame(npm_packages)
proj_pkg_df = pd.DataFrame(project_pkg)
proj_info_df = pd.DataFrame(project_info)

# Filter NPM packages with MIT license and IsRelease true
import ast

def has_mit(licenses_str):
    try:
        arr = ast.literal_eval(licenses_str) if isinstance(licenses_str, str) else []
        return any(str(x).upper() == 'MIT' for x in arr)
    except Exception:
        return False

def is_release(versioninfo_str):
    try:
        d = ast.literal_eval(versioninfo_str) if isinstance(versioninfo_str, str) else {}
        return bool(d.get('IsRelease'))
    except Exception:
        return False

pkg_df = pkg_df[pkg_df['Licenses'].apply(has_mit) & pkg_df['VersionInfo'].apply(is_release)]

# Join with project_packageversion on System, Name, Version
merged = pkg_df.merge(proj_pkg_df, on=['System','Name','Version'], how='inner')

# Now need fork counts from Project_Information text; first map ProjectName to its info row(s)

# Extract owner/repo and fork count from Project_Information string
import re

pattern = re.compile(r"project ([^\s]+/[^\s]+).*?forks?[, ]+count of ([0-9,]+)|project ([^\s]+/[^\s]+).*?([0-9,]+) forks", re.IGNORECASE)

fork_data = {}
for row in proj_info_df['Project_Information']:
    text = str(row)
    match = pattern.search(text)
    if match:
        if match.group(1) and match.group(2):
            repo = match.group(1)
            forks = match.group(2)
        else:
            repo = match.group(3)
            forks = match.group(4)
        try:
            forks_int = int(forks.replace(',', ''))
        except Exception:
            continue
        # keep max forks per repo if multiple
        fork_data[repo] = max(fork_data.get(repo, 0), forks_int)

fork_df = pd.DataFrame([{'ProjectName': k, 'Forks': v} for k,v in fork_data.items()])

# Join merged with fork_df on ProjectName
merged2 = merged.merge(fork_df, on='ProjectName', how='inner')

# Aggregate by ProjectName to get max fork count per project
proj_forks = merged2.groupby('ProjectName', as_index=False)['Forks'].max()

# Sort desc and pick top 5
top5 = proj_forks.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IdaBf5ZiflnR5fBKoranIEAM': 'file_storage/call_IdaBf5ZiflnR5fBKoranIEAM.json', 'var_call_agxIK8wBFndZ25ec6TASQopl': ['project_info', 'project_packageversion'], 'var_call_sZRURfzS7sKCTgIIp9WLE8hb': 'file_storage/call_sZRURfzS7sKCTgIIp9WLE8hb.json', 'var_call_gadv179HlKtfatnfq22ixkYi': 'file_storage/call_gadv179HlKtfatnfq22ixkYi.json'}

exec(code, env_args)
