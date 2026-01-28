code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        import os
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_ljCdmggjsLNypPlQrLNrN1RR)
ppv = load_records(var_call_XgQC6mDl9JCNzg0H5pwUCA7p)
pi = load_records(var_call_3hFEQyikHlyVM33qSZMtsGFB)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# join packages to project mapping on System, Name, Version
m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
# unique projects
projects = m[['ProjectName']].dropna().drop_duplicates()

# parse project_info string to extract owner/repo and forks
pat = re.compile(r"project\s+([^\s,]+/[^\s,]+).+?([0-9,]+)\s+forks?", re.IGNORECASE)
rows = []
for s in pi_df['Project_Information'].dropna().astype(str):
    mm = pat.search(s)
    if mm:
        proj = mm.group(1)
        forks = int(mm.group(2).replace(',',''))
        rows.append({'ProjectName': proj, 'Forks': forks, 'Project_Information': s})
pi_parsed = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

joined = projects.merge(pi_parsed[['ProjectName','Forks']], on='ProjectName', how='inner')

# sort and take top 5
out = joined.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ljCdmggjsLNypPlQrLNrN1RR': 'file_storage/call_ljCdmggjsLNypPlQrLNrN1RR.json', 'var_call_XgQC6mDl9JCNzg0H5pwUCA7p': 'file_storage/call_XgQC6mDl9JCNzg0H5pwUCA7p.json', 'var_call_3hFEQyikHlyVM33qSZMtsGFB': 'file_storage/call_3hFEQyikHlyVM33qSZMtsGFB.json'}

exec(code, env_args)
