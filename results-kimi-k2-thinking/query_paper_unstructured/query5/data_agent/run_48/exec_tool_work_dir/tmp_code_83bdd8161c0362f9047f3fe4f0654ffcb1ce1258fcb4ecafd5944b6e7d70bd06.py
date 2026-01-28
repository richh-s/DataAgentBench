code = """import json, re

citation_data = var_functions.query_db:0
paper_data = var_functions.query_db:5

if isinstance(citation_data, str) and citation_data.endswith('.json'):
    with open(citation_data, 'r') as f:
        citation_data = json.load(f)

if isinstance(paper_data, str) and paper_data.endswith('.json'):
    with open(paper_data, 'r') as f:
        paper_data = json.load(f)

chi_titles = set()
for paper in paper_data:
    text = paper.get('text', '')
    if re.search(r'CHI', text, re.IGNORECASE):
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        if title:
            chi_titles.add(title.lower().strip())

total = 0
matches = 0
for cit in citation_data:
    cit_title = cit.get('title', '').lower().strip()
    cit_count = int(cit.get('citation_count', 0))
    if cit_title in chi_titles or re.sub(r'[^a-z0-9\s]', '', cit_title) in {re.sub(r'[^a-z0-9\s]', '', t) for t in chi_titles}:
        total += cit_count
        matches += 1

result = {'total_citation_count': total, 'chi_papers_cited': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
