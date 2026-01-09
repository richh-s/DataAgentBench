code = """import json, re, pandas as pd
from pathlib import Path

def load_records(v):
    if isinstance(v, str) and v.endswith('.json') and Path(v).exists():
        return json.load(open(v, 'r', encoding='utf-8'))
    return v

pkg = load_records(var_call_RFeEZaW2oXqmb1EeKXVe25Co)
ppv = load_records(var_call_Bry1i4B0XUmZNRLSBKUWHfzB)
pi = load_records(var_call_sd7vMmpaKOsJPfmlDSLPOWo0)

pkg_df = pd.DataFrame(pkg).drop_duplicates()
ppv_df = pd.DataFrame(ppv).drop_duplicates(subset=['System','Name','Version','ProjectName'])

# join pkg->project mappings
j = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# unique projects among eligible packages
projects = sorted(j['ProjectName'].dropna().unique().tolist())

# parse fork counts from project_info text
fork_re = re.compile(r'([0-9][0-9,]*)\s+forks?')
proj_re = re.compile(r'project\s+([^\s]+/[^\s]+)')

forks_by_project = {}
for rec in pi:
    s = rec.get('Project_Information')
    if not isinstance(s, str):
        continue
    mproj = proj_re.search(s)
    mfork = fork_re.search(s)
    if not (mproj and mfork):
        continue
    pname = mproj.group(1).strip().strip('.,')
    forks = int(mfork.group(1).replace(',',''))
    # keep max if duplicates
    if pname not in forks_by_project or forks > forks_by_project[pname]:
        forks_by_project[pname] = forks

rows = []
for p in projects:
    if p in forks_by_project:
        rows.append({'ProjectName': p, 'Forks': forks_by_project[p]})

out_df = pd.DataFrame(rows)
if len(out_df)==0:
    top5 = []
else:
    top5 = out_df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_RFeEZaW2oXqmb1EeKXVe25Co': 'file_storage/call_RFeEZaW2oXqmb1EeKXVe25Co.json', 'var_call_Bry1i4B0XUmZNRLSBKUWHfzB': 'file_storage/call_Bry1i4B0XUmZNRLSBKUWHfzB.json', 'var_call_sd7vMmpaKOsJPfmlDSLPOWo0': 'file_storage/call_sd7vMmpaKOsJPfmlDSLPOWo0.json'}

exec(code, env_args)
