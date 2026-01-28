code = """import json, re
from collections import defaultdict

# Load citations for 2020
path_citations = var_call_HjsjLve08fWZ6EFdYU8i5lrJ
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Build a map from title to citation_count (as int)
 citation_2020 = {c['title']: int(c['citation_count']) for c in citations}

# Load paper docs
path_docs = var_call_PjYc91RChnlAWx3S0o4TCIlm
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Helper to detect CHI venue from text
chi_patterns = [
    r"CHI '\d{2}",
    r"CHI \d{4}",
    r"ACM CHI",
    r"Conference on Human Factors in Computing Systems",
]

def is_chi(text):
    t = text.upper()
    for p in chi_patterns:
        if re.search(p, t, re.IGNORECASE):
            return True
    return False

# Map filename without .txt to whether it's CHI
chi_titles = set()
for d in docs:
    filename = d.get('filename','')
    text = d.get('text','')
    if not filename or not text:
        continue
    if is_chi(text):
        title = filename
        if title.lower().endswith('.txt'):
            title = title[:-4]
        chi_titles.add(title)

# Sum citation counts for titles that are CHI papers
 total_citations = 0
for title, count in citation_2020.items():
    if title in chi_titles:
        total_citations += count

result = total_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HjsjLve08fWZ6EFdYU8i5lrJ': 'file_storage/call_HjsjLve08fWZ6EFdYU8i5lrJ.json', 'var_call_NE52DDMJ601BTW5U4v5hQVjs': ['paper_docs'], 'var_call_PjYc91RChnlAWx3S0o4TCIlm': 'file_storage/call_PjYc91RChnlAWx3S0o4TCIlm.json'}

exec(code, env_args)
