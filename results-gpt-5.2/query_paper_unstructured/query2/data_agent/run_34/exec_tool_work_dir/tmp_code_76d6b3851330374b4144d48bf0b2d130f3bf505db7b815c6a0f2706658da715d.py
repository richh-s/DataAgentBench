code = """import json, re

cit_path = var_call_lhFvPE9YVBHGdn7iY52xvBz3
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

docs_path = var_call_euNumx1ZaLA6zKpMsVbVsWUY
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

acm_titles = set()
pat1 = re.compile(r"\bCopyright\b[^\\n]{0,200}\bACM\b", re.IGNORECASE)
pat2 = re.compile(r"\b\u00a9\s*ACM\b", re.IGNORECASE)
pat3 = re.compile(r"\bAssociation for Computing Machinery\b", re.IGNORECASE)

for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if pat1.search(text) or pat2.search(text) or pat3.search(text):
        acm_titles.add(title)

counts = []
for r in citations:
    t = r.get('title')
    if t in acm_titles:
        cc = r.get('citation_count')
        try:
            counts.append(int(cc))
        except Exception:
            pass

avg = (sum(counts) / len(counts)) if counts else None
result = {"acm_papers_with_2018_citations": len(counts), "average_2018_citation_count": avg}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lhFvPE9YVBHGdn7iY52xvBz3': 'file_storage/call_lhFvPE9YVBHGdn7iY52xvBz3.json', 'var_call_euNumx1ZaLA6zKpMsVbVsWUY': 'file_storage/call_euNumx1ZaLA6zKpMsVbVsWUY.json'}

exec(code, env_args)
