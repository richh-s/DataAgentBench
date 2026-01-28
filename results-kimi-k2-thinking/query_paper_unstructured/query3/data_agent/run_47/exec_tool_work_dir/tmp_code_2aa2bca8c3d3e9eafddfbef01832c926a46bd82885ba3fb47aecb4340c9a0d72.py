code = """papers_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:3']

import json

# Read the paper documents
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Read the citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Extract paper information
paper_data = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    import re
    year_match = re.search(r'\b(201[0-9]|202[0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if it's empirical
    is_empirical = 'empirical' in text.lower()
    
    paper_data.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

# Sum citations by title
citation_counts = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_counts[title] = citation_counts.get(title, 0) + count

# Filter papers: empirical, published after 2016, and have citations
filtered_papers = []
for paper in paper_data:
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        if title in citation_counts and citation_counts[title] > 0:
            filtered_papers.append({
                'title': title,
                'total_citations': citation_counts[title]
            })

# Sort by citation count
filtered_papers.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(filtered_papers, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}}

exec(code, env_args)
