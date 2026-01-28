code = """import json
import re

# Load citations data from 2020
with open(var_functions.query_db:0, 'r') as f:
    citations_data = json.load(f)

# Load paper docs data
with open(var_functions.query_db:2, 'r') as f:
    papers_data = json.load(f)

# Create a dictionary of citation counts by title
citation_counts = {}
for citation in citations_data:
    citation_counts[citation['title']] = int(citation['citation_count'])

# Process papers to find CHI papers
chi_papers = []
for paper in papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Check if CHI venue is mentioned in the paper text
    chi_patterns = [
        r'CHI\s*\'?\s*\d{2}',  # CHI '15, CHI 15
        r'CHI\s*\d{4}',        # CHI 2015
        r'CHI\s*\'\d{2}',      # CHI '15
        r'Proceedings of the .*CHI',  # Proceedings of the ... CHI
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi:
        chi_papers.append(title)

# Match CHI papers with citations and sum counts
total_citations = 0
matched_papers = []

for paper_title in chi_papers:
    if paper_title in citation_counts:
        count = citation_counts[paper_title]
        total_citations += count
        matched_papers.append({
            'title': paper_title,
            'citation_count': count
        })

# Sort matched papers by citation count (descending)
matched_papers.sort(key=lambda x: x['citation_count'], reverse=True)

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(matched_papers),
    'chi_papers_with_citations': matched_papers
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
