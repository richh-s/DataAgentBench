code = """import json, os

citations_2020 = var_call_YGt8w86jZMC1KUhw3nksVKe0

def load_docs(obj):
    if isinstance(obj, str) and os.path.isfile(obj):
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

paper_docs = load_docs(var_call_HRRRhOrJJKKI1iz5wjKsUzZE)

chi_titles = set()
for doc in paper_docs:
    filename = doc.get('filename') or ''
    if not filename.lower().endswith('.txt'):
        continue
    title = filename[:-4]
    text = (doc.get('text') or '').upper()
    head = text[:1000]
    if ' CHI ' in head or "CHI '" in head or '\nCHI ' in head:
        chi_titles.add(title)

chi_citation_total = 0
for rec in citations_2020:
    title = rec.get('title')
    if title in chi_titles:
        try:
            chi_citation_total += int(rec.get('citation_count', 0))
        except Exception:
            pass

print("__RESULT__:")
print(json.dumps(chi_citation_total))"""

env_args = {'var_call_YGt8w86jZMC1KUhw3nksVKe0': 'file_storage/call_YGt8w86jZMC1KUhw3nksVKe0.json', 'var_call_HRRRhOrJJKKI1iz5wjKsUzZE': 'file_storage/call_HRRRhOrJJKKI1iz5wjKsUzZE.json'}

exec(code, env_args)
