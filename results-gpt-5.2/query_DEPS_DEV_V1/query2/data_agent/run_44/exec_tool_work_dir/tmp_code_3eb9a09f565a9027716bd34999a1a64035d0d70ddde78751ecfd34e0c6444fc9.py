code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pkg = load_records(var_call_0rwJ8TmI3zzRLhG7TPjd10K3)
ppv = load_records(var_call_wKgJ2ATXLvpDGiPaLLaWp73K)
pi = load_records(var_call_KhiNhowDxhPSQQ2B5a2ilu7m)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

rows = []
pat_repo = re.compile(r"project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_forks = re.compile(r"\b([0-9][0-9,]*)\s+forks?\b")
for rec in pi:
    txt = rec.get('Project_Information') or ''
    mr = pat_repo.search(txt)
    mf = pat_forks.search(txt)
    if mr and mf:
        repo = mr.group(1)
        forks = int(mf.group(1).replace(',',''))
        rows.append({'ProjectName': repo, 'Forks': forks})

pi_df = pd.DataFrame(rows)
if not pi_df.empty:
    pi_df = pi_df.drop_duplicates(subset=['ProjectName'])

mf2 = m.merge(pi_df, on='ProjectName', how='inner') if not pi_df.empty else m.assign(Forks=pd.NA).iloc[0:0]

proj_max = mf2.groupby('ProjectName', as_index=False).agg(Forks=('Forks','max'))
proj_max = proj_max.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out = proj_max.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0rwJ8TmI3zzRLhG7TPjd10K3': 'file_storage/call_0rwJ8TmI3zzRLhG7TPjd10K3.json', 'var_call_wKgJ2ATXLvpDGiPaLLaWp73K': 'file_storage/call_wKgJ2ATXLvpDGiPaLLaWp73K.json', 'var_call_KhiNhowDxhPSQQ2B5a2ilu7m': 'file_storage/call_KhiNhowDxhPSQQ2B5a2ilu7m.json'}

exec(code, env_args)
