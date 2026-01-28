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

# Try a very simple extraction
print('=== SIMPLE SEARCH ===')
print(f'Papers: {len(mongo_data)}')
print(f'Citations: {len(citations)}')

# Count exact title matches first
citation_titles = set(c['title'] for c in citations)

exact_matches = 0
for doc in mongo_data:
    filename = doc.get('filename', '')
    if filename and filename.replace('.txt', '') in citation_titles:
        exact_matches += 1

print(f'Exact title matches: {exact_matches}')

# Build citation map
citation_map = {c['title']: int(c['total_citations']) for c in citations}

# Check each paper simply
found_any = False
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Skip if no citation
    if title not in citation_map:
        continue
    
    # Extract year simply
    year = None
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        year = int(match.group(1))
    
    # Check empirical simply
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if year and year > 2016 and has_empirical:
        found_any = True
        print(f'Found: {title} ({year}) - {citation_map[title]} citations')

if not found_any:
    print('No papers found meeting all criteria')

# Simple test: find ANY paper with empirical
print('\n=== EMPIRICAL PAPERS (any year) ===')
empirical_any = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        year_match = re.search(r"\b(20\d{2})\b", text)
        year = int(year_match.group(1)) if year_match else None
        empirical_any.append({'title': title, 'year': year})

print(f'Empirical papers total: {len(empirical_any)}')
for i, p in enumerate(empirical_any[:10]):
    print(f"{i+1}. {p['title']} ({p['year']})")

# Simple test: find ANY paper after 2016
print('\n=== POST-2016 PAPERS (any) ===')
post_2016_any = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    year_match = re.search(r"\b(20\d{2})\b", text)
    if year_match:
        year = int(year_match.group(1))
        if year > 2016:
            post_2016_any.append({'title': title, 'year': year})

print(f'Post-2016 papers total: {len(post_2016_any)}')
for i, p in enumerate(post_2016_any[:10]):
    print(f"{i+1}. {p['title']} ({p['year']})")

# Now do strict criteria but simpler
final_results = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Must have citation
    if title not in citation_map:
        continue
    
    # Extract year
    year_match = re.search(r"\b(20\d{2})\b", text)
    if not year_match:
        continue
    year = int(year_match.group(1))
    
    # Check empirical
    if 'empirical' not in text.lower() and 'empirically' not in text.lower():
        continue
    
    # Check year filter
    if year <= 2016:
        continue
    
    final_results.append({
        'title': title,
        'total_citations': citation_map[title]
    })

# Sort and return
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print(f'\n=== FINAL RESULTS: {len(final_results)} papers ===')
for i, p in enumerate(final_results):
    print(f"{i+1}. {p['title']} - {p['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': []}

exec(code, env_args)
