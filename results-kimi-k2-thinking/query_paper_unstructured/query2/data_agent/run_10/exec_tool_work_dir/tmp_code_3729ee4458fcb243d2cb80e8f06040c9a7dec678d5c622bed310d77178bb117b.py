code = """import json
import pandas as pd

# Load citations data
citations_file = var_functions.query_db:0
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents data
papers_file = var_functions.query_db:4
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total citations in 2018: {len(citations_2018)}")
print(f"Total paper documents: {len(paper_docs)}")

# Extract paper info from documents
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Determine source by looking for publisher patterns in text
    source = None
    text_lower = text.lower()
    
    # Check for ACM patterns
    if 'acm' in text_lower or 'doi.org/10.1145' in text_lower:
        source = 'ACM'
    elif 'ieee' in text_lower:
        source = 'IEEE'
    elif 'pubmed' in text_lower:
        source = 'PubMed'
    else:
        # Default or unknown
        source = 'Unknown'
    
    paper_info.append({
        'title': title,
        'source': source
    })

# Create a lookup dictionary for ACM papers
acm_titles = set()
for info in paper_info:
    if info['source'] == 'ACM':
        acm_titles.add(info['title'])

print(f"Found {len(acm_titles)} ACM papers")

# Find ACM citations from 2018
acm_citations = []
for cit in citations_2018:
    cit_title = cit.get('title', '')
    if cit_title in acm_titles:
        acm_citations.append(int(cit.get('citation_count', 0)))

print(f"Found {len(acm_citations)} ACM citations in 2018")
print(f"Citation counts: {acm_citations[:10]}...")  # Show first 10

# Calculate average if we have data
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': avg_citations,
        'total_papers': len(acm_citations),
        'total_citations': sum(acm_citations)
    }
else:
    result = {
        'average_citation_count': None,
        'total_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found in 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
