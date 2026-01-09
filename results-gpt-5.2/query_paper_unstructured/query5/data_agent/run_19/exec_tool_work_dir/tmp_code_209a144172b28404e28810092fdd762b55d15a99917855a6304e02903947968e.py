code = """import json, re
import pandas as pd

# Load citations 2020
c_path = var_call_hWiM5HZ68V4F6rVA8Xf5s2cA
with open(c_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Load paper docs
p_path = var_call_eSzFc6IqyNMmiU3cunAwbWtK
with open(p_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build set of CHI paper titles from docs
chi_titles = set()
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # heuristic: venue appears in header; match 'CHI' token (avoid 'Ubicomp', etc.)
    # Look for patterns like "CHI '20" or "CHI 2020" or "Proceedings of the SIGCHI"
    if re.search(r"\bCHI\b\s*['’]?\d{2}\b", text) or re.search(r"\bCHI\b\s*20\d{2}\b", text) or re.search(r"SIGCHI\b", text):
        chi_titles.add(title)

# Filter citations to those titles
rows = []
for r in citations:
    t = r.get('title')
    if t in chi_titles:
        try:
            cc = int(r.get('citation_count'))
        except Exception:
            cc = 0
        rows.append({'title': t, 'citation_count_2020': cc})

# Aggregate total
total = sum(x['citation_count_2020'] for x in rows)

out = {
    'citation_year': 2020,
    'venue': 'CHI',
    'num_papers': len(rows),
    'total_citation_count': total
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hWiM5HZ68V4F6rVA8Xf5s2cA': 'file_storage/call_hWiM5HZ68V4F6rVA8Xf5s2cA.json', 'var_call_eSzFc6IqyNMmiU3cunAwbWtK': 'file_storage/call_eSzFc6IqyNMmiU3cunAwbWtK.json'}

exec(code, env_args)
