code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load(var_call_EksUhU1xiPQrFqfdLOVJVIbg)
ppv = load(var_call_b0aW5QJqLdpcS6Osu14vkirC)
pi = load(var_call_NjLXcy3XFwhltqubXOvRhPGY)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

rows = []
star_re = re.compile(r'\b([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)\b')
stars_re = re.compile(r'(\d+[\d,]*)\s+stars')
for rec in pi:
    s = rec.get('Project_Information') if isinstance(rec, dict) else None
    if not s:
        continue
    mstars = stars_re.search(s)
    if not mstars:
        continue
    # find all owner/repo candidates; choose the one after word 'project' if possible
    cands = star_re.findall(s)
    if not cands:
        continue
    project = cands[0]
    # heuristic: prefer cand that appears after 'project ' or 'project named '
    lower = s.lower()
    best = None
    for cand in cands:
        idx = lower.find(cand.lower())
        if idx != -1:
            # proximity to 'project'
            pidx = lower.rfind('project', 0, idx)
            score = (idx - pidx) if pidx != -1 else 10**9
            if best is None or score < best[0]:
                best = (score, cand)
    if best:
        project = best[1]
    stars = int(mstars.group(1).replace(',',''))
    rows.append({'ProjectName': project, 'Stars': stars})

proj_df = pd.DataFrame(rows)
if not proj_df.empty:
    proj_df = proj_df.drop_duplicates(subset=['ProjectName'], keep='first')

# build output even if empty
out = {'pkg_cols': list(pkg_df.columns), 'ppv_cols': list(ppv_df.columns), 'proj_cols': list(proj_df.columns), 'proj_sample': proj_df.head(3).to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6uggoPVDtK2VSjqJ1z9HzbHl': ['packageinfo'], 'var_call_hSF0CM4usTrZKTgQznJUgOim': ['project_info', 'project_packageversion'], 'var_call_EksUhU1xiPQrFqfdLOVJVIbg': 'file_storage/call_EksUhU1xiPQrFqfdLOVJVIbg.json', 'var_call_b0aW5QJqLdpcS6Osu14vkirC': 'file_storage/call_b0aW5QJqLdpcS6Osu14vkirC.json', 'var_call_NjLXcy3XFwhltqubXOvRhPGY': 'file_storage/call_NjLXcy3XFwhltqubXOvRhPGY.json'}

exec(code, env_args)
