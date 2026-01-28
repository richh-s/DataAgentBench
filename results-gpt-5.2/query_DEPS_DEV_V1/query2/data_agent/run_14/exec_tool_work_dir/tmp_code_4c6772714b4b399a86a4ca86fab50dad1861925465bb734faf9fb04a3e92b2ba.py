code = """import json, re, pandas as pd

# Load large results
pkg_src = var_call_RAqt3dQyLrDd0gj0RwpRthNc
ppv_src = var_call_qnYM7WHmNSQ3mNs7QXKikLAr
pi_src = var_call_p3LQ72Es1nMBiT2CfUwkyJgk

def load_records(src):
    if isinstance(src, str):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    return src

pkg = load_records(pkg_src)
ppv = load_records(ppv_src)
pi = load_records(pi_src)

pkg_df = pd.DataFrame(pkg)[['System','Name','Version']].dropna()
ppv_df = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].dropna()

# match on System/Name/Version
m = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
# unique projects among qualifying package versions
projects = m[['ProjectName']].drop_duplicates()

# parse project info text: extract owner/repo and forks count
rows = []
# compile regexes
repo_re = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
forks_re = re.compile(r"(\d[\d,]*)\s+forks?", re.IGNORECASE)

for rec in pi:
    txt = rec.get('Project_Information')
    if not isinstance(txt, str):
        continue
    rm = repo_re.search(txt)
    if not rm:
        continue
    repo = rm.group(1)
    fm = forks_re.search(txt)
    if not fm:
        continue
    forks = int(fm.group(1).replace(',',''))
    rows.append({'ProjectName': repo, 'Forks': forks})

pi_df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])

joined = projects.merge(pi_df, on='ProjectName', how='inner')
# highest forks
out = joined.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_RAqt3dQyLrDd0gj0RwpRthNc': 'file_storage/call_RAqt3dQyLrDd0gj0RwpRthNc.json', 'var_call_qnYM7WHmNSQ3mNs7QXKikLAr': 'file_storage/call_qnYM7WHmNSQ3mNs7QXKikLAr.json', 'var_call_p3LQ72Es1nMBiT2CfUwkyJgk': 'file_storage/call_p3LQ72Es1nMBiT2CfUwkyJgk.json'}

exec(code, env_args)
