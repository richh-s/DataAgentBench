code = """import json, re, pandas as pd

# load large results
import os

def load_result(x):
    if isinstance(x, str) and x.endswith('.json') and os.path.exists(x):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

pkg = load_result(var_call_pH1tAbkqvStAaKlqkcWx7QdL)
ppv = load_result(var_call_wzZKrBkSjK4C7fHoJDZYt48L)
pi = load_result(var_call_pWJ06Yz4KXDUfAFm6iJ0xyvA)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()
merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
proj_names = merged['ProjectName'].dropna().drop_duplicates()

# parse forks from Project_Information
pattern = re.compile(r"project\s+([^\s]+/[^\s]+).*?\b([0-9,]+)\s+forks?\b", re.IGNORECASE)
rows = []
for rec in pi:
    s = rec.get('Project_Information')
    if not s:
        continue
    m = pattern.search(s)
    if not m:
        continue
    pname = m.group(1).strip().rstrip('.,')
    forks = int(m.group(2).replace(',',''))
    rows.append((pname, forks))

fork_df = pd.DataFrame(rows, columns=['ProjectName','Forks'])
# in case duplicates, take max
fork_df = fork_df.groupby('ProjectName', as_index=False)['Forks'].max()

cand = fork_df[fork_df['ProjectName'].isin(set(proj_names))].sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

result = cand.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_pH1tAbkqvStAaKlqkcWx7QdL': 'file_storage/call_pH1tAbkqvStAaKlqkcWx7QdL.json', 'var_call_wzZKrBkSjK4C7fHoJDZYt48L': 'file_storage/call_wzZKrBkSjK4C7fHoJDZYt48L.json', 'var_call_pWJ06Yz4KXDUfAFm6iJ0xyvA': 'file_storage/call_pWJ06Yz4KXDUfAFm6iJ0xyvA.json'}

exec(code, env_args)
