code = """import json, re, pandas as pd

# load big results

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkgs = load_records(var_call_wj2XDfLebwmEanmJge8aeLEa)
ppv = load_records(var_call_zetaH8YchcoYJ7YMiA9R8cAL)
pi = load_records(var_call_vOKmNBpupvgnV7x4CxEbNAlI)

pkgs_df = pd.DataFrame(pkgs)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna().drop_duplicates()

merged = pkgs_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
projects = merged['ProjectName'].dropna().drop_duplicates()

# parse fork counts from Project_Information and repo name
def parse_info(s):
    if not isinstance(s,str):
        return None
    m_repo = re.search(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    if not m_repo:
        m_repo = re.search(r'project\s+named\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    if not m_repo:
        m_repo = re.search(r'hosted on GitHub under the name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)', s)
    repo = m_repo.group(1) if m_repo else None
    m_forks = re.search(r'([0-9][0-9,]*)\s+forks', s)
    forks = int(m_forks.group(1).replace(',','')) if m_forks else None
    return repo, forks

rows=[]
for rec in pi:
    s = rec.get('Project_Information')
    parsed = parse_info(s)
    if parsed is None:
        continue
    repo, forks = parsed
    if repo is None or forks is None:
        continue
    rows.append({'ProjectName': repo, 'Forks': forks})

info_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'], keep='last')

cand = info_df[info_df['ProjectName'].isin(set(projects))].copy()

top5 = cand.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wj2XDfLebwmEanmJge8aeLEa': 'file_storage/call_wj2XDfLebwmEanmJge8aeLEa.json', 'var_call_zetaH8YchcoYJ7YMiA9R8cAL': 'file_storage/call_zetaH8YchcoYJ7YMiA9R8cAL.json', 'var_call_vOKmNBpupvgnV7x4CxEbNAlI': 'file_storage/call_vOKmNBpupvgnV7x4CxEbNAlI.json'}

exec(code, env_args)
