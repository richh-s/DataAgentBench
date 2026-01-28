code = """import json
import re

# Access the stored results using locals()
paper_docs_file = locals()['var_functions.query_db:2']
citations_file = locals()['var_functions.query_db:3']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read citations
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper information
papers = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    if not title or not text:
        continue
    
    # Find year
    year = None
    # Look for venue patterns
    venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    for pattern in venue_patterns:
        match = re.search(pattern + r'.{0,30}(20\d{2})', text, re.IGNORECASE)
        if match:
            year = int(match.group(1))
            break
    
    if not year:
        # Find first occurrence of 20xx
        year_match = re.search(r'(20\d{2})', text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check if empirical
    is_empirical = 'empirical' in text.lower()
    
    papers[title] = {
        'year': year,
        'is_empirical': is_empirical
    }

# Sum citations per paper
citation_sums = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    citation_sums[title] = citation_sums.get(title, 0) + count

# Find empirical papers after 2016
results = []
for title, info in papers.items():
    if info['year'] and info['year'] > 2016 and info['is_empirical']:
        if title in citation_sums:
            results.append({
                'title': title,
                'total_citation_count': citation_sums[title]
            })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
