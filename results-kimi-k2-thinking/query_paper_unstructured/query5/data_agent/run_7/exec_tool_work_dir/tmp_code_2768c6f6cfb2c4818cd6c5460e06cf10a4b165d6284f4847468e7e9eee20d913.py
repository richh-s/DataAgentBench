code = """import json
import re

citations_file_path = locals()['var_functions.query_db:12']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

print('Total citations loaded:', len(citations_data))

papers_file_path = locals()['var_functions.query_db:14']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

print('Papers found:', len(papers_data))

# Create a set of paper titles from CHI papers for matching
chi_paper_titles = []
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    chi_paper_titles.append(title)

print('CHI papers titles count:', len(chi_paper_titles))

# Match with citations
matched_citations = []
for citation in citations_data:
    cit_title = citation.get('title', '')
    cit_count = int(citation.get('citation_count', 0))
    
    # Check if citation title matches any CHI paper title
    for paper_title in chi_paper_titles:
        if paper_title.lower().strip() == cit_title.lower().strip():
            matched_citations.append({
                'title': cit_title,
                'count': cit_count
            })
            break

print('Matched citations:', len(matched_citations))

# Calculate total
if matched_citations:
    total_citations = sum(c['count'] for c in matched_citations)
    print('Total citations for CHI papers:', total_citations)
else:
    print('No matches found with simple title matching')

print('__RESULT__:')
result = {
    'matched_citations': matched_citations,
    'count': len(matched_citations)
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'status': 'ready_to_query_mongodb', 'citation_count': 188}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'status': 'papers_loaded', 'count': 99}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
