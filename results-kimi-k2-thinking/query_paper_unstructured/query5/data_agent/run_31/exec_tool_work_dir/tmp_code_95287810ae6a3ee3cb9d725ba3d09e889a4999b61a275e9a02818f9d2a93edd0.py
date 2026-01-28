code = """import json
import re

# Read the citations data from 2020
citations_file = var_functions.query_db:0
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Read the paper documents
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Create a mapping of paper titles to their venue
chi_paper_titles = set()
total_papers_checked = 0

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # If no text content, skip
    if not text:
        continue
        
    total_papers_checked += 1
    
    # Check if this is a CHI paper by looking for CHI venue patterns
    # Common patterns: CHI '15, CHI 2015, CHI15, Proceedings of CHI, etc.
    chi_patterns = [
        r'CHI\s*\'\s*\d{2}',  # CHI '15
        r'CHI\s*\d{4}',       # CHI 2015
        r'CHI\s*\d{2}\b',     # CHI 15 (word boundary)
        r'Proceedings of .{0,20}CHI',  # Proceedings of CHI
        r'CHI\s+Conference',   # CHI Conference
        r'ACM\s+CHI',          # ACM CHI
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        # Extract title from filename (remove .txt extension)
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_paper_titles.add(title)

print("Processing complete")

# Now filter citations for CHI papers only and sum up
total_citations = 0
chi_citations_count = 0
citations_in_data = len(citations_2020)

for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    # Check if this title is a CHI paper
    if title in chi_paper_titles:
        total_citations += count
        chi_citations_count += 1

result = {
    'total_chi_citations_in_2020': total_citations,
    'chi_papers_with_citations': chi_citations_count,
    'total_papers_in_corpus': citations_in_data,
    'chi_papers_identified': len(chi_paper_titles),
    'papers_checked_for_venue': total_papers_checked
}

print('-'*30)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
