code = """import re, json
from pathlib import Path

# Load full citation data
with open(var_call_C86dysktVw4MTLkKqpUvoLH4, 'r') as f:
    citations = json.load(f)

# Load full paper docs
with open(var_call_2NWLjZFw4oQkButkKFQxEUjc, 'r') as f:
    papers = json.load(f)

results = []
for p in papers:
    text = p.get('text','')
    # crude year extraction: look for 2016 in text
    if '2016' not in text:
        continue
    # domain filter already roughly by regex, but double-check
    if 'physical activity' not in text.lower():
        continue
    title = p.get('filename','').replace('.txt','')
    # find matching citation record
    total_cit = None
    for c in citations:
        if c['title'] == title:
            total_cit = int(c['total_citations'])
            break
    if total_cit is not None:
        results.append({'title': title, 'total_citations': total_cit})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_2NWLjZFw4oQkButkKFQxEUjc': 'file_storage/call_2NWLjZFw4oQkButkKFQxEUjc.json', 'var_call_C86dysktVw4MTLkKqpUvoLH4': 'file_storage/call_C86dysktVw4MTLkKqpUvoLH4.json'}

exec(code, env_args)
