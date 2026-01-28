code = """import json
import re

# Load paper documents from file
papers_path = locals()['var_functions.query_db:26']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations from file  
citations_path = locals()['var_functions.query_db:27']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Extract paper metadata
paper_metadata = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '').strip() if filename else ''
    
    # Extract year - look for 4-digit years between 2010-2030
    year_match = re.search(r"\b(20(?:1[0-9]|2[0-9]))\b", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if paper mentions empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Also extract venue if available  
    venue_match = re.search(r"\b(CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b", text)
    venue = venue_match.group(1) if venue_match else None
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'venue': venue,
        'is_empirical': has_empirical
    })

# Sum up total citations per paper title
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    if title:
        citation_totals[title] = citation_totals.get(title, 0) + count

# Filter for empirical papers published after 2016
filtered_results = []
for paper in paper_metadata:
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        if title in citation_totals:
            filtered_results.append({
                'title': title,
                'total_citations': citation_totals[title]
            })

# Sort by citation count descending
filtered_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(filtered_results, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}, 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json'}

exec(code, env_args)
