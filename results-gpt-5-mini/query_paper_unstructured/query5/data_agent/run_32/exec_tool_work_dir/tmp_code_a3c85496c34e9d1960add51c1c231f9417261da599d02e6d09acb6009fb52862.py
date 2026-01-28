code = """import json
import re

# Load data files from storage
with open(var_call_Z3DAHvLOiNBp2rzBdZmAhv5Z, 'r') as f:
    citations = json.load(f)

with open(var_call_J73C9B5EDplrGMJwk7MazD5K, 'r') as f:
    docs = json.load(f)

# Build set of titles (filename without .txt) that are CHI papers
chi_titles = set()
chi_pattern = re.compile(r"\bCHI\b", re.IGNORECASE)
for d in docs:
    text = d.get('text', '')
    if chi_pattern.search(text):
        fn = d.get('filename', '')
        if fn.endswith('.txt'):
            title = fn[:-4]
        else:
            title = fn
        chi_titles.add(title)

# Filter citations for 2020 (citations list already filtered earlier) and for CHI titles
matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles:
        matched.append({'title': title, 'citation_count': count})
        total += count

# Sort matched list by citation_count descending
matched.sort(key=lambda x: x['citation_count'], reverse=True)

result = {'total_citations_for_CHI_papers_in_2020': total, 'papers': matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Z3DAHvLOiNBp2rzBdZmAhv5Z': 'file_storage/call_Z3DAHvLOiNBp2rzBdZmAhv5Z.json', 'var_call_GPczZFUsXMw7LgUTBsasBvON': 'file_storage/call_GPczZFUsXMw7LgUTBsasBvON.json', 'var_call_J73C9B5EDplrGMJwk7MazD5K': 'file_storage/call_J73C9B5EDplrGMJwk7MazD5K.json'}

exec(code, env_args)
