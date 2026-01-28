code = """import json
import re

# Load citation data for 2018
citations_file = var_functions.query_db:0
citations_2018 = []
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = var_functions.query_db:0

# Load paper documents
papers_file = var_functions.query_db:2
paper_docs = []
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:2

# Create a mapping of paper titles to their documents for faster lookup
papers_by_title = {}
for paper in paper_docs:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    papers_by_title[title] = paper

# Process each citation and check if it was published by ACM
acm_citations = []

for citation in citations_2018:
    citation_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Find the corresponding paper document
    paper_doc = papers_by_title.get(citation_title, None)
    
    if paper_doc:
        text = paper_doc.get('text', '')
        
        # Check if the paper is published by ACM
        is_acm = False
        
        # Look for ACM patterns
        text_upper = text.upper()
        
        # Check for ACM-specific indicators
        if 'ACM' in text_upper:
            # Check for ACM copyright/permission statements
            if 'Permission' in text and 'ACM' in text:
                is_acm = True
            # Check for ACM DOI pattern
            elif '10.1145' in text:  # ACM DOI prefix
                is_acm = True
            # Check for ACM Classification
            elif 'ACM Classification' in text:
                is_acm = True
        
        if is_acm:
            acm_citations.append({
                'title': citation_title,
                'citation_count': citation_count
            })

# Calculate average citation count for ACM papers
if acm_citations:
    total_citations = sum(c['citation_count'] for c in acm_citations)
    avg_citations = total_citations / len(acm_citations)
else:
    avg_citations = None

result = {
    'total_acm_papers': len(acm_citations),
    'average_citation_count': avg_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
