code = """import json, re, pandas as pd

pkg_src = var_call_f6UmnHm9tLgbcTWK5VBMfZzV
ppv_src = var_call_FZ9C0DUWeVO3ERu0JmBuDl5s
pi_src  = var_call_b4vxqe2IjkAeUso3a7dupFw3

def load_records(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load_records(pkg_src)
ppv = load_records(ppv_src)
pi  = load_records(pi_src)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = set(m['ProjectName'].dropna().drop_duplicates().tolist())

fork_re = re.compile(r'\b([0-9][0-9,]*)\s+forks\b')
proj_re = re.compile(r'\bproject\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', re.IGNORECASE)

rows = []
for rec in pi:
    text = rec.get('Project_Information')
    if not text:
        continue
    pm = proj_re.search(text)
    if not pm:
        continue
    pname = pm.group(1)
    if pname not in projects:
        continue
    fm = fork_re.search(text)
    if not fm:
        continue
    forks = int(fm.group(1).replace(',',''))
    rows.append((pname, forks))

if rows:
    fork_df = pd.DataFrame(rows, columns=['ProjectName','Forks'])
    fork_df = fork_df.groupby('ProjectName', as_index=False)['Forks'].max()
    out = fork_df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    result = out.to_dict(orient='records')
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_f6UmnHm9tLgbcTWK5VBMfZzV': 'file_storage/call_f6UmnHm9tLgbcTWK5VBMfZzV.json', 'var_call_FZ9C0DUWeVO3ERu0JmBuDl5s': 'file_storage/call_FZ9C0DUWeVO3ERu0JmBuDl5s.json', 'var_call_b4vxqe2IjkAeUso3a7dupFw3': 'file_storage/call_b4vxqe2IjkAeUso3a7dupFw3.json'}

exec(code, env_args)
