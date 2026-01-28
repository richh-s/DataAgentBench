code = """import json, re, statistics, os

# Load full citation data
path = var_call_Un4sAuOnRDhijF5Y9sGJyioc
with open(path, 'r') as f:
    citations = json.load(f)

# Build a set of titles cited in 2018
titles_2018 = {c['title'] for c in citations}

# Load paper docs metadata from preview variable (already full list if not truncated)
papers = var_call_RQPO8TFCONYXuKbvQbUoxBNj

acm_titles = set()
for doc in papers:
    text = doc.get('text', '')
    # Heuristic: check if publisher ACM appears in front-matter
    if re.search(r'ACM\b', text):
        # title is filename without .txt
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        acm_titles.add(title)

# Filter citation records to those whose titles are ACM and cited in 2018
counts = []
for c in citations:
    if c['title'] in acm_titles:
        try:
            counts.append(int(c['citation_count']))
        except Exception:
            pass

avg = statistics.mean(counts) if counts else 0

import math
avg_rounded = round(avg, 2)

result = avg_rounded

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Un4sAuOnRDhijF5Y9sGJyioc': 'file_storage/call_Un4sAuOnRDhijF5Y9sGJyioc.json', 'var_call_RQPO8TFCONYXuKbvQbUoxBNj': 'file_storage/call_RQPO8TFCONYXuKbvQbUoxBNj.json'}

exec(code, env_args)
