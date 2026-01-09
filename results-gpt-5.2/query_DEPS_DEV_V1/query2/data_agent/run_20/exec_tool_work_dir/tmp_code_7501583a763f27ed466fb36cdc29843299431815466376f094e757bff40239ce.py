code = """import json, re, pandas as pd

# Load large results

def load_maybe_path(v):
    if isinstance(v, str):
        # file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_maybe_path(var_call_1tDXH57o54HBmkNb2iIQG2X5)
ppv = load_maybe_path(var_call_q8v7syzzEEZifdrqN9qjYfY1)
pi = load_maybe_path(var_call_YvUdKMdVnUfwPMwqdGUBaoAh)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

# join package versions to project names
m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# parse project_info Project_Information for repo and forks
rows=[]
pat_repo = re.compile(r'project\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
pat_forks = re.compile(r'(?:and\s+)?(\d[\d,]*)\s+forks')
for rec in pi:
    s = rec.get('Project_Information') or ''
    mrepo = pat_repo.search(s)
    mforks = pat_forks.search(s)
    if not mrepo or not mforks:
        continue
    repo = mrepo.group(1)
    forks = int(mforks.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

# attach forks to matched projects
m2 = m.merge(pi_df, on='ProjectName', how='inner')

# Some packages map to same project; rank by forks per project
proj = m2.groupby('ProjectName', as_index=False).agg(Forks=('Forks','max'))

# top 5
proj_top = proj.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

# also list example package names associated (optional); pick one
pkg_for_proj = m2.groupby('ProjectName', as_index=False).agg(Package=('Name','first'))
final = proj_top.merge(pkg_for_proj, on='ProjectName', how='left')[['ProjectName','Package','Forks']]

out = final.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1tDXH57o54HBmkNb2iIQG2X5': 'file_storage/call_1tDXH57o54HBmkNb2iIQG2X5.json', 'var_call_q8v7syzzEEZifdrqN9qjYfY1': 'file_storage/call_q8v7syzzEEZifdrqN9qjYfY1.json', 'var_call_YvUdKMdVnUfwPMwqdGUBaoAh': 'file_storage/call_YvUdKMdVnUfwPMwqdGUBaoAh.json'}

exec(code, env_args)
