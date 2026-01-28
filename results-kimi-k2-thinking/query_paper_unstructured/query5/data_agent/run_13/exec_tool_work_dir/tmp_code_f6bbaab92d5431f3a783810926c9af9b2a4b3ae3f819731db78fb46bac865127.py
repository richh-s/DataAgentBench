code = """import json
import re

# Load citations data
citation_file = locals()['var_functions.query_db:5']
if isinstance(citation_file, str) and citation_file.endswith('.json'):
    with open(citation_file, 'r') as f:
        citations = json.load(f)
else:
    citations = locals()['var_functions.query_db:5']

# Load papers data
paper_file = locals()['var_functions.query_db:6']
if isinstance(paper_file, str) and paper_file.endswith('.json'):
    with open(paper_file, 'r') as f:
        papers = json.load(f)
else:
    papers = locals()['var_functions.query_db:6']

print('Loaded %d papers and %d citations' % (len(papers), len(citations)))

# Find CHI papers by checking if 'CHI' appears in text
chi_papers = []
for p in papers:
    text = p.get('text', '')
    if 'CHI' in text or 'Human Factors in Computing Systems' in text:
        title = p.get('filename', '').replace('.txt', '')
        chi_papers.append(title)

print('Found %d CHI papers' % len(chi_papers))

# Sum 2020 citations for CHI papers
total = 0
count = 0
for c in citations:
    if isinstance(c, dict) and int(c.get('citation_year', 0)) == 2020:
        cite_title = c.get('title', '')
        if cite_title in chi_papers:
            total += int(c.get('citation_count', 0))
            count += 1

print('Matched %d papers, total citations = %d' % (count, total))
result = {'total_citations_2020': total, 'chi_papers_cited': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'total_citations': 243, 'papers_count': 4}}

exec(code, env_args)
