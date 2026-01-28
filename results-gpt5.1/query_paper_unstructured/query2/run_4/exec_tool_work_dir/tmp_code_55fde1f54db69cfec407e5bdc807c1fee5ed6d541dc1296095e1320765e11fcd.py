code = """import json, re, statistics
from collections import defaultdict

# Load citations data
with open(var_call_EZcKqy4VwfQlIl4ja5NO2O8H, 'r') as f:
    citations = json.load(f)

# Load paper docs data
with open(var_call_RycN9KCl6ijtCoXfTzUS7WAi, 'r') as f:
    docs = json.load(f)

# Build index from title to source (publisher) using heuristics on text
# We consider a paper to be ACM if its text contains 'Copyright' and 'ACM'
acm_titles = set()
for doc in docs:
    title = doc.get('filename','').rsplit('.txt',1)[0]
    text = doc.get('text','')
    if not title or not text:
        continue
    if re.search(r'ACM', text):
        acm_titles.add(title)

# Collect citation counts for ACM papers cited in 2018
counts = []
for row in citations:
    title = row.get('title')
    if title in acm_titles:
        try:
            c = int(row.get('citation_count'))
            counts.append(c)
        except (TypeError, ValueError):
            continue

avg = statistics.mean(counts) if counts else 0

result = {"average_citation_count_acm_2018": avg, "paper_count": len(counts)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EZcKqy4VwfQlIl4ja5NO2O8H': 'file_storage/call_EZcKqy4VwfQlIl4ja5NO2O8H.json', 'var_call_RycN9KCl6ijtCoXfTzUS7WAi': 'file_storage/call_RycN9KCl6ijtCoXfTzUS7WAi.json'}

exec(code, env_args)
