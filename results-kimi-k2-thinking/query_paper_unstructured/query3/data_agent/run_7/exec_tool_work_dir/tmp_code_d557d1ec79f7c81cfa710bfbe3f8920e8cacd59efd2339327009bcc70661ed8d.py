code = """import json
import re

# Load the paper documents
paper_docs_file = var_functions.query_db:0
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Load the citation data
citations_result = var_functions.query_db:1

# Process paper data to extract title, year, and contribution
papers_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = re.sub(r'\.txt$', '', filename)
    
    # Extract year from text - look for 4-digit years (1900-2099)
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Check if contribution type includes 'empirical'
    contribution_empirical = 'empirical' in text.lower()
    
    papers_info.append({
        'title': title,
        'year': year,
        'is_empirical': contribution_empirical,
        'text_snippet': text[:500]  # First 500 chars for debugging
    })

# Filter papers: empirical contribution and year > 2016
empirical_papers_after_2016 = [
    paper for paper in papers_info 
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016
]

# Group citations by title and sum them up
citation_totals = {}
for citation in citations_result:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title in citation_totals:
        citation_totals[title] += count
    else:
        citation_totals[title] = count

# Join empirical papers with citation totals
result = []
for paper in empirical_papers_after_2016:
    title = paper['title']
    total_citations = citation_totals.get(title, 0)
    
    # Only include papers with citations
    if total_citations > 0:
        result.append({
            'title': title,
            'total_citation_count': total_citations,
            'year': paper['year']
        })

# Sort by citation count (descending)
result_sorted = sorted(result, key=lambda x: x['total_citation_count'], reverse=True)

# Print result
print('__RESULT__:')
print(json.dumps(result_sorted, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
