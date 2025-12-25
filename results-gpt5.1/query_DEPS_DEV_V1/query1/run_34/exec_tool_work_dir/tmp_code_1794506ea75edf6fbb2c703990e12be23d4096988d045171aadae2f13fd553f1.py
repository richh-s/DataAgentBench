code = """import json, pandas as pd, re, os

# load latest NPM versions
with open(var_call_5C8goQSsQBuL9wjncoZGq8jz, 'r') as f:
    latest = pd.read_json(f)

# load project_packageversion
with open(var_call_6MH4txoAxXmQTzSWwtlanqCC, 'r') as f:
    ppv = pd.DataFrame(json.load(f))

# join latest with ppv to get ProjectName
merged = latest.merge(ppv, on=['System','Name','Version'], how='inner')

# extract repo name and stars from project_info text
with open(var_call_cF2ipZH1o4gptIVvlOpHTZdP, 'r') as f:
    pi = pd.DataFrame(json.load(f))

repos = []
stars = []
for text in pi['Project_Information']:
    m_repo = re.search(r"project ([\w.-]+/[\w.-]+)", text)
    m_stars = re.search(r"(\d[\d,]*) stars", text)
    if m_repo and m_stars:
        repos.append(m_repo.group(1))
        stars.append(int(m_stars.group(1).replace(',', '')))

repo_star = pd.DataFrame({'ProjectName': repos, 'Stars': stars}).drop_duplicates('ProjectName')

full = merged.merge(repo_star, on='ProjectName', how='inner')

# for each package Name, keep max Stars
idx = full.groupby('Name')['Stars'].idxmax()
per_pkg = full.loc[idx, ['Name','Version','Stars']]

# top 5 by Stars
top5 = per_pkg.sort_values('Stars', ascending=False).head(5)
result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_LXWPZszMZItiAcI1by9sxnXM': ['project_info', 'project_packageversion'], 'var_call_UQC9GPlj5T53scmjbbAAC5hL': 'file_storage/call_UQC9GPlj5T53scmjbbAAC5hL.json', 'var_call_5C8goQSsQBuL9wjncoZGq8jz': 'file_storage/call_5C8goQSsQBuL9wjncoZGq8jz.json', 'var_call_6MH4txoAxXmQTzSWwtlanqCC': 'file_storage/call_6MH4txoAxXmQTzSWwtlanqCC.json', 'var_call_cF2ipZH1o4gptIVvlOpHTZdP': 'file_storage/call_cF2ipZH1o4gptIVvlOpHTZdP.json'}

exec(code, env_args)
