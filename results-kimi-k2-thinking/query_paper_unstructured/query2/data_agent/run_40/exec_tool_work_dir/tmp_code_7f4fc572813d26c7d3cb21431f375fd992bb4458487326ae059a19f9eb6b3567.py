code = """import json
import re

# Get citations data for 2018 (158 records)
citation_data_key = 'var_functions.query_db:0'
citations_2018 = locals().get(citation_data_key)

if isinstance(citations_2018, str) and citations_2018.endswith('.json'):
    with open(citations_2018, 'r') as f:
        citations_2018 = json.load(f)

# Get paper documents (only 5 documents)
paper_data_key = 'var_functions.query_db:2'
paper_docs = locals().get(paper_data_key)

if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Process paper documents to identify ACM papers
acm_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if this is an ACM paper
    is_acm = False
    
    # Look for ACM patterns
    acm_patterns = [
        r'ACM\s+Classification',
        r'Copyright\s+\d{4}\s+ACM',
        r'ACM\s+[^\s]*\d{4}',
        r'Association for Computing Machinery',
        r'ACM\s+Digital Library',
        r'Permission[^.]*ACM[^.]*\.',
        r'UBICOMP\s*.?\s*\d{4}.*ACM',  # Ubicomp is ACM
        r'CHI\s*.?\s*\d{4}.*ACM',      # CHI is ACM
    ]
    
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_acm = True
            break
    
    if is_acm:
        acm_papers.append(title)

# Create a mapping of titles to ACM status
acm_titles = set(acm_papers)

# Join with citations
acm_citations = []
for citation in citations_2018:
    cit_title = citation.get('title', '')
    
    # Check if this is an ACM paper
    if cit_title in acm_titles:
        acm_citations.append({
            'title': cit_title,
            'citation_count': int(citation.get('citation_count', 0))
        })

# Calculate average
if acm_citations:
    total_citations = sum(c['citation_count'] for c in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'acm_papers_count': len(acm_citations),
        'total_citations': total_citations,
        'acm_papers': acm_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'acm_papers_count': 0,
        'total_citations': 0,
        'acm_papers': []
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json'}

exec(code, env_args)
