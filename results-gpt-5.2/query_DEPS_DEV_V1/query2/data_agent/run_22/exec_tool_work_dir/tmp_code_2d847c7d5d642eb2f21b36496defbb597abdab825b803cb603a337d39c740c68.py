code = """import json, re
import pandas as pd

def load(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_n52OU3KGj1iqhjytfZEpa1XI)
ppv = load(var_call_lYQSdxDxWq7gB1iOaZeljo8b)
pi = load(var_call_eAGdD1omrWjxZoM5urgkZC5M)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

joined = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
project_names = set(joined['ProjectName'].dropna().astype(str).str.strip())

# parse fork counts from Project_Information and map to project name
pat = re.compile(r"(?:The project|The GitHub project named|The GitHub project)\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?([0-9][0-9,]*)\s+fork", re.IGNORECASE)
rows = []
for rec in pi:
    s = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not s or not isinstance(s, str):
        continue
    m = pat.search(s)
    if not m:
        continue
    pname = m.group(1)
    forks = int(m.group(2).replace(',',''))
    rows.append((pname, forks))

fork_df = pd.DataFrame(rows, columns=['ProjectName','Forks'])
# keep max forks per project (in case of duplicates)
fork_df = fork_df.groupby('ProjectName', as_index=False)['Forks'].max()

cand = fork_df[fork_df['ProjectName'].isin(project_names)].copy()
# Top 5
cand = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = cand.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_n52OU3KGj1iqhjytfZEpa1XI': 'file_storage/call_n52OU3KGj1iqhjytfZEpa1XI.json', 'var_call_lYQSdxDxWq7gB1iOaZeljo8b': 'file_storage/call_lYQSdxDxWq7gB1iOaZeljo8b.json', 'var_call_eAGdD1omrWjxZoM5urgkZC5M': 'file_storage/call_eAGdD1omrWjxZoM5urgkZC5M.json'}

exec(code, env_args)
