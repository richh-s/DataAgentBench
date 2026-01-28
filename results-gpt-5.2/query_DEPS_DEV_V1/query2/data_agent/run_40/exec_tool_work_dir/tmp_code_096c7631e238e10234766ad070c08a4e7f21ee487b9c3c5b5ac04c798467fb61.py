code = """import json, re, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_maybe_path(var_call_ZE9KN9DOlI7j7zVOCa3r3FqT)
ppv = load_maybe_path(var_call_ww7i2MXMtA5uvgeQwPLi9f81)
pi = load_maybe_path(var_call_FhD4S8krAStrLmiGyy7r2oUI)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna().drop_duplicates()

df = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
proj_names = set(df['ProjectName'].astype(str))

fork_re = re.compile(r"\b([0-9][0-9,]*)\s+forks\b", re.IGNORECASE)
name_re = re.compile(r"\bproject\s+([^\s]+/[^\s]+)")

rows = []
for rec in pi:
    text = rec.get('Project_Information')
    if not isinstance(text, str):
        continue
    mname = name_re.search(text)
    if not mname:
        continue
    pname = mname.group(1).rstrip('.,;')
    if pname not in proj_names:
        continue
    mf = fork_re.search(text)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',', ''))
    rows.append({'ProjectName': pname, 'Forks': forks})

df_f = pd.DataFrame(rows)
if len(df_f)==0:
    result = []
else:
    df_f = df_f.drop_duplicates(subset=['ProjectName'])
    top5 = df_f.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    result = top5.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZE9KN9DOlI7j7zVOCa3r3FqT': 'file_storage/call_ZE9KN9DOlI7j7zVOCa3r3FqT.json', 'var_call_ww7i2MXMtA5uvgeQwPLi9f81': 'file_storage/call_ww7i2MXMtA5uvgeQwPLi9f81.json', 'var_call_FhD4S8krAStrLmiGyy7r2oUI': 'file_storage/call_FhD4S8krAStrLmiGyy7r2oUI.json'}

exec(code, env_args)
