code = """import json, re

path_docs = var_call_YtD90rUj03rayH0hWzM7kgCV
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# find park-related completed in 2022 by direct regex scan, then map back to likely project names near it.

def extract_titles_near(text, idx, window=600):
    start = max(0, idx-window)
    snippet = text[start:idx]
    # take last ~20 lines
    lines = [ln.strip() for ln in snippet.splitlines() if ln.strip()]
    lines = lines[-30:]
    # candidate titles: lines not starting with bullets/labels and not containing ':'
    cands = []
    for ln in lines[::-1]:
        low = ln.lower()
        if 'updates' in low or 'project schedule' in low or 'estimated schedule' in low:
            continue
        if ':' in ln:
            continue
        if len(ln) > 140:
            continue
        if low.startswith(('(cid','page','agenda item','to:','prepared','approved','date prepared','meeting date','subject','recommended action','discussion')):
            continue
        # must include park-ish keyword
        if any(k in low for k in ['park','playground','bluffs']):
            cands.append(ln)
    return cands[:3]

hits = []
for d in docs:
    t = d.get('text','')
    for m in re.finditer(r'Construction was completed[^\n]*2022', t, flags=re.I):
        titles = extract_titles_near(t, m.start())
        hits.append({'filename': d.get('filename'), 'match': m.group(0), 'titles': titles})

print('__RESULT__:')
print(json.dumps(hits[:50]))"""

env_args = {'var_call_YtD90rUj03rayH0hWzM7kgCV': 'file_storage/call_YtD90rUj03rayH0hWzM7kgCV.json', 'var_call_7rv7dzdnvLIhF51JyL0Jqu7x': 'file_storage/call_7rv7dzdnvLIhF51JyL0Jqu7x.json', 'var_call_k6GiortEkCkLT38S4OkCuc8D': {'total_funding': 0, 'project_count': 0, 'projects': [], 'matched_project_names': []}}

exec(code, env_args)
