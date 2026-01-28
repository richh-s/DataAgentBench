code = """import json
import re

# Read the data
citations_file = var_functions.query_db:0
papers_file = var_functions.query_db:5

with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Function to extract source (publisher) from paper text
def extract_source(text):
    text_upper = text.upper()
    
    # Simple checks
    if 'ACM' in text_upper:
        return 'ACM'
    elif 'IEEE' in text_upper:
        return 'IEEE'
    elif 'PUBMED' in text_upper:
        return 'PubMed'
    
    return None

# Process paper documents
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract source
    source = extract_source(text)
    
    if title and source:
        paper_info.append({'title': title, 'source': source})

# Filter ACM papers
acm_papers = {}
for paper in paper_info:
    if paper['source'] == 'ACM':
        acm_papers[paper['title']] = paper

print('Found', len(acm_papers), 'ACM papers')

# Find ACM papers cited in 2018
acm_citations_2018 = []
for citation in citations_2018:
    cit_title = citation.get('title', '')
    if cit_title in acm_papers:
        acm_citations_2018.append({
            'title': cit_title,
            'citation_count': int(citation.get('citation_count', 0))
        })

print('Found', len(acm_citations_2018), 'ACM papers cited in 2018')

# Calculate average
if acm_citations_2018:
    total_citations = sum(p['citation_count'] for p in acm_citations_2018)
    avg_citations = total_citations / len(acm_citations_2018)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_papers': len(acm_citations_2018),
        'total_citations': total_citations
    }
else:
    result = {
        'average_citation_count': 0,
        'total_papers': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
