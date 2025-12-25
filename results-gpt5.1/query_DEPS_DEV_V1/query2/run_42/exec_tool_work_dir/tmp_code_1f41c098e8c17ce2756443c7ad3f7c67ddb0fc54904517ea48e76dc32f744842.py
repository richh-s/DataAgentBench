code = """import json, re, pandas as pd

# Load full tables
with open(var_call_3edF84j6a1ztVmCN0xcGI6Pt, 'r') as f:
    npm_release = json.load(f)
with open(var_call_d2ufa6RPPkcUh1QkyuEJI9Qg, 'r') as f:
    project_info = json.load(f)
with open(var_call_YTudLivLxC7RXK0nOpqAhEkP, 'r') as f:
    proj_pkg = json.load(f)

npm_df = pd.DataFrame(npm_release)
projinfo_df = pd.DataFrame(project_info)
projpkg_df = pd.DataFrame(proj_pkg)

# Join NPM release packages with project_packageversion on System, Name, Version
merged = pd.merge(npm_df, projpkg_df, on=['System','Name','Version'], how='inner')

# Extract repo name and fork count from Project_Information text
pat = re.compile(r"The project ([^ ]+/[^ ]+) .*? (?:currently has|has|is .*? with).*? (?:[0-9,]+ stars, and ([0-9,]+) forks|([0-9,]+) forks)")

repos = []
for info in projinfo_df['Project_Information'].dropna():
    m = pat.search(info)
    if m:
        repo = m.group(1)
        forks = m.group(2) or m.group(3)
        forks = int(forks.replace(',', ''))
        repos.append({'ProjectName': repo, 'Forks': forks})

repos_df = pd.DataFrame(repos).drop_duplicates(subset=['ProjectName'])

# Map merged packages to repos with fork counts using ProjectName
merged2 = pd.merge(merged, repos_df, on='ProjectName', how='inner')

# For each project, we just care that there exists at least one matching package
result = merged2[['ProjectName','Forks']].drop_duplicates(subset=['ProjectName']).sort_values('Forks', ascending=False).head(5)

out = result.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3edF84j6a1ztVmCN0xcGI6Pt': 'file_storage/call_3edF84j6a1ztVmCN0xcGI6Pt.json', 'var_call_d2ufa6RPPkcUh1QkyuEJI9Qg': 'file_storage/call_d2ufa6RPPkcUh1QkyuEJI9Qg.json', 'var_call_aFs5pgGLU005Pj634FLvjH1c': {'npm_rows': 176998, 'proj_rows': 770}, 'var_call_YTudLivLxC7RXK0nOpqAhEkP': 'file_storage/call_YTudLivLxC7RXK0nOpqAhEkP.json'}

exec(code, env_args)
