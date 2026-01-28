code = """import json, re

def load(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_latest = load(var_call_Wmn4ZjaNEt1MylUS4b0rwr1y)
proj_pkg = load(var_call_CM29JjO0yMg1zMvvvwhYjq5L)
proj_info = load(var_call_wYMLSMTL4oICfXSaKQLWVcUO)

# Build set of latest package keys
keys = set()
for rec in pkg_latest:
    keys.add((rec.get('System'), rec.get('Name'), rec.get('Version')))

# Map package (Name,Version,System) -> list of ProjectName
mappings = []
for rec in proj_pkg:
    key = (rec.get('System'), rec.get('Name'), rec.get('Version'))
    if key in keys:
        mappings.append({'System': rec.get('System'), 'Name': rec.get('Name'), 'Version': rec.get('Version'), 'ProjectName': rec.get('ProjectName')})

# Parse project_info to map repo fullname -> stars
repo_stars = {}
stars_re = re.compile(r"([0-9][0-9,]*)\s+stars", re.IGNORECASE)
repo_re = re.compile(r"project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", re.IGNORECASE)

for rec in proj_info:
    text = rec.get('Project_Information') if isinstance(rec.get('Project_Information'), str) else ''
    if not text:
        continue
    # find repo fullname
    repo = None
    m = repo_re.search(text)
    if m:
        repo = m.group(1)
    # find stars
    s = None
    ms = stars_re.findall(text)
    if ms:
        try:
            s = int(ms[-1].replace(',', ''))
        except:
            s = None
    if repo and s is not None:
        # keep max stars if multiple entries
        if repo in repo_stars:
            if s > repo_stars[repo]:
                repo_stars[repo] = s
        else:
            repo_stars[repo] = s

# For each mapping, attach stars from repo_stars
results = []
for m in mappings:
    pname = m.get('ProjectName')
    stars = None
    if isinstance(pname, str) and pname in repo_stars:
        stars = repo_stars[pname]
    else:
        # try short repo name match: find any repo in repo_stars that ends with '/<short>'
        if isinstance(pname, str):
            short = pname.split('/')[-1]
            for repo, s in repo_stars.items():
                if repo.endswith('/' + short):
                    stars = s
                    break
    if stars is None:
        stars = 0
    results.append({'Name': m.get('Name'), 'Version': m.get('Version'), 'ProjectName': m.get('ProjectName'), 'Stars': stars})

# Consolidate per package Name: keep highest stars and its version
best = {}
for r in results:
    name = r['Name']
    if name not in best or r['Stars'] > best[name]['Stars']:
        best[name] = r

best_list = list(best.values())
# Sort by stars desc and take top 5
best_list.sort(key=lambda x: x['Stars'], reverse=True)
top5 = best_list[:5]

# Prepare output
lines = []
for i, it in enumerate(top5, start=1):
    lines.append(f"{i}. {it['Name']} {it['Version']} — {it['Stars']} stars ({it['ProjectName']})")
answer_text = "\n".join(lines)
output = {'text': answer_text, 'records': top5}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json', 'var_call_ilbKEsM79khpKPMvJgTK2F5A': {'len_a': 22146, 'len_b': 597602, 'len_c': 770}}

exec(code, env_args)
