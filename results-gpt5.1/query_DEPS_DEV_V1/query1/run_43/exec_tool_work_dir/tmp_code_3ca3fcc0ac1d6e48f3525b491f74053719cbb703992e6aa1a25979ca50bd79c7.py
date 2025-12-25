code = """import json, pandas as pd, re

# Load merged latest package-projectname mapping
path_latest = var_call_Vj8gQoT9Zvr9F8epqn57WUgv
with open(path_latest, 'r') as f:
    latest_pkg_proj = json.load(f)
latest_df = pd.DataFrame(latest_pkg_proj)

# Load project_info
path_pinfo = var_call_qHMPZs3KTUwsOFWyf6wAv2tF
with open(path_pinfo, 'r') as f:
    pinfo_rows = json.load(f)
pinfo_df = pd.DataFrame(pinfo_rows)

# Extract repo name (owner/repo) from Project_Information
repo_pattern = re.compile(r"project ([^\s/]+/[^\s]+)|named ([^\s/]+/[^\s]+)|under the name ([^\s/]+/[^\s]+)")
star_pattern = re.compile(r"(\d[\d,]*) stars")

repos = []
stars = []
for info in pinfo_df['Project_Information']:
    m = repo_pattern.search(info)
    repo = None
    if m:
        for g in m.groups():
            if g:
                repo = g
                break
    repos.append(repo)
    sm = star_pattern.search(info)
    s = None
    if sm:
        s = int(sm.group(1).replace(',', ''))
    stars.append(s)

pinfo_df['ProjectName'] = repos
pinfo_df['Stars'] = stars

# Drop rows without repo
pinfo_df = pinfo_df.dropna(subset=['ProjectName','Stars'])

# Join latest_df with pinfo_df on ProjectName
merged = latest_df.merge(pinfo_df[['ProjectName','Stars']], on='ProjectName', how='inner')

# For each package (Name), we already have latest version; now pick top 5 by Stars
top5 = merged.sort_values('Stars', ascending=False).head(5)

result = top5[['Name','Version','Stars']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Os96Ro0WCvduiy8cpOCYMkJg': 'file_storage/call_Os96Ro0WCvduiy8cpOCYMkJg.json', 'var_call_8wuGEJO8RIudYTua4TW33fxX': 'file_storage/call_8wuGEJO8RIudYTua4TW33fxX.json', 'var_call_qHMPZs3KTUwsOFWyf6wAv2tF': 'file_storage/call_qHMPZs3KTUwsOFWyf6wAv2tF.json', 'var_call_Vj8gQoT9Zvr9F8epqn57WUgv': 'file_storage/call_Vj8gQoT9Zvr9F8epqn57WUgv.json'}

exec(code, env_args)
