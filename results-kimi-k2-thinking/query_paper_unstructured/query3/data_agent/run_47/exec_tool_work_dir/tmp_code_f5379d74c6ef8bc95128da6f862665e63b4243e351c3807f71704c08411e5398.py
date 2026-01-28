code = """import json
import re

# Access the stored results
papers_raw = locals()['var_functions.query_db:2']
citations_raw = locals()['var_functions.query_db:3']

# Extract paper information
papers = []
for paper in papers_raw:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Find year - look for 4-digit numbers between 2010-2029
    year_match = re.search(r'\b(201[0-9]|202[0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for contribution type
    text_lower = text.lower()
    has_empirical = 'empirical' in text_lower
    
    papers.append({
        'title': title,
        'year': year,
        'is_empirical': has_empirical
    })

# Sum up citations by title
citation_counts = {}
for citation in citations_raw:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_counts[title] = citation_counts.get(title, 0) + count

# Filter papers with empirical contribution published after 2016
filtered_papers = []
for paper in papers:
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        if title in citation_counts:
            filtered_papers.append({
                'title': title,
                'total_citations': citation_counts[title]
            })

# Sort by citation count descending
filtered_papers.sort(key=lambda x: x['total_citations'], reverse=True)

result = json.dumps(filtered_papers, ensure_ascii=False)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}}

exec(code, env_args)
