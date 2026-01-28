code = """import json
import re

citation_data = locals()['var_functions.query_db:0']
paper_data = locals()['var_functions.query_db:5']

# Handle file paths
if isinstance(citation_data, str):
    with open(citation_data, 'r') as f:
        citation_data = json.load(f)
if isinstance(paper_data, str):
    with open(paper_data, 'r') as f:
        paper_data = json.load(f)

chi_titles = {}
for paper in paper_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for CHI patterns
    if re.search(r'CHI', text, re.IGNORECASE):
        normalized = title.lower().strip()
        chi_titles[normalized] = title
        chi_titles[re.sub(r'[^a-z0-9\s]', '', normalized)] = title

total = 0
matched = 0
for cit in citation_data:
    title = cit.get('title', '').lower().strip()
    count = int(cit.get('citation_count', 0))
    
    if title in chi_titles or re.sub(r'[^a-z0-9\s]', '', title) in chi_titles:
        total += count
        matched += 1

result = {'total_citation_count': total, 'chi_papers_cited': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
