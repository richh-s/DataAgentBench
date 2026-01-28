code = """import json
import re

# Load citations data
citations_file = var_functions.query_db:0
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = var_functions.query_db:0

# Load paper docs data  
paper_docs_file = var_functions.query_db:2
if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs_data = json.load(f)
else:
    paper_docs_data = var_functions.query_db:2

print(f"Number of citations in 2018: {len(citations_data)}")
print(f"Number of paper documents: {len(paper_docs_data)}")

# Create a dictionary for citations keyed by title for easy lookup
citations_dict = {item['title']: int(item['citation_count']) for item in citations_data}

# Extract paper information from MongoDB documents
acm_papers = []

for doc in paper_docs_data:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Get text content
    text = doc.get('text', '')
    
    # Look for ACM in the text (source/publisher)
    # Common patterns: ACM, ACM Classification, ACM References, etc.
    if re.search(r'\bACM\b', text, re.IGNORECASE):
        # Check if this paper has citations in 2018
        if title in citations_dict:
            acm_papers.append({
                'title': title,
                'citation_count': citations_dict[title],
                'source': 'ACM'
            })

print(f"Number of ACM papers cited in 2018: {len(acm_papers)}")

if acm_papers:
    # Calculate average citation count
    total_citations = sum(paper['citation_count'] for paper in acm_papers)
    avg_citations = total_citations / len(acm_papers)
    
    result = {
        'acm_papers_count': len(acm_papers),
        'total_citations': total_citations,
        'average_citation_count': round(avg_citations, 2)
    }
else:
    result = {
        'acm_papers_count': 0,
        'total_citations': 0,
        'average_citation_count': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
