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
    
    year_match = re.search(r'(?:\'|\b)(201[0-9]|202[0-9])(?:\'|\b)', text)
    year = int(year_match.group(1)) if year_match else None
    
    text_lower = text.lower()
    contribution = None
    if 'empirical' in text_lower:
        contribution = 'empirical'
    elif 'artifact' in text_lower:
        contribution = 'artifact'
    elif 'theoretical' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower:
        contribution = 'survey'
    elif 'methodological' in text_lower:
        contribution = 'methodological'
    
    papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

citation_counts = {}
for citation in citations_raw:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_counts[title] = citation_counts.get(title, 0) + count

filtered_papers = []
for paper in papers:
    if paper['contribution'] == 'empirical' and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        if title in citation_counts:
            filtered_papers.append({
                'title': title,
                'total_citations': citation_counts[title]
            })

filtered_papers.sort(key=lambda x: x['total_citations'], reverse=True)

result = json.dumps(filtered_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}}

exec(code, env_args)
