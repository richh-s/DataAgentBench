code = """import json
import re

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers data  
papers_path = locals()['var_functions.query_db:4']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Build ACM papers dictionary
acm_papers = {}
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    if 'ACM' in paper['text']:
        acm_papers[title] = True

# Find ACM citations from 2018
acm_citation_counts = []
for citation in citations:
    cit_title = citation['title']
    if cit_title in acm_papers:
        acm_citation_counts.append(int(citation['citation_count']))

# Calculate average
if acm_citation_counts:
    avg = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg = 0

result = {
    'total_citations_2018': len(citations),
    'acm_citations_found': len(acm_citation_counts),
    'average_citation_count': round(avg, 2),
    'acm_citations': acm_citation_counts
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': {'total_citations_2018': 158, 'acm_papers_count': 2, 'average_citation_count': 68.5, 'acm_citations_list': [50, 87]}, 'var_functions.execute_python:14': {'total_citations_2018': 158, 'acm_papers_in_corpus': 5, 'exact_matches': 2, 'close_matches': 2}}

exec(code, env_args)
