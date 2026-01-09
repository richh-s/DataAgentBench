code = """import json, re, pandas as pd

# Load citations 2020
cit = var_call_4CqxFHE0am19nJyL2jJwL3cz
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

docs = var_call_s7FHupoFbPHVr6XNH5g09YkZ
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Build set of CHI paper titles from docs by simple venue detection
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # detect CHI in header/citation lines: e.g., "CHI 'YY" or "Proceedings of the SIGCHI"
    if re.search(r"\bCHI\b\s*'\d{2}", text) or re.search(r"\bSIGCHI\b", text) or re.search(r"\bACM\s+CHI\b", text):
        chi_titles.add(title)

# Sum citations for CHI titles in 2020
chi_cit_total = 0
chi_rows = []
for r in cit:
    t = r.get('title')
    if t in chi_titles:
        cc = r.get('citation_count')
        try:
            cc = int(cc)
        except Exception:
            cc = 0
        chi_cit_total += cc
        chi_rows.append({'title': t, 'citation_count_2020': cc})

out = {
    'total_citation_count_2020_for_CHI_papers': chi_cit_total,
    'num_CHI_papers_cited_in_2020': len(chi_rows)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4CqxFHE0am19nJyL2jJwL3cz': 'file_storage/call_4CqxFHE0am19nJyL2jJwL3cz.json', 'var_call_s7FHupoFbPHVr6XNH5g09YkZ': 'file_storage/call_s7FHupoFbPHVr6XNH5g09YkZ.json'}

exec(code, env_args)
