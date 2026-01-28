code = """import json, re, pandas as pd

# Load citations 2018
cit_path = var_call_lhFvPE9YVBHGdn7iY52xvBz3
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Load paper docs
docs_path = var_call_euNumx1ZaLA6zKpMsVbVsWUY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build set of ACM paper titles from docs (filename without .txt) by searching for ACM copyright string
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bCopyright\b[^\n]{0,200}\bACM\b', text, flags=re.IGNORECASE) or re.search(r'\b\u00a9\s*ACM\b', text, flags=re.IGNORECASE) or re.search(r'\bAssociation for Computing Machinery\b', text, flags=re.IGNORECASE):
        acm_titles.add(title)

# Filter citations to ACM titles and compute average
counts = []
for r in citations:
    t = r.get('title')
    if t in acm_titles:
        try:
            counts.append(int(r.get('citation_count')))
        except Exception:
            pass

avg = sum(counts)/len(counts) if counts else None
result = {
    "acm_papers_with_2018_citations": len(counts),
    "average_2018_citation_count": avg
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lhFvPE9YVBHGdn7iY52xvBz3': 'file_storage/call_lhFvPE9YVBHGdn7iY52xvBz3.json', 'var_call_euNumx1ZaLA6zKpMsVbVsWUY': 'file_storage/call_euNumx1ZaLA6zKpMsVbVsWUY.json'}

exec(code, env_args)
