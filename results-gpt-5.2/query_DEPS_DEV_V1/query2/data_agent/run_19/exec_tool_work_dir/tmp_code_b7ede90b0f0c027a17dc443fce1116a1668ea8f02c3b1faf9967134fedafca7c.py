code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_sq18f1POglqOaHQGljnNBxQk)
ppv = load_records(var_call_GZQr3iKF4A4WDOrsAI6AulUW)
pi = load_records(var_call_Kei07TSxZR175XfgA7olkwQ6)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

df = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
# unique projects
projects = sorted(df['ProjectName'].dropna().unique().tolist())

# parse Project_Information: extract owner/repo and forks
rows=[]
pat_repo = re.compile(r'\b([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)\b')
pat_forks = re.compile(r'\b([0-9][0-9,]*)\s+forks?\b', re.IGNORECASE)
for rec in pi:
    text = rec.get('Project_Information') or ''
    mrepo = pat_repo.search(text)
    mf = pat_forks.search(text)
    if not mrepo or not mf:
        continue
    repo = mrepo.group(1)
    forks = int(mf.group(1).replace(',',''))
    rows.append((repo, forks))

metrics = pd.DataFrame(rows, columns=['ProjectName','Forks']).drop_duplicates(subset=['ProjectName'])

sel = metrics[metrics['ProjectName'].isin(projects)].copy()
sel = sel.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out = sel.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sq18f1POglqOaHQGljnNBxQk': 'file_storage/call_sq18f1POglqOaHQGljnNBxQk.json', 'var_call_GZQr3iKF4A4WDOrsAI6AulUW': 'file_storage/call_GZQr3iKF4A4WDOrsAI6AulUW.json', 'var_call_Kei07TSxZR175XfgA7olkwQ6': 'file_storage/call_Kei07TSxZR175XfgA7olkwQ6.json'}

exec(code, env_args)
