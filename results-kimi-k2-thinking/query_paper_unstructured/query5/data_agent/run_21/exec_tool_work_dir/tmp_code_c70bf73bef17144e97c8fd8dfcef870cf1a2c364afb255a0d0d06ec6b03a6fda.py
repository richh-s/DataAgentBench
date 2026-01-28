code = """import json
import re

# Read the citations data
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read the paper docs data
paper_docs_file = var_functions.query_db:5
with open(paper_docs_file, 'r') as f:
    paper_docs_data = json.load(f)

# Process paper docs to extract venue information
chi_papers = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Look for venue information in the text
    # Common HCI venues: CHI, Ubicomp, CSCW, DIS, PervasiveHealth, WWW, IUI, OzCHI, TEI, AH
    venue_patterns = [
        r'CHI\s*\'\d{2}', r'CHI\s+\d{4}', r'Proceedings of the SIGCHI',
        r'Proceedings of the ACM on Human-Computer Interaction',
        r'CSCW', r'Ubicomp', r'DIS', r'PervasiveHealth', r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH'
    ]
    
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            if 'CHI' in pattern or 'SIGCHI' in pattern:
                venue = 'CHI'
                break
            elif 'CSCW' in pattern:
                venue = 'CSCW'
                break
            elif 'Ubicomp' in pattern:
                venue = 'Ubicomp'
                break
            elif 'DIS' in pattern:
                venue = 'DIS'
                break
            # Add more venue detection as needed
    
    # If no specific venue found, check for general conference patterns
    if not venue:
        # Check for common conference header patterns
        if 'CHI' in text[:500]:  # Check first 500 characters
            venue = 'CHI'
        elif re.search(r'Proceedings of .*CHI', text):
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
    citation_count = int(citation.get('citation_count', 0))
    
    if citation_title in chi_titles:
        total_citations += citation_count
        matched_papers.append({
            'title': citation_title,
            'citations_2020': citation_count
        })

result = {
    'total_citation_count': total_citations,
    'matched_chi_papers_count': len(matched_papers),
    'chi_papers_in_db': len(chi_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
