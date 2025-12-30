code = """import json, pandas as pd
from statistics import mean

# Load full citations result
with open(var_call_EXFf7WlLidpioxwGT99TNekz, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_dMgUPwhrOCC9EzRCzDHBxn1d, 'r') as f:
    papers = json.load(f)

# Build lookup of title -> is_acm based on text heuristic
acm_titles = set()
for doc in papers:
    text = doc.get('text','').upper()
    # simple heuristic: look for 'ACM' near copyright/permission lines
    if 'ACM' in text[:4000]:
        title = doc.get('filename','').rsplit('.txt',1)[0]
        acm_titles.add(title)

# Filter citations for ACM-sourced papers
acm_citations = [int(r['citation_count']) for r in citations if r['title'] in acm_titles]

avg_citation = mean(acm_citations) if acm_citations else 0

import json as _json
result = _json.dumps(avg_citation)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_EXFf7WlLidpioxwGT99TNekz': 'file_storage/call_EXFf7WlLidpioxwGT99TNekz.json', 'var_call_lUgzkbIVZwKRHLdRsPeupull': ['paper_docs'], 'var_call_dMgUPwhrOCC9EzRCzDHBxn1d': 'file_storage/call_dMgUPwhrOCC9EzRCzDHBxn1d.json'}

exec(code, env_args)
