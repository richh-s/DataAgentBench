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

print(f"Total 2020 citations records: {len(citations_2020)}")
print(f"Total paper documents: {len(paper_docs)}")

# Extract venue information from paper documents
# The hint says venue can be extracted from the full text
# Looking at the sample, venues appear near the beginning, often in headers

paper_venues = {}
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Look for venue information in the text
    # Common patterns: CHI 'YY, CHI YY, CHI Conference, etc.
    # Search in the first part of the text (header area)
    header_text = text[:2000]  # Look in first 2000 characters
    
    venue = None
    # Pattern matching for CHI
    chi_patterns = [
        r'CHI\s*[\'\u2019]?\d{2}',  # CHI '15, CHI 15, CHI'15
        r'CHI\s+\d{4}',  # CHI 2015
        r'Proceedings of the .*CHI',  # Proceedings of the CHI
        r'ACM CHI',  # ACM CHI
    ]
    
    for pattern in chi_patterns:
        if re.search(pattern, header_text, re.IGNORECASE):
            venue = "CHI"
            break
    
    if venue:
        paper_venues[title] = venue

print(f"Found {len(paper_venues)} CHI papers in documents")

# Now join with citations data
total_citations = 0
chi_citations_count = 0

for citation in citations_2020:
    cit_title = citation['title']
    cit_count = int(citation['citation_count'])
    
    if cit_title in paper_venues:
        total_citations += cit_count
        chi_citations_count += 1

print(f"Found {chi_citations_count} CHI papers cited in 2020")
print(f"Total citation count for CHI papers in 2020: {total_citations}")

# Prepare result
result = {
    "total_citation_count": total_citations,
    "chi_papers_count": chi_citations_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
