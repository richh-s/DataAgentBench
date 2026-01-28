code = """import json
import re

# Load the citations data for 2020
citations_file = var_functions.query_db:2
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load the paper documents data
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

print('Total 2020 citations records:', len(citations_2020))
print('Total paper documents:', len(paper_docs))

# Extract venue information from paper documents
paper_venues = {}
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Look for venue information in the first part of the text (header area)
    header_text = text[:2000].lower()  # Convert to lowercase for easier matching
    
    # Check if CHI appears in the header
    if 'chi' in header_text:
        # Verify it's not just a random mention but likely a venue
        # Look for common conference patterns
        patterns = [
            'chi',  # Just CHI
            'proceedings',  # Proceedings of CHI
            'conference',   # CHI conference
            'acm chi'       # ACM CHI
        ]
        
        # Count occurrences and context
        chi_count = header_text.count('chi')
        if chi_count > 0:
            # Additional check: look for year patterns like '15, 2015, etc.
            has_year = re.search(r'(\'|\u2019)?\d{2}|\d{4}', header_text)
            if has_year or chi_count > 2:  # If multiple mentions or has year
                paper_venues[title] = 'CHI'

print('Found', len(paper_venues), 'potential CHI papers in documents')

# Create a mapping of titles to citation info for easier lookup
citation_map = {}
for citation in citations_2020:
    citation_map[citation['title']] = int(citation['citation_count'])

# Find CHI papers that have citations in 2020
total_citations = 0
chi_papers_with_citations = []

for title, venue in paper_venues.items():
    if title in citation_map:
        cit_count = citation_map[title]
        total_citations += cit_count
        chi_papers_with_citations.append({
            'title': title,
            'citations_2020': cit_count
        })

print('CHI papers cited in 2020:', len(chi_papers_with_citations))
print('Total citation count for CHI papers in 2020:', total_citations)

# For verification, show first few papers
print('Sample CHI papers:')
for i, paper in enumerate(chi_papers_with_citations[:5]):
    print(f"  {i+1}. {paper['title']} - {paper['citations_2020']} citations")

# Prepare result
result = {
    'total_citation_count': total_citations,
    'chi_papers_count': len(chi_papers_with_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
