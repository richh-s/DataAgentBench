code = """import json

# Read the citations data for 2018
citations_file = var_functions.query_db_32
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper documents data
papers_file = var_functions.query_db_34
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Create a dictionary mapping paper titles to their sources
paper_sources = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    sources = []
    if 'ACM' in text:
        sources.append('ACM')
    if 'IEEE' in text:
        sources.append('IEEE')
    if 'PubMed' in text.lower():
        sources.append('PubMed')
    
    if sources:
        paper_sources[title] = sources

# Match citations with paper sources and filter for ACM papers
acm_citations = []
all_citation_counts = []

for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    all_citation_counts.append(count)
    
    if title in paper_sources and 'ACM' in paper_sources[title]:
        acm_citations.append(count)

# Calculate statistics
total_papers = len(citations_data)
acm_count = len(acm_citations)
avg_acm = sum(acm_citations) / acm_count if acm_count > 0 else 0
avg_all = sum(all_citation_counts) / len(all_citation_counts) if all_citation_counts else 0

# Prepare result
result = {
    'total_papers_cited_in_2018': total_papers,
    'acm_papers_identified': acm_count,
    'average_citation_count_acm_papers': round(avg_acm, 2),
    'average_citation_count_all_papers': round(avg_all, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'status': 'checking_variables'}, 'var_functions.execute_python:30': {'status': 'variable_check_complete'}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
