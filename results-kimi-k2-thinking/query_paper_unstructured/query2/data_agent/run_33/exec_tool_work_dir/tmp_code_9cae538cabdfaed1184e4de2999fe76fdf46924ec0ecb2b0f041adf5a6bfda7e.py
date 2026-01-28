code = """import json
import re

# Load the citation data for 2018 from stored results
citation_data = locals()['var_functions.query_db:0']
# Handle both direct data and file path
if isinstance(citation_data, str) and citation_data.endswith('.json'):
    with open(citation_data, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citation_data

# Load the paper documents data
paper_docs_data = locals()['var_functions.query_db:5']
# Handle both direct data and file path
if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Create a dictionary for citation data with title as key for easy lookup
citation_dict = {}
for item in citations_2018:
    title = item.get('title', '')
    citation_count = int(item.get('citation_count', 0))
    citation_dict[title] = citation_count

# Process paper documents to extract titles and identify ACM papers
acm_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if the paper was published by ACM
    # Look for ACM references in the text
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        # Additional check: look for ACM copyright or publication notice
        acm_patterns = [
            r'ACM\s+\d{4}',  # ACM with year
            r'Association for Computing Machinery',  # Full name
            r'Permission to make digital or hard copies.*ACM',  # Copyright notice
            r'ACM\s+Classification',  # ACM classification
            r'Published by ACM'  # Publication notice
        ]
        
        is_acm = False
        for pattern in acm_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_acm = True
                break
        
        if is_acm and title in citation_dict:
            acm_papers.append({
                'title': title,
                'citation_count': citation_dict[title]
            })

# Calculate average citation count for ACM papers
if acm_papers:
    total_citations = sum(paper['citation_count'] for paper in acm_papers)
    average_citations = total_citations / len(acm_papers)
    
    result = {
        'average_citation_count': round(average_citations, 2),
        'total_acm_papers': len(acm_papers),
        'total_citations': total_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
