code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_3m97wNj3g9Tlg0iI8J6uh9Sj)
ppv = load_records(var_call_RrHlFOGiwW9wQ211KgUC4uao)
pi = load_records(var_call_ShNXjAyIbgDoMMm5y2fYcdJF)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

j = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
projects = set(j['ProjectName'].dropna().unique().tolist())

pat = re.compile(r"The project\s+([^\s]+/[^\s]+).*?\b(\d[\d,]*)\s+forks\b", re.IGNORECASE)
rows=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m = pat.search(txt)
    if not m:
        continue
    pname = m.group(1).strip().rstrip('.').rstrip(',')
    forks = int(m.group(2).replace(',',''))
    if pname in projects:
        rows.append({'ProjectName': pname, 'Forks': forks})

df = pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    df = df.groupby('ProjectName', as_index=False)['Forks'].max()
    df = df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    out = df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3m97wNj3g9Tlg0iI8J6uh9Sj': 'file_storage/call_3m97wNj3g9Tlg0iI8J6uh9Sj.json', 'var_call_RrHlFOGiwW9wQ211KgUC4uao': 'file_storage/call_RrHlFOGiwW9wQ211KgUC4uao.json', 'var_call_ShNXjAyIbgDoMMm5y2fYcdJF': 'file_storage/call_ShNXjAyIbgDoMMm5y2fYcdJF.json'}

exec(code, env_args)
