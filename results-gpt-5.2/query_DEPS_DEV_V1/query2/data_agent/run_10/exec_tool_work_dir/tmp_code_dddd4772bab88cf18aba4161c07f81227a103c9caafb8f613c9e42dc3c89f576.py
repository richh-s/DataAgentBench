code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_Stm3WcxosxA0uLgXiDyIPt1e)
ppv = load_records(var_call_sdNF1u5qHYePKtzHQNQQ6inW)
pi = load_records(var_call_0UBcYlw9AHHZXUXZ2v3aQzew)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse project_info Project_Information to extract repo and forks
rows=[]
pat = re.compile(r"project\s+([^\s]+/[^\s]+)")
pat2 = re.compile(r"([0-9][0-9,]*)\s+forks?", re.IGNORECASE)
for rec in pi:
    s = rec.get('Project_Information') or ''
    mrepo = pat.search(s)
    mf = pat2.search(s)
    if mrepo and mf:
        repo = mrepo.group(1).strip().rstrip('.,')
        forks = int(mf.group(1).replace(',',''))
        rows.append((repo, forks, s))

pi_df = pd.DataFrame(rows, columns=['ProjectName','Forks','Project_Information']).drop_duplicates(subset=['ProjectName'])

merged2 = merged.merge(pi_df, on='ProjectName', how='inner')

# Many package versions can map to same project; take max forks per project
proj_max = merged2.groupby('ProjectName', as_index=False)['Forks'].max()
proj_top5 = proj_max.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = proj_top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Stm3WcxosxA0uLgXiDyIPt1e': 'file_storage/call_Stm3WcxosxA0uLgXiDyIPt1e.json', 'var_call_sdNF1u5qHYePKtzHQNQQ6inW': 'file_storage/call_sdNF1u5qHYePKtzHQNQQ6inW.json', 'var_call_0UBcYlw9AHHZXUXZ2v3aQzew': 'file_storage/call_0UBcYlw9AHHZXUXZ2v3aQzew.json'}

exec(code, env_args)
