code = """import json

def load(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg_latest = load(var_call_Wmn4ZjaNEt1MylUS4b0rwr1y)
proj_pkg = load(var_call_CM29JjO0yMg1zMvvvwhYjq5L)
proj_info = load(var_call_wYMLSMTL4oICfXSaKQLWVcUO)

keys = set()
for r in pkg_latest:
    keys.add((r.get('System'), r.get('Name'), r.get('Version')))

mappings = []
for r in proj_pkg:
    key = (r.get('System'), r.get('Name'), r.get('Version'))
    if key in keys:
        mappings.append({'System': r.get('System'), 'Name': r.get('Name'), 'Version': r.get('Version'), 'ProjectName': r.get('ProjectName')})

repo_stars = {}
for r in proj_info:
    text = r.get('Project_Information') if isinstance(r.get('Project_Information'), str) else ''
    if not text:
        continue
    lower = text.lower()
    repo = None
    if 'project ' in lower:
        idx = lower.find('project ')
        sub = text[idx + len('project '):]
        token = ''
        for ch in sub:
            if ch.isspace() or ch in ',.':
                break
            token += ch
        if '/' in token:
            repo = token
    stars = None
    if 'stars' in lower:
        pos = lower.rfind('stars')
        i = pos - 1
        while i >= 0 and text[i] == ' ':
            i -= 1
        digits = ''
        j = i
        while j >= 0 and (text[j].isdigit() or text[j] == ','):
            digits = text[j] + digits
            j -= 1
        if digits:
            try:
                stars = int(digits.replace(',', ''))
            except:
                stars = None
    if repo and stars is not None:
        prev = repo_stars.get(repo)
        if prev is None or stars > prev:
            repo_stars[repo] = stars

results = []
for m in mappings:
    pname = m.get('ProjectName')
    stars = 0
    if isinstance(pname, str) and pname in repo_stars:
        stars = repo_stars[pname]
    else:
        if isinstance(pname, str):
            short = pname.split('/')[-1]
            for repo, s in repo_stars.items():
                if repo.endswith('/' + short):
                    stars = s
                    break
    results.append({'Name': m.get('Name'), 'Version': m.get('Version'), 'ProjectName': pname, 'Stars': stars})

best = {}
for r in results:
    name = r['Name']
    if name not in best or r['Stars'] > best[name]['Stars']:
        best[name] = r

best_list = list(best.values())
best_list.sort(key=lambda x: x['Stars'], reverse=True)

top5 = best_list[:5]

lines = []
for i, it in enumerate(top5, start=1):
    lines.append(str(i) + '. ' + str(it['Name']) + ' ' + str(it['Version']) + ' - ' + str(it['Stars']) + ' stars (' + str(it['ProjectName']) + ')')
answer_text = '\n'.join(lines)
output = {'text': answer_text, 'records': top5}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_E8TbuKKRyBtdFCb4DZqm7pZI': ['packageinfo'], 'var_call_2xc9qu26NUq4fx2UNbpxve99': ['project_info', 'project_packageversion'], 'var_call_Wmn4ZjaNEt1MylUS4b0rwr1y': 'file_storage/call_Wmn4ZjaNEt1MylUS4b0rwr1y.json', 'var_call_CM29JjO0yMg1zMvvvwhYjq5L': 'file_storage/call_CM29JjO0yMg1zMvvvwhYjq5L.json', 'var_call_wYMLSMTL4oICfXSaKQLWVcUO': 'file_storage/call_wYMLSMTL4oICfXSaKQLWVcUO.json', 'var_call_ilbKEsM79khpKPMvJgTK2F5A': {'len_a': 22146, 'len_b': 597602, 'len_c': 770}}

exec(code, env_args)
