code = """import json, re
import pandas as pd

# Load MIT+release NPM package versions
pkg_src = var_call_QejXgWQZ3rwqiAMEKqeI0SiE
if isinstance(pkg_src, str):
    with open(pkg_src, 'r', encoding='utf-8') as f:
        pkg = json.load(f)
else:
    pkg = pkg_src

ppv_src = var_call_kZfWyEm6MckJmyWnziOsSZJF
if isinstance(ppv_src, str):
    with open(ppv_src, 'r', encoding='utf-8') as f:
        ppv = json.load(f)
else:
    ppv = ppv_src

pi_src = var_call_zyWFxtGeEqFBmz6u0cN45XxD
if isinstance(pi_src, str):
    with open(pi_src, 'r', encoding='utf-8') as f:
        pi = json.load(f)
else:
    pi = pi_src

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].dropna()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna()

# Join to get GitHub project for MIT+release package versions
joined = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Unique projects
projects = joined['ProjectName'].dropna().drop_duplicates().tolist()

# Parse fork counts from project_info.Project_Information strings
fork_re = re.compile(r'(?P<forks>[0-9][0-9,]*)\s+forks?\b', re.IGNORECASE)
# Extract owner/repo from strings like: "The project owner/repo ..."
repo_re = re.compile(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')

fork_map = {}
for rec in pi:
    s = rec.get('Project_Information')
    if not s:
        continue
    mrepo = repo_re.search(s)
    mfork = fork_re.search(s)
    if not (mrepo and mfork):
        continue
    repo = mrepo.group(1)
    forks = int(mfork.group('forks').replace(',',''))
    # keep max if duplicates
    if repo not in fork_map or forks > fork_map[repo]:
        fork_map[repo] = forks

proj_df = pd.DataFrame({'ProjectName': projects})
proj_df['Forks'] = proj_df['ProjectName'].map(fork_map)
proj_df = proj_df.dropna(subset=['Forks'])
proj_df['Forks'] = proj_df['Forks'].astype(int)

# For output, select top 5 projects by forks
out = proj_df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QejXgWQZ3rwqiAMEKqeI0SiE': 'file_storage/call_QejXgWQZ3rwqiAMEKqeI0SiE.json', 'var_call_kZfWyEm6MckJmyWnziOsSZJF': 'file_storage/call_kZfWyEm6MckJmyWnziOsSZJF.json', 'var_call_zyWFxtGeEqFBmz6u0cN45XxD': 'file_storage/call_zyWFxtGeEqFBmz6u0cN45XxD.json'}

exec(code, env_args)
