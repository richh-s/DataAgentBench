code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_maybe_path(var_call_8b335bbpXsVdAyNahva9YHt1)
ppv = load_maybe_path(var_call_dmcrBtFAHtTIiosCUJBsopaU)
pi = load_maybe_path(var_call_l1AGsZwYwGm674XbWsH9Obxu)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = merged[['ProjectName']].drop_duplicates()

# Parse fork counts from Project_Information text
rows = []
pat1 = re.compile(r"project\s+([^\s]+/[^\s]+).*?([0-9][0-9,]*)\s+forks", re.IGNORECASE)
pat2 = re.compile(r"named\s+([^\s]+/[^\s,]+).*?([0-9][0-9,]*)\s+forks", re.IGNORECASE)
for rec in pi:
    txt = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not txt:
        continue
    m = pat1.search(txt) or pat2.search(txt)
    if not m:
        continue
    proj = m.group(1).strip().rstrip('.')
    forks = int(m.group(2).replace(',',''))
    rows.append({'ProjectName': proj, 'Forks': forks, 'Project_Information': txt})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

final = projects.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='inner')
# top 5 by forks
out = final.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8b335bbpXsVdAyNahva9YHt1': 'file_storage/call_8b335bbpXsVdAyNahva9YHt1.json', 'var_call_dmcrBtFAHtTIiosCUJBsopaU': 'file_storage/call_dmcrBtFAHtTIiosCUJBsopaU.json', 'var_call_l1AGsZwYwGm674XbWsH9Obxu': 'file_storage/call_l1AGsZwYwGm674XbWsH9Obxu.json'}

exec(code, env_args)
