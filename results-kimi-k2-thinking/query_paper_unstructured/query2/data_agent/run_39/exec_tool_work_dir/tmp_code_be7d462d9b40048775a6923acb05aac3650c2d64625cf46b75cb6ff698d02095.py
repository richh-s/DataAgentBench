code = """import json
import re

# Load citations data
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

# Load paper docs data  
paper_docs_data = locals()['var_functions.query_db:2']
if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

# Create sets for efficient lookup
citation_titles = set([item['title'] for item in citations_data])
paper_titles = set()
acm_papers = set()

# Process paper docs
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        paper_titles.add(title)
        
        text = doc.get('text', '')
        if re.search(r'\bACM\b', text, re.IGNORECASE):
            acm_papers.add(title)

# Find ACM papers that are in the 2018 citations
acm_papers_cited_in_2018 = []
for citation in citations_data:
    if citation['title'] in acm_papers:
        acm_papers_cited_in_2018.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count'])
        })

# Calculate average
if acm_papers_cited_in_2018:
    total_citations = sum(p['citation_count'] for p in acm_papers_cited_in_2018)
    avg_citations = total_citations / len(acm_papers_cited_in_2018)
else:
    total_citations = 0
    avg_citations = 0

# Prepare result
result = {
    'summary': {
        'total_2018_citations': len(citations_data),
        'total_paper_docs': len(paper_titles),
        'acm_papers_found': len(acm_papers),
        'acm_papers_cited_in_2018': len(acm_papers_cited_in_2018)
    },
    'average_citation_count': round(avg_citations, 2)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'acm_papers_count': 0, 'total_citations': 0, 'average_citation_count': 0, 'message': 'No ACM papers found in 2018 citations'}}

exec(code, env_args)
