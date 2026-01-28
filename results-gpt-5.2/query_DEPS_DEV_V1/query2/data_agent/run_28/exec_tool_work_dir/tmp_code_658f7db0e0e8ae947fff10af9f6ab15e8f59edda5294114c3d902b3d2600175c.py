code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkgs = load_records(var_call_2gJTrmwa2mTi6H6Ix1pMg6FJ)
ppv = load_records(var_call_vrFYx4nMmtblsEz8zlnIuOBY)
pi = load_records(var_call_EqEv4ubUPaWyyZYquYO100Hi)

df_pkgs = pd.DataFrame(pkgs)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

df = df_pkgs.merge(df_ppv, on=['System','Name','Version'], how='inner')
# parse project_info text -> (ProjectName, forks)
rows=[]
pat = re.compile(r"project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).+?([0-9,]+)\s+fork", re.IGNORECASE)
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m = pat.search(txt)
    if not m:
        continue
    proj = m.group(1)
    forks = int(m.group(2).replace(',',''))
    rows.append((proj, forks))

df_info = pd.DataFrame(rows, columns=['ProjectName','Forks']).drop_duplicates(subset=['ProjectName'])

df2 = df.merge(df_info, on='ProjectName', how='inner')
# compute top 5 projects by forks
out = (df2[['ProjectName','Forks']]
       .drop_duplicates()
       .sort_values(['Forks','ProjectName'], ascending=[False, True])
       .head(5))
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2gJTrmwa2mTi6H6Ix1pMg6FJ': 'file_storage/call_2gJTrmwa2mTi6H6Ix1pMg6FJ.json', 'var_call_vrFYx4nMmtblsEz8zlnIuOBY': 'file_storage/call_vrFYx4nMmtblsEz8zlnIuOBY.json', 'var_call_EqEv4ubUPaWyyZYquYO100Hi': 'file_storage/call_EqEv4ubUPaWyyZYquYO100Hi.json'}

exec(code, env_args)
