code = """import json
import re

# Load the full results
with open('var_functions.query_db:2', 'r') as f:
    papers = json.load(f)

with open('var_functions.query_db:5', 'r') as f:
    citations_2020 = json.load(f)

# Extract title from filename
for paper in papers:
    filename = paper['filename']
    # Remove .txt extension to get title
    title = filename.replace('.txt', '')
    paper['title'] = title
    
    # Extract venue from text - look for CHI mentions
    text = paper.get('text', '')
    
    # Look for venue patterns
    venue_patterns = [
        r'CHI\s*\'\d{2}',  # CHI '15, CHI '20, etc.
        r'CHI\s+\d{4}',   # CHI 2015, CHI 2020, etc.
        r'Proceedings of the .*?CHI',  # Proceedings of CHI
        r'ACM Conference on Human Factors',  # Full name
    ]
    
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = "CHI"
            break
    
    paper['venue'] = venue

# Filter CHI papers
chi_papers = [p for p in papers if p['venue'] == 'CHI']

# Create a dictionary of CHI papers by title for easy lookup
chi_papers_dict = {p['title'].lower().strip(): p for p in chi_papers}

# Match citations with CHI papers
chi_citations_2020 = []
for citation in citations_2020:
    citation_title = citation['title'].lower().strip()
    if citation_title in chi_papers_dict:
        chi_citations_2020.append({
            'title': citation['title'],
            'citation_count': int(citation['citation_count']),
            'citation_year': int(citation['citation_year'])
        })

# Calculate total citation count
total_citations = sum(c['citation_count'] for c in chi_citations_2020)

# Also get count of unique papers
unique_papers_count = len(chi_citations_2020)

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': unique_papers_count,
    'chi_papers_with_citations': chi_citations_2020
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
