code = """import json
import re

# Load data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('=== BASIC DATA STATS ===')
print(f'Total papers: {len(mongo_data)}')
print(f'Total citations: {len(citations)}')

# Check for papers with years
print('\n=== YEAR CHECK ===')
years_found = []
for doc in mongo_data:
    text = doc.get('text', '')
    
    # Try venue format
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
        years_found.append(year)
    else:
        # Try full year
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
            years_found.append(year)

if years_found:
    print(f'Years extracted: {sorted(set(years_found))}')
    print(f'Post-2016 papers: {len([y for y in years_found if y > 2016])}')
else:
    print('No years found!')

# Check for empirical keyword
print('\n=== EMPIRICAL KEYWORD CHECK ===')
empirical_count = 0
for doc in mongo_data:
    text = doc.get('text', '')
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        empirical_count += 1

print(f'Papers with "empirical": {empirical_count}')

# Check title matching
print('\n=== TITLE MATCHING CHECK ===')
paper_titles = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if filename:
        paper_titles.append(filename.replace('.txt', ''))

citation_titles = [cit['title'] for cit in citations]

print(f'Paper titles sample: {paper_titles[:5]}')
print(f'Citation titles sample: {citation_titles[:5]}')

exact_matches = set(paper_titles) & set(citation_titles)
print(f'Exact title matches: {len(exact_matches)}')

# Now find empirical papers after 2016
empirical_papers = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check empirical
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if year and year > 2016 and has_empirical:
        empirical_papers.append(title)

print(f'\nPost-2016 empirical papers: {len(empirical_papers)}')

if empirical_papers:
    print('Sample papers:')
    for i, title in enumerate(empirical_papers[:10]):
        print(f'  {i+1}. {title}')

# Find those with citations
citation_map = {cit['title'].lower(): int(cit['total_citations']) for cit in citations}
results = []

for title in empirical_papers:
    if title.lower() in citation_map:
        results.append({
            'title': title,
            'total_citations': citation_map[title.lower()]
        })

print(f'\nWith citations: {len(results)}')

# Sort
def sort_func(x):
    return x['total_citations']
results.sort(key=sort_func, reverse=True)

# Show top results
if results:
    print('\nTop papers:')
    for i, res in enumerate(results[:10]):
        print(f"{i+1}. {res['title']} - {res['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': []}

exec(code, env_args)
