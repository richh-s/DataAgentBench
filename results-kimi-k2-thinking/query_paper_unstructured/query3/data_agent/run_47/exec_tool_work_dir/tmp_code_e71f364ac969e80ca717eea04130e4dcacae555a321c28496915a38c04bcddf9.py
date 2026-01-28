code = """import json
import re

# Load paper documents
papers_path = locals()['var_functions.query_db:26']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
citations_path = locals()['var_functions.query_db:27']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Process papers: extract title, year, and check for empirical
processed_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '').strip() if filename else ''
    
    # Extract year - try multiple patterns
    year = None
    year_patterns = [
        r"\b(201[7-9]|202[0-9])\b",  # 2017-2029
        r"'([1-9][0-9])\b",  # '15 for 2015
        r"\b(20(?:1[7-9]|2[0-9]))\b"  # explicit 20xx
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            # Handle 2-digit years
            if len(year_str) == 2:
                if int(year_str) < 50:
                    year = int('20' + year_str)
                else:
                    year = int('19' + year_str)
            else:
                year = int(year_str)
            break
    
    # Check for empirical (case-insensitive)
    is_empirical = 'empirical' in text.lower()
    
    processed_papers.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

# Process citations: sum by title
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count_str = citation.get('citation_count', '0')
    
    # Remove any non-numeric characters and convert to int
    count = int(re.sub(r'[^0-9]', '', str(count_str)))
    
    if title:
        citation_totals[title] = citation_totals.get(title, 0) + count

# Find papers that match criteria: empirical AND year > 2016 AND has citations
results = []
for paper in processed_papers:
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        if title in citation_totals and citation_totals[title] > 0:
            results.append({
                'title': title,
                'total_citations': citation_totals[title]
            })

# Sort by citation count descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Print results
output = json.dumps(results, ensure_ascii=False, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}, 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.execute_python:30': []}

exec(code, env_args)
