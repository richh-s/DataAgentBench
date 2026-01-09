code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_8hhuWewv6KNBIaS4DyquA8V3)
ppv = load_records(var_call_RXOyRsFxkixWIVVgL6w0BF5g)
pi = load_records(var_call_X6Kk3b5HblnhbO5EnQD9BM9K)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna().drop_duplicates()

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = merged[['ProjectName']].drop_duplicates()

# parse project_info into repo, forks
pat_repo = re.compile(r'project\s+([^\s,]+/[^\s,]+)', re.IGNORECASE)
pat_forks = re.compile(r'(?:and\s+)?(\d{1,3}(?:,\d{3})*)\s+forks', re.IGNORECASE)

rows=[]
for rec in pi:
    s = rec.get('Project_Information') or ''
    mrepo = pat_repo.search(s)
    mf = pat_forks.search(s)
    if not (mrepo and mf):
        continue
    repo = mrepo.group(1)
    forks = int(mf.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': s})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

proj = projects.merge(pi_df[['ProjectName','Forks']], on='ProjectName', how='inner')

# some packages may map to same project; ensure unique project ranking
ranked = proj.drop_duplicates(subset=['ProjectName']).sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = ranked.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8hhuWewv6KNBIaS4DyquA8V3': 'file_storage/call_8hhuWewv6KNBIaS4DyquA8V3.json', 'var_call_RXOyRsFxkixWIVVgL6w0BF5g': 'file_storage/call_RXOyRsFxkixWIVVgL6w0BF5g.json', 'var_call_X6Kk3b5HblnhbO5EnQD9BM9K': 'file_storage/call_X6Kk3b5HblnhbO5EnQD9BM9K.json'}

exec(code, env_args)
