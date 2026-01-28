code = """import json, re

path_docs = var_call_HMibItbSybVlZOrOudCMaRUr
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_year(text):
    patterns = [
        r'\bCHI\s*2016\b', r'\bCSCW\s*2016\b', r'\bUbiComp\s*2016\b', r'\bUbicomp\s*2016\b',
        r'\bDIS\s*2016\b', r'\bIUI\s*2016\b', r'\bWWW\s*2016\b', r'\bTEI\s*2016\b', r'\bOzCHI\s*2016\b',
        r'\bPervasiveHealth\s*2016\b',
        r'\b2016\b'
    ]
    for pat in patterns:
        if re.search(pat, text or '', flags=re.IGNORECASE):
            return 2016
    return None

def is_physical_activity_domain(text, filename):
    hay = ((filename or '') + '\n' + (text or '')).lower()
    return ('physical activity' in hay) or ('physical-activity' in hay)

pa_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if infer_year(text) != 2016:
        continue
    if not is_physical_activity_domain(text, title):
        continue
    pa_titles.add(title)

path_cit = var_call_pDRTPsGZdBN8yMri3wCsXzf if 'var_call_pDRTPsGZdBN8yMri3wCsXzf' in globals() else var_call_pDRTPsGZdBN8y5Mri3wCsXzf
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

cit_map = {r['title']: int(r['total_citations']) for r in cits}

out = [{'title': t, 'total_citations': cit_map.get(t)} for t in sorted(pa_titles)]
out = [r for r in out if r['total_citations'] is not None]

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_HMibItbSybVlZOrOudCMaRUr': 'file_storage/call_HMibItbSybVlZOrOudCMaRUr.json', 'var_call_pDRTPsGZdBN8y5Mri3wCsXzf': 'file_storage/call_pDRTPsGZdBN8y5Mri3wCsXzf.json'}

exec(code, env_args)
