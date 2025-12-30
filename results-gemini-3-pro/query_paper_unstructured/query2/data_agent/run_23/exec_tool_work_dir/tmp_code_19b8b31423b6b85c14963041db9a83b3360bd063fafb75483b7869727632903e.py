code = """import json
import re

# Load citations
with open(locals()['var_function-call-17141929478925860109'], 'r') as f:
    citations = json.load(f)

# Load paper docs
with open(locals()['var_function-call-2705178407937486249'], 'r') as f:
    papers = json.load(f)

acm_titles = set()
for p in papers:
    text = p.get('text', '')
    if not text:
        continue
    head = text[:5000]
    
    # Check for definitive ACM markers
    # 1. "© ACM"
    # 2. "permissions@acm.org"
    if "© ACM" in head or "permissions@acm.org" in head:
        acm_titles.add(p['filename'].replace('.txt', ''))
        continue
    
    # 3. "Copyright ... ACM" (case insensitive)
    if re.search(r'copyright.{0,50}ACM', head, re.IGNORECASE):
        acm_titles.add(p['filename'].replace('.txt', ''))
        continue

    # Fallback: if "ACM" is there but not "IEEE"
    # This handles cases where copyright might be formatted differently but source is ACM
    if "ACM" in head and "IEEE" not in head:
        acm_titles.add(p['filename'].replace('.txt', ''))

cited_acm_counts = []
for c in citations:
    if c['title'] in acm_titles:
        cited_acm_counts.append(int(c['citation_count']))

result = 0.0
if cited_acm_counts:
    result = sum(cited_acm_counts) / len(cited_acm_counts)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17141929478925860109': 'file_storage/function-call-17141929478925860109.json', 'var_function-call-17141929478925860542': 'file_storage/function-call-17141929478925860542.json', 'var_function-call-2705178407937486249': 'file_storage/function-call-2705178407937486249.json', 'var_function-call-520291134195266981': 68.5}

exec(code, env_args)
