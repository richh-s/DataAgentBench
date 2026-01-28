code = """import json
import os
import re

# Read the paper documents data
paper_docs_path = locals()['var_functions.query_db:4']
if isinstance(paper_docs_path, str) and os.path.exists(paper_docs_path):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = []

# Read the citations data  
citations_path = locals()['var_functions.query_db:5']
if isinstance(citations_path, str) and os.path.exists(citations_path):
    with open(citations_path, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = []

# Extract paper information (title, source, year, etc.)
acm_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is published by ACM
    # Look for ACM indicators in the text (case-insensitive)
    is_acm = 'ACM' in text or 'acm' in text.lower()
    
    if is_acm and title:  # Only process if it's ACM and has a title
        acm_papers.append(title)

# Convert citations to a dictionary for easy lookup
citations_dict = {}
for citation in citations_2018:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    if title:  # Only add if title is not empty
        citations_dict[title] = citation_count

# Find ACM papers that have citations in 2018
acm_citations = []
matched_papers = []

for paper_title in acm_papers:
    if paper_title in citations_dict:
        citation_count = citations_dict[paper_title]
        acm_citations.append(citation_count)
        matched_papers.append({
            'title': paper_title,
            'citation_count': citation_count
        })

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_cited': len(acm_citations),
        'total_citations': sum(acm_citations),
        'sample_matched_papers': matched_papers[:5]  # Show first 5 for verification
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_cited': 0,
        'total_citations': 0,
        'acm_papers_found': len(acm_papers),
        'citations_available': len(citations_dict),
        'message': 'No ACM papers found with citations in 2018'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'storage_keys': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5'], 'all_vars': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5', '__builtins__', 'json', 'os', 're', 'storage_keys']}, 'var_functions.execute_python:16': {'paper_docs_count': 99, 'citations_2018_count': 158, 'paper_docs_type': "<class 'str'>", 'citations_type': "<class 'str'>"}}

exec(code, env_args)
