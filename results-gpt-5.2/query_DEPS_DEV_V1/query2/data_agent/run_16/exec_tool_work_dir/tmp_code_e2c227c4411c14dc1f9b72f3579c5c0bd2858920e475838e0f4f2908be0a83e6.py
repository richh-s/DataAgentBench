code = """import json, re, pandas as pd

pkg_src = var_call_TBfq6ui6ABPZ2vL1bhHZ2JOP
ppv_src = var_call_Ao0yp5FJgzJMtORaKQaK339d
pi_src  = var_call_9KCIw2aOU5bguHeDcerBoBJO

def load(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load(pkg_src)
ppv = load(ppv_src)
pi  = load(pi_src)

df_pkg = pd.DataFrame(pkg)
df_ppv = pd.DataFrame(ppv)

# normalize column names (some DBs may differ)
for df in (df_pkg, df_ppv):
    df.columns = [str(c) for c in df.columns]

needed_pkg = ['System','Name','Version']
needed_ppv = ['System','Name','Version','ProjectName']

if not all(c in df_pkg.columns for c in needed_pkg):
    raise Exception('package columns missing: ' + str(df_pkg.columns.tolist()[:20]))
if not all(c in df_ppv.columns for c in needed_ppv):
    raise Exception('ppv columns missing: ' + str(df_ppv.columns.tolist()[:20]))

m = df_pkg[needed_pkg].merge(df_ppv[needed_ppv], on=['System','Name','Version'], how='inner')

fork_re = re.compile(r'\b(\d[\d,]*)\s+forks\b', re.IGNORECASE)
name_res = [
    re.compile(r'\bproject\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b'),
    re.compile(r'\bon\s+GitHub\s+under\s+the\s+name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b'),
    re.compile(r'\bnamed\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b'),
    re.compile(r'\bunder\s+the\s+name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')
]

def extract_owner_repo(s):
    if not isinstance(s, str):
        return None
    for rr in name_res:
        mm = rr.search(s)
        if mm:
            return mm.group(1)
    return None

def extract_forks(s):
    if not isinstance(s, str):
        return None
    mm = fork_re.search(s)
    if not mm:
        return None
    return int(mm.group(1).replace(',',''))

pi_rows = []
for rec in pi:
    s = rec.get('Project_Information')
    owner_repo = extract_owner_repo(s)
    forks = extract_forks(s)
    if owner_repo and forks is not None:
        pi_rows.append({'ProjectName': owner_repo, 'Forks': forks})

df_metrics = pd.DataFrame(pi_rows)
if not df_metrics.empty:
    df_metrics = df_metrics.drop_duplicates(subset=['ProjectName'])
else:
    df_metrics = pd.DataFrame(columns=['ProjectName','Forks'])

m2 = m[['ProjectName']].drop_duplicates().merge(df_metrics, on='ProjectName', how='inner')

m2 = m2.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out_lines = []
for i, row in enumerate(m2.to_dict(orient='records'), start=1):
    out_lines.append(str(i) + '. ' + row.get('ProjectName','') + ' — ' + str(int(row.get('Forks',0))) + ' forks')

result = chr(10).join(out_lines)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TBfq6ui6ABPZ2vL1bhHZ2JOP': 'file_storage/call_TBfq6ui6ABPZ2vL1bhHZ2JOP.json', 'var_call_Ao0yp5FJgzJMtORaKQaK339d': 'file_storage/call_Ao0yp5FJgzJMtORaKQaK339d.json', 'var_call_9KCIw2aOU5bguHeDcerBoBJO': 'file_storage/call_9KCIw2aOU5bguHeDcerBoBJO.json'}

exec(code, env_args)
