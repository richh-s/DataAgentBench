code = """import json
import re

# Load all data
citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

print('Total 2018 citations: ' + str(len(citations_data)))
print('Total papers in collection: ' + str(len(papers_data)))

# List the filenames we have
print('Available paper files:')
for paper in papers_data:
    print('  - ' + paper.get('filename', 'NO FILENAME'))

# Create mapping of citation titles
citation_dict = {c['title'].strip().lower(): int(c['citation_count']) for c in citations_data}
print('\nSample citation titles:')
for i, title in enumerate(list(citation_dict.keys())[:5]):
    print('  - ' + title)

result = {
    'total_2018_citations': len(citations_data),
    'total_papers_available': len(papers_data),
    'available_filenames': [p.get('filename') for p in papers_data],
    'sample_citation_titles': list(citation_dict.keys())[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}, 'var_functions.execute_python:24': {'total_citations': 158, 'total_papers': 5, 'papers_dict_size': 5, 'sample_citation_title': 'expense control: a gamified, semi-automated, crowd-based approach for receipt capturing', 'sample_match_found': False}}

exec(code, env_args)
