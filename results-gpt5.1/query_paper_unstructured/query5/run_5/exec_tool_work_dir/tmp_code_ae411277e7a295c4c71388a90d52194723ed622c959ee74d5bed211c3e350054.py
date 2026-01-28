code = """import json, pandas as pd

# Load full citation results
path_citations = var_call_rMPCvJzbXsmD4s4HMtB2CRTL
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load full paper docs results
path_docs = var_call_8BjrgoixABW8sPa9rRTffqUH
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Build a set of CHI titles from docs by detecting 'CHI' in the text metadata lines
chi_titles = set()
for d in docs:
    text = d.get('text', '')
    header = text[:1000].upper()
    if ' CHI ' in header or "CHI '" in header or '\nCHI ' in header:
        filename = d.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Sum citation counts for 2020 for titles that are CHI papers
chi_citation_total = 0
for c in citations:
    title = c.get('title')
    if title in chi_titles:
        try:
            chi_citation_total += int(c.get('citation_count', 0))
        except (TypeError, ValueError):
            continue

result = chi_citation_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rMPCvJzbXsmD4s4HMtB2CRTL': 'file_storage/call_rMPCvJzbXsmD4s4HMtB2CRTL.json', 'var_call_8BjrgoixABW8sPa9rRTffqUH': 'file_storage/call_8BjrgoixABW8sPa9rRTffqUH.json'}

exec(code, env_args)
