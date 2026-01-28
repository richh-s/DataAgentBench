code = """import json, statistics, re
from pathlib import Path

# Load citations data
with open(var_call_Jbz2EE5pdbBJCQ9iEvP9zKoE, 'r') as f:
    citations = json.load(f)

# Load paper docs data
with open(var_call_QyGJBX36y5XtgnvyeFh5ZIm1, 'r') as f:
    docs = json.load(f)

# Build a quick index of filename (without .txt) -> source via heuristic search in text
# We'll detect ACM papers by looking for typical ACM copyright/publisher strings.

def is_acm(text):
    if not text:
        return False
    t = text.lower()
    patterns = [
        'copyright 20',
        'acm 97',
        'acm 978',
        'request permissions from permissions@acm.org',
        'acm classification keywords',
        'permission to make digital or hard copies',
    ]
    return any(p in t for p in patterns)

acm_titles = set()
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    if is_acm(d.get('text','')):
        acm_titles.add(title)

# Collect citation counts for ACM papers in 2018
counts = []
for c in citations:
    title = c.get('title')
    if title in acm_titles:
        try:
            counts.append(int(c.get('citation_count')))
        except (TypeError, ValueError):
            pass

avg = statistics.mean(counts) if counts else 0

result = {
    'acm_paper_count': len(counts),
    'average_citation_count_2018': avg
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Jbz2EE5pdbBJCQ9iEvP9zKoE': 'file_storage/call_Jbz2EE5pdbBJCQ9iEvP9zKoE.json', 'var_call_QyGJBX36y5XtgnvyeFh5ZIm1': 'file_storage/call_QyGJBX36y5XtgnvyeFh5ZIm1.json'}

exec(code, env_args)
