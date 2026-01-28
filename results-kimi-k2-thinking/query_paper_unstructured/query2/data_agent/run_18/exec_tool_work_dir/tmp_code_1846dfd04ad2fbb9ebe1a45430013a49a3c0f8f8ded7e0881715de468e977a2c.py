code = """import json
import re

# Access the stored data
citations_data = globals()['var_functions.query_db:32']
papers_data = globals()['var_functions.query_db:34']

# Create mapping of paper titles to their sources
paper_sources = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    sources = []
    # Check for ACM in the text
    if 'ACM' in text:
        sources.append('ACM')
    # Check for IEEE
    if 'IEEE' in text:
        sources.append('IEEE')
    # Check for PubMed
    if 'PubMed' in text.lower():
        sources.append('PubMed')
    
    if sources:
        paper_sources[title] = sources

# Match citations with paper sources and calculate statistics
acm_citations = []
all_citation_counts = []

for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    all_citation_counts.append(count)
    
    # Check if this paper has ACM as a source
    if title in paper_sources and 'ACM' in paper_sources[title]:
        acm_citations.append(count)

# Calculate average citation counts
total_papers = len(citations_data)
acm_paper_count = len(acm_citations)
average_acm = sum(acm_citations) / acm_paper_count if acm_paper_count > 0 else 0
average_all = sum(all_citation_counts) / len(all_citation_counts) if all_citation_counts else 0

# Prepare final result
result = {
    'total_papers_cited_in_2018': total_papers,
    'acm_papers_identified': acm_paper_count,
    'average_citation_count_acm_papers': round(average_acm, 2),
    'average_citation_count_all_papers': round(average_all, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'status': 'checking_variables'}, 'var_functions.execute_python:30': {'status': 'variable_check_complete'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': {'status': 'variable_search_complete'}}

exec(code, env_args)
