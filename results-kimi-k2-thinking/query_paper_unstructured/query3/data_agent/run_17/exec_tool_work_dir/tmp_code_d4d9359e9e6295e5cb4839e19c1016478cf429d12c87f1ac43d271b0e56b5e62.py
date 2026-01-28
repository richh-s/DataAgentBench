code = """import json
import re

# Read MongoDB papers data
with open('file_storage/functions.query_db:2.json', 'r') as f:
    papers_data = json.load(f)

# Read citations data
with open('file_storage/functions.query_db:8.json', 'r') as f:
    citations_data = json.load(f)

# Extract paper information from MongoDB documents
papers = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for 4-digit years 2017-2025 (after 2016)
    year_match = re.search(r'(20(?:1[7-9]|2[0-5]))', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution type - look for empirical (case-insensitive)
    contribution = None
    text_lower = text.lower()
    
    # Check if it's an empirical paper
    if 'empirical' in text_lower:
        contribution = 'empirical'
    
    if title:  # Only add if we have a title
        papers.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })

# Filter papers with empirical contribution published after 2016
empirical_papers = [
    p for p in papers 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

# Create a dictionary for empirical papers for easy lookup
empirical_papers_dict = {p['title']: p for p in empirical_papers}

# Calculate total citations for each empirical paper
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    if title in empirical_papers_dict:
        citation_count = int(citation.get('citation_count', 0))
        if title not in citation_totals:
            citation_totals[title] = 0
        citation_totals[title] += citation_count

# Prepare results
results = []
for title, paper_info in empirical_papers_dict.items():
    total_citations = citation_totals.get(title, 0)
    results.append({
        'title': title,
        'year': paper_info['year'],
        'total_citation_count': total_citations
    })

# Sort by year then title
results.sort(key=lambda x: (x['year'], x['title']))

print('__RESULT__:')
print(json.dumps({
    'empirical_papers_after_2016': results,
    'count': len(results)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'available_variables': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:8'], 'query_db_2': 'file_storage/functions.query_db:2.json', 'query_db_8': 'file_storage/functions.query_db:8.json'}}

exec(code, env_args)
