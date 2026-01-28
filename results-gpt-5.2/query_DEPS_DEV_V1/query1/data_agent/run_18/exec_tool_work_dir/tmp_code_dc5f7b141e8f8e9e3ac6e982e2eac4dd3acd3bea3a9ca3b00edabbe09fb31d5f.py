code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pi = load(var_call_NjLXcy3XFwhltqubXOvRhPGY)

rows=[]
star_re = re.compile(r'\b([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)\b')
stars_re = re.compile(r'(\d+[\d,]*)\s+stars', re.I)
for rec in pi[:20000]:
    s = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not s:
        continue
    mstars = stars_re.search(s)
    if not mstars:
        continue
    cands = star_re.findall(s)
    if not cands:
        continue
    stars = int(mstars.group(1).replace(',',''))
    rows.append({'ProjectName': cands[0], 'Stars': stars, 'Text': s[:120]})

df=pd.DataFrame(rows)
out={'n': len(rows), 'sample': df.head(5).to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6uggoPVDtK2VSjqJ1z9HzbHl': ['packageinfo'], 'var_call_hSF0CM4usTrZKTgQznJUgOim': ['project_info', 'project_packageversion'], 'var_call_EksUhU1xiPQrFqfdLOVJVIbg': 'file_storage/call_EksUhU1xiPQrFqfdLOVJVIbg.json', 'var_call_b0aW5QJqLdpcS6Osu14vkirC': 'file_storage/call_b0aW5QJqLdpcS6Osu14vkirC.json', 'var_call_NjLXcy3XFwhltqubXOvRhPGY': 'file_storage/call_NjLXcy3XFwhltqubXOvRhPGY.json', 'var_call_7pRH6XMB4EEFZrXa77geByhQ': {'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt'], 'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'proj_cols': [], 'proj_sample': []}}

exec(code, env_args)
