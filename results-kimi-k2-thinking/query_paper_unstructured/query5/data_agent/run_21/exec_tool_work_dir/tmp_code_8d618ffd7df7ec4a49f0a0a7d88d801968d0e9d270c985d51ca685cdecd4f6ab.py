code = """import json
import re

# Read the citations data file path
citations_file = locals()['var_functions.query_db:2']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper docs data file path
paper_docs_file = locals()['var_functions.query_db:5']
with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

# Process paper docs to extract venue information
chi_papers = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Look for venue information in the text - check for CHI specifically
    venue = None
    
    # Check multiple patterns for CHI
    chi_patterns = [
        r'CHI\s*\'\d{2}', r'CHI\s+\d{4}', r'Proceedings of the SIGCHI',
        r'Proceedings of the ACM.*Human.*Computer.*Interaction',
        r'ACM.*CHI'
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = 'CHI'
            break
    
    # Check first 1000 characters for CHI mentions
    if not venue and 'CHI' in text[:1000]:
        venue = 'CHI'
    
    if venue == 'CHI':
        chi_papers.append({
            'title': title,
            'filename': filename
        })

# Create a set of CHI paper titles for fast lookup
chi_titles = set(paper['title'] for paper in chi_papers)

# Sum citation counts for CHI papers cited in 2020
total_citations = 0
matched_papers = []

for citation in citations_data:
    citation_title = citation.get('title', '')
    try:
        citation_count = int(citation.get('citation_count', 0))
    except (ValueError, TypeError):
        citation_count = 0
    
    if citation_title in chi_titles:
        total_citations += citation_count
        matched_papers.append({
            'title': citation_title,
            'citations_2020': citation_count
        })

result = {
    'total_citation_count': total_citations,
    'matched_chi_papers_count': len(matched_papers),
    'chi_papers_in_corpus': len(chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
