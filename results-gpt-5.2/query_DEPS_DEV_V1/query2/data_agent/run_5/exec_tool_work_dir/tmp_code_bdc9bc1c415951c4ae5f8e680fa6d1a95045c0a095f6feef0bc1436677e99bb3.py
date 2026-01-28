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

# join package versions to github projects
j = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')

# unique projects that have at least one MIT+release npm package version
projects = j[['ProjectName']].drop_duplicates()

# parse fork count from Project_Information text
rows=[]
pat = re.compile(r"The project\s+([^\s]+/[^\s]+).*?\b(\d[\d,]*)\s+forks\b", re.IGNORECASE)
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m = pat.search(txt)
    if not m:
        continue
    pname = m.group(1).strip().rstrip('.').rstrip(',')
    forks = int(m.group(2).replace(',',''))
    rows.append({'ProjectName': pname, 'Forks': forks, 'Project_Information': txt})

df_pi = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

cand = projects.merge(df_pi[['ProjectName','Forks']], on='ProjectName', how='inner')

# some packages may map to same project; keep max forks per project
cand = cand.groupby('ProjectName', as_index=False)['Forks'].max()

top5 = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3m97wNj3g9Tlg0iI8J6uh9Sj': 'file_storage/call_3m97wNj3g9Tlg0iI8J6uh9Sj.json', 'var_call_RrHlFOGiwW9wQ211KgUC4uao': 'file_storage/call_RrHlFOGiwW9wQ211KgUC4uao.json', 'var_call_ShNXjAyIbgDoMMm5y2fYcdJF': 'file_storage/call_ShNXjAyIbgDoMMm5y2fYcdJF.json'}

exec(code, env_args)
