code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_uMuAXnZrLIwJEk1TK7TLVVcR)
ppv = load_records(var_call_bjHDaVWEtjs3UTSvtkjniksW)
pi = load_records(var_call_iOf5lzF0Iat0tfqX3kWa2bZT)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = merged[['ProjectName']].drop_duplicates()

# Parse project_info strings to extract owner/repo and fork count
rows=[]
pat_repo = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_repo2 = re.compile(r"named\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
pat_forks = re.compile(r"([0-9,]+)\s+forks?", re.IGNORECASE)
for rec in pi:
    s = rec.get('Project_Information') or ''
    m = pat_repo.search(s) or pat_repo2.search(s)
    if not m:
        continue
    repo = m.group(1)
    mf = pat_forks.search(s)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks})

pi_df = pd.DataFrame(rows).drop_duplicates('ProjectName')

top = projects.merge(pi_df, on='ProjectName', how='inner')
# In case multiple packages map to same project, keep max forks per project
agg = top.groupby('ProjectName', as_index=False)['Forks'].max()
agg = agg.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = agg.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Z9c6PjYcGPXMLcwb4TqaSVbx': ['packageinfo'], 'var_call_e8wQtkqcPaoCBQZBsFJndMco': ['project_info', 'project_packageversion'], 'var_call_uMuAXnZrLIwJEk1TK7TLVVcR': 'file_storage/call_uMuAXnZrLIwJEk1TK7TLVVcR.json', 'var_call_bjHDaVWEtjs3UTSvtkjniksW': 'file_storage/call_bjHDaVWEtjs3UTSvtkjniksW.json', 'var_call_iOf5lzF0Iat0tfqX3kWa2bZT': 'file_storage/call_iOf5lzF0Iat0tfqX3kWa2bZT.json'}

exec(code, env_args)
