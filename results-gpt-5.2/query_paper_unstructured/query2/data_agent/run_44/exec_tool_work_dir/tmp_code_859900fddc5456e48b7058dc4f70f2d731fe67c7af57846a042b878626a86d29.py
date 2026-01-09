code = """import json, re
import pandas as pd

# Load citations 2018
cit = var_call_zSgHJoaZqQZUtnQcB0mm6NTI
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

docs = var_call_qcuB7G45SlVxG9i3bj36sxYz
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Build set of ACM paper titles from docs via simple pattern matching in text
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bACM\b', text) and re.search(r'Copyright\s*\d{4}\s*©\s*ACM|\bACM\s+Classification\b|\bAssociation\s+for\s+Computing\s+Machinery\b', text, flags=re.IGNORECASE):
        acm_titles.add(title)

# Join with citations
rows = []
for r in cit:
    t = r.get('title')
    if t in acm_titles:
        try:
            cc = int(r.get('citation_count'))
        except Exception:
            continue
        rows.append(cc)

avg = sum(rows)/len(rows) if rows else None
out = {
    "average_citation_count_2018_for_acm_papers": avg,
    "acm_papers_with_2018_citations_matched": len(rows)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zSgHJoaZqQZUtnQcB0mm6NTI': 'file_storage/call_zSgHJoaZqQZUtnQcB0mm6NTI.json', 'var_call_qcuB7G45SlVxG9i3bj36sxYz': 'file_storage/call_qcuB7G45SlVxG9i3bj36sxYz.json'}

exec(code, env_args)
