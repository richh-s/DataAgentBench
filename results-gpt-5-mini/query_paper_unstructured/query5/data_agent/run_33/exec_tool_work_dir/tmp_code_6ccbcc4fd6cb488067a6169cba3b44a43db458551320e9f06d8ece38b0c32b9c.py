code = """import json
# Load citations list
with open(var_call_clUmDxoXhXkk75ik6VU6Rg6E, 'r') as f:
    citations = json.load(f)
# Load paper docs list
with open(var_call_n1BHQo02P4bBrod5pPoYjyyw, 'r') as f:
    papers = json.load(f)

# Build a map from filename to paper record
paper_map = {p['filename']: p for p in papers}

# Filter citations to those whose title corresponds to a CHI paper in paper_docs
# Need to extract venue from paper text. We'll check if '\nCHI' or 'CHI' occurs in the text near top.
chi_titles = []
chi_citations = []
for rec in citations:
    title = rec['title']
    filename = title + '.txt'
    paper = paper_map.get(filename)
    if not paper:
        continue
    text = paper.get('text','').upper()
    # Simple heuristic: check if 'CHI' appears in the first 300 chars or 'CHI ' or 'CHI,' or "CHI'"
    header = text[:1000]
    if 'CHI' in header:
        chi_titles.append(title)
        chi_citations.append({'title': title, 'citation_count': int(rec['citation_count'])})

# Sum total citation counts for CHI papers
total = sum([c['citation_count'] for c in chi_citations])

result = {'total_citations_2020_for_CHI_papers': total, 'num_CHI_papers': len(chi_citations)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_clUmDxoXhXkk75ik6VU6Rg6E': 'file_storage/call_clUmDxoXhXkk75ik6VU6Rg6E.json', 'var_call_ctjReNTaVANGYMn2boLQJjyr': 'file_storage/call_ctjReNTaVANGYMn2boLQJjyr.json', 'var_call_n1BHQo02P4bBrod5pPoYjyyw': 'file_storage/call_n1BHQo02P4bBrod5pPoYjyyw.json'}

exec(code, env_args)
