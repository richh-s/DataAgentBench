code = """import json
import re

# Load data
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
print('Total papers: ' + str(len(papers_data)))

# Build papers dictionary using filename as key
papers_dict = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    if filename:
        title_key = filename.replace('.txt', '').strip().lower()
        papers_dict[title_key] = paper

print('Papers in dictionary: ' + str(len(papers_dict)))

# Check sample match
sample_citation = citations_data[0]
sample_title = sample_citation['title'].strip().lower()
print('Sample citation title: ' + sample_title)
print('Has matching paper: ' + str(sample_title in papers_dict))

result = {
    'total_citations': len(citations_data),
    'total_papers': len(papers_data),
    'papers_dict_size': len(papers_dict),
    'sample_citation_title': sample_title,
    'sample_match_found': sample_title in papers_dict
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_2018_citations': 158, 'missing_papers': 156, 'average_citations': 68.5, 'total_citations_for_acm_papers': 137}}

exec(code, env_args)
