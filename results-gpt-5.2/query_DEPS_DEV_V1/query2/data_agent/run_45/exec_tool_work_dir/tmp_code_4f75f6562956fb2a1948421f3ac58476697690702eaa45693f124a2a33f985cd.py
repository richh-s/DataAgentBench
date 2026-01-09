code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        import pathlib
        p = pathlib.Path(x)
        return json.loads(p.read_text())
    return x

pkg = load_records(var_call_V0FsEZyqPz5RkafIQfZL3hzL)
mapr = load_records(var_call_GCg4FZMDsoKlN7J5JhmpiVuQ)
projinfo = load_records(var_call_uXaLChyCTltJaKPSkaJajT3K)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
map_df = pd.DataFrame(mapr)[['System','Name','Version','ProjectName']].drop_duplicates()

merged = pkg_df.merge(map_df, on=['System','Name','Version'], how='inner')
projects = merged[['ProjectName']].drop_duplicates()

# parse fork count from Project_Information text
rows=[]
pat = re.compile(r"The project\s+(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+).*?\s(?P<forks>[0-9,]+)\s+forks", re.IGNORECASE)
for rec in projinfo:
    text = rec.get('Project_Information')
    if not text:
        continue
    m = pat.search(text)
    if not m:
        continue
    repo = m.group('repo')
    forks = int(m.group('forks').replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks, 'Project_Information': text})

info_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

cand = projects.merge(info_df[['ProjectName','Forks']], on='ProjectName', how='inner')
# aggregate by project (in case multiple versions)
out = cand.groupby('ProjectName', as_index=False)['Forks'].max()
out = out.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_V0FsEZyqPz5RkafIQfZL3hzL': 'file_storage/call_V0FsEZyqPz5RkafIQfZL3hzL.json', 'var_call_GCg4FZMDsoKlN7J5JhmpiVuQ': 'file_storage/call_GCg4FZMDsoKlN7J5JhmpiVuQ.json', 'var_call_uXaLChyCTltJaKPSkaJajT3K': 'file_storage/call_uXaLChyCTltJaKPSkaJajT3K.json'}

exec(code, env_args)
