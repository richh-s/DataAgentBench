code = """import json, re, pandas as pd

# Load large results if stored as file paths
pkg_src = var_call_TBfq6ui6ABPZ2vL1bhHZ2JOP
ppv_src = var_call_Ao0yp5FJgzJMtORaKQaK339d
pi_src  = var_call_9KCIw2aOU5bguHeDcerBoBJO

def load(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load(pkg_src)
ppv = load(ppv_src)
pi  = load(pi_src)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version','Licenses','VersionInfo']]
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']]
df_pi = pd.DataFrame(pi)

# join package versions to github projects
m = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')

# parse project name from Project_Information and forks count
fork_re = re.compile(r'\b(\d[\d,]*)\s+forks\b', re.IGNORECASE)
name_re1 = re.compile(r'\bproject\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')
name_re2 = re.compile(r'\bnamed\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')
name_re3 = re.compile(r'\bunder\s+the\s+name\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')

def extract_owner_repo(s):
    if not isinstance(s, str):
        return None
    for rr in (name_re1, name_re2, name_re3):
        mm = rr.search(s)
        if mm:
            return mm.group(1)
    return None

def extract_forks(s):
    if not isinstance(s, str):
        return None
    mm = fork_re.search(s)
    if not mm:
        return None
    return int(mm.group(1).replace(',',''))

pi_rows = []
for rec in pi:
    s = rec.get('Project_Information')
    owner_repo = extract_owner_repo(s)
    forks = extract_forks(s)
    if owner_repo and forks is not None:
        pi_rows.append({'ProjectName': owner_repo, 'Forks': forks})

df_metrics = pd.DataFrame(pi_rows).drop_duplicates(subset=['ProjectName'])

# combine and deduplicate per project
m2 = m[['ProjectName']].drop_duplicates().merge(df_metrics, on='ProjectName', how='inner')

# take top 5 by forks
m2 = m2.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

out_lines = []
for i, row in enumerate(m2.to_dict(orient='records'), start=1):
    out_lines.append(f"{i}. {row['ProjectName']} — {row['Forks']} forks")

result = "\n".join(out_lines)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_TBfq6ui6ABPZ2vL1bhHZ2JOP': 'file_storage/call_TBfq6ui6ABPZ2vL1bhHZ2JOP.json', 'var_call_Ao0yp5FJgzJMtORaKQaK339d': 'file_storage/call_Ao0yp5FJgzJMtORaKQaK339d.json', 'var_call_9KCIw2aOU5bguHeDcerBoBJO': 'file_storage/call_9KCIw2aOU5bguHeDcerBoBJO.json'}

exec(code, env_args)
