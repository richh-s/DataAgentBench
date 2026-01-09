code = """import json, re
import pandas as pd

# Load mongo docs (file path)
path_docs = var_call_HMibItbSybVlZOrOudCMaRUr
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def infer_year(text):
    # look for common patterns
    patterns = [
        r'\bCHI\s*2016\b', r'\bCSCW\s*2016\b', r'\bUbiComp\s*2016\b', r'\bUbicomp\s*2016\b',
        r'\bDIS\s*2016\b', r'\bIUI\s*2016\b', r'\bWWW\s*2016\b', r'\bTEI\s*2016\b', r'\bOzCHI\s*2016\b',
        r'\bPervasiveHealth\s*2016\b',
        r'\b2016\b'
    ]
    for pat in patterns:
        if re.search(pat, text, flags=re.IGNORECASE):
            return 2016
    return None

def infer_domain(text, filename):
    hay = (filename + "\n" + text).lower()
    if 'physical activity' in hay or 'physical-activity' in hay:
        return True
    # include obvious related terms? but keep strict
    return False

records = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = infer_year(text)
    if year != 2016:
        continue
    if not infer_domain(text, title):
        continue
    records.append({'title': title})

# Unique titles
titles_2016_pa = sorted(set(r['title'] for r in records))

# Load citations totals (file path)
path_cit = var_call_pDRTPsGZdBN8y5Mri3wCsXzf
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

cit_map = {r['title']: int(r['total_citations']) for r in cits}

out = []
for t in titles_2016_pa:
    out.append({'title': t, 'total_citations': cit_map.get(t)})

# remove missing citation totals
out2 = [r for r in out if r['total_citations'] is not None]

result = json.dumps(out2, ensure_ascii=False)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_HMibItbSybVlZOrOudCMaRUr': 'file_storage/call_HMibItbSybVlZOrOudCMaRUr.json', 'var_call_pDRTPsGZdBN8y5Mri3wCsXzf': 'file_storage/call_pDRTPsGZdBN8y5Mri3wCsXzf.json'}

exec(code, env_args)
