code = """import json, re
# Load citations (2020) and papers
with open(var_call_clUmDxoXhXkk75ik6VU6Rg6E, 'r') as f:
    citations = json.load(f)
with open(var_call_n1BHQo02P4bBrod5pPoYjyyw, 'r') as f:
    papers = json.load(f)

# Build filename -> paper map
paper_map = {p['filename']: p for p in papers}

# Find all papers whose text contains 'CHI' (case-insensitive)
chi_filenames = []
for p in papers:
    text = p.get('text','')
    if re.search(r'\bCHI\b', text, re.IGNORECASE):
        chi_filenames.append(p['filename'])

# Now match citations titles to these filenames
chi_citations = []
chi_set = set([fn[:-4] for fn in chi_filenames])  # remove .txt
for rec in citations:
    title = rec['title']
    if title in chi_set:
        try:
            count = int(rec['citation_count'])
        except:
            try:
                count = int(float(rec['citation_count']))
            except:
                count = 0
        chi_citations.append({'title': title, 'citation_count': count})

total = sum(c['citation_count'] for c in chi_citations)
result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_CHI_papers': len(chi_citations),
    'CHI_papers': chi_citations
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_clUmDxoXhXkk75ik6VU6Rg6E': 'file_storage/call_clUmDxoXhXkk75ik6VU6Rg6E.json', 'var_call_ctjReNTaVANGYMn2boLQJjyr': 'file_storage/call_ctjReNTaVANGYMn2boLQJjyr.json', 'var_call_n1BHQo02P4bBrod5pPoYjyyw': 'file_storage/call_n1BHQo02P4bBrod5pPoYjyyw.json', 'var_call_QjxGHyhNrnX1WqyCs5Aw9t0t': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers': 0, 'CHI_papers': []}}

exec(code, env_args)
