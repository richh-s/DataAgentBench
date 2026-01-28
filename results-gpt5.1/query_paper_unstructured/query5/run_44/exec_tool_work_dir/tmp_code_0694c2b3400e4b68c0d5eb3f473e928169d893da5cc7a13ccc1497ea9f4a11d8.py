code = """import json, os, re

# Load citations for 2020
citations_2020 = var_call_YGt8w86jZMC1KUhw3nksVKe0

# Load paper docs (possibly from file if it's a path string)
def load_docs(obj):
    if isinstance(obj, str) and os.path.isfile(obj):
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

paper_docs = load_docs(var_call_HRRRhOrJJKKI1iz5wjKsUzZE)

# Build a mapping from title (filename without .txt) to venue by regex search in text
chi_titles = set()
for doc in paper_docs:
    filename = doc.get('filename') or ''
    if not filename.lower().endswith('.txt'):
        continue
    title = filename[:-4]
    text = doc.get('text') or ''
    # Heuristic: treat as CHI paper if ' CHI ' or "CHI '" appears near the top or with ACM reference
    head = text[:1000].upper()
    if ' CHI ' in head or "CHI '" in head or '\nCHI ' in head:
        chi_titles.add(title)

# Sum citation counts for 2020 where title is in chi_titles
chi_citation_total = 0
for rec in citations_2020:
    title = rec['title']
    if title in chi_titles:
        try:
            chi_citation_total += int(rec['citation_count'])
        except Exception:
            pass

result = chi_citation_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YGt8w86jZMC1KUhw3nksVKe0': 'file_storage/call_YGt8w86jZMC1KUhw3nksVKe0.json', 'var_call_HRRRhOrJJKKI1iz5wjKsUzZE': 'file_storage/call_HRRRhOrJJKKI1iz5wjKsUzZE.json'}

exec(code, env_args)
