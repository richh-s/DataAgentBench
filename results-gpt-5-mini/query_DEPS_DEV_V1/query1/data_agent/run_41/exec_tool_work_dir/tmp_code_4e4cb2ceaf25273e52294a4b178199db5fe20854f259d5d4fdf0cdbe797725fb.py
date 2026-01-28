code = """import json, re

def load(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

proj_info = load(var_call_wYMLSMTL4oICfXSaKQLWVcUO)

repo_pattern = re.compile(r"project\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", re.IGNORECASE)
stars_pattern = re.compile(r"([0-9][0-9,]*)\s+stars", re.IGNORECASE)

repo_stars = {}
for rec in proj_info:
    text = rec.get('Project_Information') if isinstance(rec.get('Project_Information'), str) else ''
    if not text:
        continue
    repo = None
    m = repo_pattern.search(text)
    if m:
        repo = m.group(1)
    # alternative patterns
    if not repo:
        m2 = re.search(r"named\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", text, re.IGNORECASE)
        if m2:
            repo = m2.group(1)
    if not repo:
        m3 = re.search(r"on\s+GitHub\s+under\s+the\s+name\s+([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", text, re.IGNORECASE)
        if m3:
            repo = m3.group(1)
    # extract stars
    stars = None
    mstar = stars_pattern.findall(text)
    if mstar:
        try:
            stars = int(mstar[-1].replace(',', ''))
        except:
            stars = None
    if repo and stars is not None:
        prev = repo_stars.get(repo)
        if prev is None or stars > prev:
            repo_stars[repo] = stars

# sort
top_repos = sorted(repo_stars.items(), key=lambda x: x[1], reverse=True)[:50]

print('__RESULT__:')
print(json.dumps(top_repos))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json', 'var_call_ilbKEsM79khpKPMvJgTK2F5A': {'len_a': 22146, 'len_b': 597602, 'len_c': 770}, 'var_call_1weIKGjvkjiGFHP8hR66Kab9': 'file_storage/call_1weIKGjvkjiGFHP8hR66Kab9.json'}

exec(code, env_args)
