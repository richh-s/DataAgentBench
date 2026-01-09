code = """import json, re, pandas as pd

# load large results
import os

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_ykXBLNcBiLmoFxVOgimI3Mds)
ppv = load_records(var_call_yb0ixQB7kFJdKOPNF7AMWDjz)
pi = load_records(var_call_RzTiRfnJK8epaUTOkSrljtV5)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']]
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']]

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
project_names = merged['ProjectName'].dropna().unique().tolist()

# parse project_info text to extract repo and forks
rows=[]
pat_repo = re.compile(r'project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
pat_forks = re.compile(r'(?:and\s+)?(\d{1,3}(?:,\d{3})*)\s+forks?')

for rec in pi:
    text = rec.get('Project_Information') or ''
    mrepo = pat_repo.search(text)
    mforks = pat_forks.search(text)
    if not mrepo or not mforks:
        continue
    repo = mrepo.group(1)
    forks = int(mforks.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': text})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

filtered = pi_df[pi_df['ProjectName'].isin(project_names)].copy()

top5 = filtered.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = top5[['ProjectName','Forks']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ykXBLNcBiLmoFxVOgimI3Mds': 'file_storage/call_ykXBLNcBiLmoFxVOgimI3Mds.json', 'var_call_yb0ixQB7kFJdKOPNF7AMWDjz': 'file_storage/call_yb0ixQB7kFJdKOPNF7AMWDjz.json', 'var_call_RzTiRfnJK8epaUTOkSrljtV5': 'file_storage/call_RzTiRfnJK8epaUTOkSrljtV5.json'}

exec(code, env_args)
