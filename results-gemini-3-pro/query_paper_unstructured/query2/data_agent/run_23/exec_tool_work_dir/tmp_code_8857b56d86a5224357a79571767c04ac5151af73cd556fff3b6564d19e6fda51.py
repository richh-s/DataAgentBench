code = """import json

# Load citations
# The key is var_function-call-17141929478925860109
with open(locals()['var_function-call-17141929478925860109'], 'r') as f:
    citations = json.load(f)

# Load paper docs
# The key is var_function-call-2705178407937486249
with open(locals()['var_function-call-2705178407937486249'], 'r') as f:
    papers = json.load(f)

acm_titles = set()
for p in papers:
    text = p.get('text', '')
    if not text:
        continue
    # Check for ACM in the first 5000 characters
    # This covers headers, abstract, and typically the copyright footer on the first page
    head_text = text[:5000]
    if "ACM" in head_text:
        # Check if it's not a false positive (unlikely in header unless referencing ACM)
        # But commonly "Copyright ... ACM" or "Permission ... ACM" or "ACM Classification"
        title = p['filename'].replace('.txt', '')
        acm_titles.add(title)

cited_acm_counts = []
for c in citations:
    title = c['title']
    # Check exact match
    if title in acm_titles:
        cited_acm_counts.append(int(c['citation_count']))

result = 0.0
if cited_acm_counts:
    result = sum(cited_acm_counts) / len(cited_acm_counts)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17141929478925860109': 'file_storage/function-call-17141929478925860109.json', 'var_function-call-17141929478925860542': 'file_storage/function-call-17141929478925860542.json', 'var_function-call-2705178407937486249': 'file_storage/function-call-2705178407937486249.json'}

exec(code, env_args)
