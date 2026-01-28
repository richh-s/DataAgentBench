code = """import json, os, re
from collections import defaultdict

# Load citations result
citations_path = var_call_LtjYPUNTqohvirJnPiBpbwS8
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Map title -> total_citations for 2020
cit_by_title = {rec['title']: int(rec['total_citations']) for rec in citations}

# Load paper docs metadata
papers_path = var_call_sRJwWmRik2QFrbOIGyOrDplW
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Helper to detect CHI venue from text (very rough heuristic)
chi_pattern = re.compile(r"CHI '\d{2}|ACM CHI|CHI Conference on Human Factors in Computing Systems", re.IGNORECASE)

chi_titles = set()
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = os.path.splitext(filename)[0]
    if chi_pattern.search(text):
        chi_titles.add(title)

# Sum citations for CHI papers cited in 2020
total = 0
for title, c in cit_by_title.items():
    if title in chi_titles:
        total += c

result = total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LtjYPUNTqohvirJnPiBpbwS8': 'file_storage/call_LtjYPUNTqohvirJnPiBpbwS8.json', 'var_call_sRJwWmRik2QFrbOIGyOrDplW': 'file_storage/call_sRJwWmRik2QFrbOIGyOrDplW.json'}

exec(code, env_args)
