code = """import re, json
from pathlib import Path

# Load full Mongo results
path_docs = Path(var_call_hSoKqQZmsc4kPLLvwL8D9d3T)
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title, year, and domain relevance
physical_docs = []
for d in docs:
    text = d.get('text', '')
    # rough year detection: look for 2016 in text
    if '2016' not in text:
        continue
    # domain: require 'physical activity' substring
    if re.search(r'physical activity', text, re.IGNORECASE):
        filename = d.get('filename', '')
        title = filename.rsplit('.txt', 1)[0]
        physical_docs.append({'title': title})

# Load citations aggregation
path_cit = Path(var_call_su2GTaNl5oqFl2gdI7bNFNZ0)
with open(path_cit, 'r') as f:
    cits = json.load(f)

# Build lookup of total citations by normalized title
cit_lookup = {c['title']: int(c['total_citations']) for c in cits}

results = []
for p in physical_docs:
    t = p['title']
    if t in cit_lookup:
        results.append({'title': t, 'total_citations': cit_lookup[t]})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_hSoKqQZmsc4kPLLvwL8D9d3T': 'file_storage/call_hSoKqQZmsc4kPLLvwL8D9d3T.json', 'var_call_su2GTaNl5oqFl2gdI7bNFNZ0': 'file_storage/call_su2GTaNl5oqFl2gdI7bNFNZ0.json'}

exec(code, env_args)
