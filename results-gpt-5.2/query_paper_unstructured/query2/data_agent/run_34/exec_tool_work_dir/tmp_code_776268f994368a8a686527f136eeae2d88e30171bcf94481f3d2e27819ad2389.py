code = """import json, re

cit_path = var_call_lhFvPE9YVBHGdn7iY52xvBz3
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

docs_path = var_call_euNumx1ZaLA6zKpMsVbVsWUY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# More permissive ACM detection
pat_acm = re.compile(r"\bACM\b|Association for Computing Machinery|acm\.org", re.IGNORECASE)

acm_titles = set()
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if pat_acm.search(text):
        acm_titles.add(title)

cit_titles = set(r.get('title') for r in citations)
intersection = sorted(list(acm_titles.intersection(cit_titles)))

# compute avg
counts = []
for r in citations:
    if r.get('title') in acm_titles:
        try:
            counts.append(int(r.get('citation_count')))
        except Exception:
            pass

avg = (sum(counts)/len(counts)) if counts else None

result = {
    "n_docs": len(docs),
    "n_acm_docs_detected": len(acm_titles),
    "n_2018_citation_rows": len(citations),
    "n_matches": len(counts),
    "avg": avg,
    "sample_matches": intersection[:20]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lhFvPE9YVBHGdn7iY52xvBz3': 'file_storage/call_lhFvPE9YVBHGdn7iY52xvBz3.json', 'var_call_euNumx1ZaLA6zKpMsVbVsWUY': 'file_storage/call_euNumx1ZaLA6zKpMsVbVsWUY.json', 'var_call_frI3g49aDo4ZLwjJpiMnKgcp': {'acm_papers_with_2018_citations': 0, 'average_2018_citation_count': None}}

exec(code, env_args)
