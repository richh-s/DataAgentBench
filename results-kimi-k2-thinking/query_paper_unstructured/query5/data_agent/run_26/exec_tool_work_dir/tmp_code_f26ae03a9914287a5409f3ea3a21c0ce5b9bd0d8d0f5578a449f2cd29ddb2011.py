code = """import json
import pandas as pd
import re

# Load the citation data for 2020
citation_file = var_functions.query_db:2
citations_2020 = []
with open(citation_file, 'r') as f:
    for line in f:
        citations_2020.append(json.loads(line.strip()))

# Load the paper documents
paper_file = var_functions.query_db:6
paper_docs = []
with open(paper_file, 'r') as f:
    for line in f:
        paper_docs.append(json.loads(line.strip()))

print(f"Loaded {len(citations_2020)} citation records for 2020")
print(f"Loaded {len(paper_docs)} paper documents")

# Create a mapping from paper titles to their venue information
paper_venues = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract venue information from text
    # Look for conference/journal names
    venue = None
    
    # Common patterns for CHI papers
    chi_patterns = [
        r'CHI\s*\'?\d{2}',  # CHI '15, CHI 2015, etc.
        r'Proceedings of the .*?CHI', 
        r'ACM Conference on Human Factors in Computing Systems'
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = 'CHI'
            break
    
    if venue:
        paper_venues[title] = venue

print(f"Found {len(paper_venues)} CHI papers")

# Filter citations for CHI papers and sum the counts
total_citations = 0
chi_paper_citations = []

for citation in citations_2020:
    title = citation.get('title', '')
    if title in paper_venues:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        chi_paper_citations.append({
            'title': title,
            'citation_count': count
        })

print(f"Found {len(chi_paper_citations)} CHI papers cited in 2020")
print(f"Total citations: {total_citations}")

result = {
    'total_citation_count': total_citations,
    'chi_papers_count': len(chi_paper_citations)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
