code = """import json, re, statistics, os

# Load full citation data
path = var_call_Un4sAuOnRDhijF5Y9sGJyioc
with open(path, 'r') as f:
    citations = json.load(f)

# Load full paper docs from file path in preview variable
path_papers = var_call_RQPO8TFCONYXuKbvQbUoxBNj
with open(path_papers, 'r') as f:
    papers = json.load(f)

acm_titles = set()
for doc in papers:
    text = doc.get('text', '')
    if re.search(r'ACM\b', text):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        acm_titles.add(title)

counts = []
for c in citations:
    if c['title'] in acm_titles:
        try:
            counts.append(int(c['citation_count']))
        except Exception:
            pass

avg = statistics.mean(counts) if counts else 0
avg_rounded = round(avg, 2)

import json as _json
out = _json.dumps(avg_rounded)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Un4sAuOnRDhijF5Y9sGJyioc': 'file_storage/call_Un4sAuOnRDhijF5Y9sGJyioc.json', 'var_call_RQPO8TFCONYXuKbvQbUoxBNj': 'file_storage/call_RQPO8TFCONYXuKbvQbUoxBNj.json'}

exec(code, env_args)
