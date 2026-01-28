code = """import json, re
import pandas as pd

def load_var(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_var(var_call_iCEQzI6rXcypBuJ0h0ZCtEUM)
ppv = load_var(var_call_ET8EdPFtmc9Hs8wYWhcSwzh9)
pi = load_var(var_call_xet73vhHi0hniOcQTrkvBiyB)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

df = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
projects = set(df['ProjectName'].dropna().unique().tolist())

# parse project_info strings for owner/repo and forks
pat_repo = re.compile(r'project\s+([^\s]+/[^\s]+)')
pat_forks = re.compile(r'(?:and\s+)?(\d{1,3}(?:,\d{3})*)\s+forks?')

rows = []
for rec in pi:
    s = rec.get('Project_Information') or ''
    mrepo = pat_repo.search(s)
    if not mrepo:
        continue
    repo = mrepo.group(1).rstrip('.,')
    if repo not in projects:
        continue
    mf = pat_forks.search(s)
    if not mf:
        continue
    forks = int(mf.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks})

df_f = pd.DataFrame(rows)
if df_f.empty:
    top5 = []
else:
    df_f = df_f.sort_values(['Forks','ProjectName'], ascending=[False, True]).drop_duplicates('ProjectName')
    top5 = df_f.head(5).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_iCEQzI6rXcypBuJ0h0ZCtEUM': 'file_storage/call_iCEQzI6rXcypBuJ0h0ZCtEUM.json', 'var_call_ET8EdPFtmc9Hs8wYWhcSwzh9': 'file_storage/call_ET8EdPFtmc9Hs8wYWhcSwzh9.json', 'var_call_xet73vhHi0hniOcQTrkvBiyB': 'file_storage/call_xet73vhHi0hniOcQTrkvBiyB.json'}

exec(code, env_args)
