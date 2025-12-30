code = """import json, re
from pathlib import Path

# Load citations
with open(var_call_T4q2EwGkGrLv0xflwwCSiPsx, 'r') as f:
    citations = json.load(f)

# Load paper docs
with open(var_call_b9s8DUZJ8d16pQWMt9QU9bvK, 'r') as f:
    paper_docs = json.load(f)

# Build lookup: title -> venue (from text heuristics)
venue_lookup = {}
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename.replace('.txt','')
    text = doc.get('text','').upper()
    venue = None
    # simple heuristic: look for 'CHI ' or "CHI '" or 'CHI 20'
    if 'CHI ' in text or "CHI'" in text or 'ACM CHI' in text:
        venue = 'CHI'
    # could add more venues but not needed
    venue_lookup[title] = venue

# Sum citations for CHI papers cited in 2020
total = 0
for row in citations:
    title = row['title']
    if venue_lookup.get(title) == 'CHI':
        try:
            c = int(row['citation_count'])
        except Exception:
            c = 0
        total += c

result = json.dumps(total)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_T4q2EwGkGrLv0xflwwCSiPsx': 'file_storage/call_T4q2EwGkGrLv0xflwwCSiPsx.json', 'var_call_b9s8DUZJ8d16pQWMt9QU9bvK': 'file_storage/call_b9s8DUZJ8d16pQWMt9QU9bvK.json'}

exec(code, env_args)
