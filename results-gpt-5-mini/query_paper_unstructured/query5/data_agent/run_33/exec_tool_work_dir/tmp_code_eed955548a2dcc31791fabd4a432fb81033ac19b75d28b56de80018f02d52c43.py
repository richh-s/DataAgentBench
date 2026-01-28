code = """import json, re
# Load citations list
with open(var_call_clUmDxoXhXkk75ik6VU6Rg6E, 'r') as f:
    citations = json.load(f)
# Load paper docs list
with open(var_call_n1BHQo02P4bBrod5pPoYjyyw, 'r') as f:
    papers = json.load(f)

# Build a map from filename to paper record
paper_map = {p['filename']: p for p in papers}

chi_citations = []
for rec in citations:
    title = rec['title']
    filename = title + '.txt'
    paper = paper_map.get(filename)
    if not paper:
        continue
    text = paper.get('text', '')
    header = text[:1000].upper()
    # Heuristic: CHI appears as a whole word in header or phrases like 'CHI '
    if re.search(r'\bCHI\b', header):
        # Also ensure it's not CHI referenced in citations header of another venue (best effort)
        # We'll accept it as CHI paper
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

env_args = {'var_call_clUmDxoXhXkk75ik6VU6Rg6E': 'file_storage/call_clUmDxoXhXkk75ik6VU6Rg6E.json', 'var_call_ctjReNTaVANGYMn2boLQJjyr': 'file_storage/call_ctjReNTaVANGYMn2boLQJjyr.json', 'var_call_n1BHQo02P4bBrod5pPoYjyyw': 'file_storage/call_n1BHQo02P4bBrod5pPoYjyyw.json'}

exec(code, env_args)
