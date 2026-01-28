code = """import json
import re

# Load the citations data for 2020
citations_file = var_functions.query_db:0
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Load the paper documents
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary to store paper titles and their venue
paper_venues = {}

# Extract venue information from each paper document
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for venue information in the text
    # Common patterns: conference abbreviations with years
    venue_patterns = [
        r"CHI\s+'?\d{2}",
        r"CHI\s+\d{4}",
        r"Proceedings of .*CHI",
        r"ACM SIGCHI",
    ]
    
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = "CHI"
            break
    
    if venue:
        paper_venues[title] = venue

# Filter citations for CHI papers and sum the counts
total_citations = 0
chi_papers_count = 0
matched_citations = []

for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in paper_venues:
        total_citations += count
        chi_papers_count += 1
        matched_citations.append({
            'title': title,
            'citation_count': count
        })

# Print results in the required format
result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': chi_papers_count,
    'sample_papers': matched_citations[:5]  # Show first 5 for verification
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
