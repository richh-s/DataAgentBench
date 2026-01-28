code = """import json
import re

# Load data directly from the query results which should be in storage
# Based on the keys provided in previous outputs

# First, let's see what's actually in storage
storage_keys = []
for key in sorted(locals().keys()):
    if not key.startswith('__'):
        storage_keys.append(key)

print("Storage keys found:", storage_keys)

# Try to find our data keys
citations_key = None
papers_key = None

for key in storage_keys:
    if 'query_db' in key and '0' in key:
        citations_key = key
    elif 'query_db' in key and '8' in key:
        papers_key = key

print("Citations key:", citations_key)
print("Papers key:", papers_key)

if citations_key and papers_key:
    citations_data = locals()[citations_key]
    papers_data = locals()[papers_key]
    
    print("Citation data type:", type(citations_data))
    print("Paper data type:", type(papers_data))
    
    # If they're file paths, load them
    if isinstance(citations_data, str) and '.json' in citations_data:
        with open(citations_data, 'r') as f:
            citations_data = json.load(f)
    
    if isinstance(papers_data, str) and '.json' in papers_data:
        with open(papers_data, 'r') as f:
            papers_data = json.load(f)
    
    print(f"Citations count: {len(citations_data)}")
    print(f"Papers count: {len(papers_data)}")
    
    # Process paper documents to find ACM papers and create lookup
    acm_papers = {}
    for paper in papers_data:
        filename = paper.get('filename', '')
        text = paper.get('text', '')
        
        title = filename.replace('.txt', '') if filename else ''
        if not title:
            continue
            
        # Check if this is an ACM paper
        is_acm = bool(re.search(r'ACM', text, re.IGNORECASE))
        if is_acm:
            normalized_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            acm_papers[normalized_title] = {
                'title': title,
                'source': 'ACM'
            }
    
    print(f"Found {len(acm_papers)} ACM papers")
    
    # Match citations with ACM papers
    acm_citations = []
    for citation in citations_data:
        citation_title = citation.get('title', '')
        citation_count = int(citation.get('citation_count', 0))
        
        if citation_title:
            normalized_citation_title = re.sub(r'[^a-zA-Z0-9]', '', citation_title.lower())
            if normalized_citation_title in acm_papers:
                acm_citations.append(citation_count)
    
    print(f"Found {len(acm_citations)} ACM citations in 2018")
    
    # Calculate average
    if acm_citations:
        avg_citations = sum(acm_citations) / len(acm_citations)
        result = {
            'average_citation_count': round(avg_citations, 2),
            'total_acm_papers_cited': len(acm_citations),
            'total_citation_count': sum(acm_citations)
        }
    else:
        result = {
            'average_citation_count': 0,
            'total_acm_papers_cited': 0,
            'total_citation_count': 0,
            'note': 'No ACM papers found in 2018 citations'
        }
else:
    result = {'error': 'Could not find query results'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:4': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'average_citation_count': 0, 'total_acm_papers': 0, 'total_citations': 0}, 'var_functions.execute_python:26': {'status': 'checked variables'}}

exec(code, env_args)
