code = """import json
import re

# Load paper documents from file path
paper_docs_path = locals()['var_functions.query_db:0']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f'Loaded {len(paper_docs)} paper documents')

# Extract paper information
papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract year - try multiple patterns
    year = None
    patterns = [
        r'\b(20\d{2})\b',  # Full year like 2017, 2018
        r"(UBICOMP|CHI|CSCW|DIS|UIST|MobileHCI)\s*\'?(\d{2})",  # Conference format
        r'Copyright\s*\d{4}\s*©\s*(20\d{2})'  # Copyright year
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            match = matches[0]
            if isinstance(match, tuple):
                year_str = match[1] if len(match) > 1 else match[0]
            else:
                year_str = match
            
            if len(year_str) == 2:
                year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
            else:
                year = int(year_str)
            break
    
    # Extract contribution type
    contribution = None
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        contribution = 'empirical'
    elif re.search(r'\bartifact\b', text, re.IGNORECASE):
        contribution = 'artifact'
    elif re.search(r'\btheoretical\b', text, re.IGNORECASE):
        contribution = 'theoretical'
    elif re.search(r'\bsurvey\b', text, re.IGNORECASE):
        contribution = 'survey'
    elif re.search(r'\bmethodological\b', text, re.IGNORECASE):
        contribution = 'methodological'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter papers: empirical contribution AND year > 2016
empirical_papers = [p for p in papers_info 
                   if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]

print(f'Found {len(empirical_papers)} empirical papers after 2016')
for p in empirical_papers:
    print(f"  - {p['title']} ({p['year']})")

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f'\nLoaded {len(citations)} citation records')

# Group citations by title to get total counts
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_totals[title] = citation_totals.get(title, 0) + count

# Match papers with their citation counts and prepare results
results = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_totals.get(title, 0)
    results.append({
        'title': title,
        'total_citation_count': total_citations,
        'year': paper['year']
    })

# Sort by citation count (descending)
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print(f'\nMatched {len(results)} papers with citations')
for r in results:
    print(f"  - {r['title']}: {r['total_citation_count']} citations")

output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:18': {'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2']}}

exec(code, env_args)
