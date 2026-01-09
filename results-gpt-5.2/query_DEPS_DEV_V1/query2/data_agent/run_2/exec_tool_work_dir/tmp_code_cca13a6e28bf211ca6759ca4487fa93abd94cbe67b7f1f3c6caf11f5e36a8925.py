code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_UhK6pe9hlL1fp19JdWKEyPjA)
ppv = load_records(var_call_vDLjwe02tRtNTRD97CBbKFXD)
pi = load_records(var_call_r8otLQaM7dG2C490cB12N0cW)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna().drop_duplicates()

df = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
# unique projects among matched packages
projects = sorted(df['ProjectName'].dropna().unique().tolist())

# parse project_info text to extract project name and forks
pat = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?([0-9,]+)\s+forks?", re.IGNORECASE)
rows=[]
for rec in pi:
    s = rec.get('Project_Information')
    if not isinstance(s,str):
        continue
    m = pat.search(s)
    if not m:
        continue
    name = m.group(1)
    forks = int(m.group(2).replace(',',''))
    rows.append((name, forks, s))

df_info = pd.DataFrame(rows, columns=['ProjectName','Forks','Project_Information']).drop_duplicates(subset=['ProjectName'])

matched = df_info[df_info['ProjectName'].isin(projects)].copy()
# top 5 by forks
matched = matched.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out = matched[['ProjectName','Forks']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UhK6pe9hlL1fp19JdWKEyPjA': 'file_storage/call_UhK6pe9hlL1fp19JdWKEyPjA.json', 'var_call_vDLjwe02tRtNTRD97CBbKFXD': 'file_storage/call_vDLjwe02tRtNTRD97CBbKFXD.json', 'var_call_r8otLQaM7dG2C490cB12N0cW': 'file_storage/call_r8otLQaM7dG2C490cB12N0cW.json'}

exec(code, env_args)
