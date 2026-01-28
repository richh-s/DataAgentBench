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

# Simple debug: check a few papers manually
print('=== MANUAL PAPER CHECK ===')
for i in range(min(5, len(mongo_data))):
    filename = mongo_data[i].get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = mongo_data[i].get('text', '')[:500]  # First 500 chars
    
    print(f'\nPaper {i+1}: {title}')
    print(f'Text preview: {text[:200]}...')
    
    # Extract year
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    print(f'Year: {year}')
    print(f'Has empirical: {"empirical" in text.lower()}')

# Check citations
print('\n=== MANUAL CITATION CHECK ===')
for i in range(min(5, len(citations))):
    cit = citations[i]
    print(f'{i+1}. {cit["title"]} - {cit["total_citations"]} citations')

# Check for empirical keyword across ALL papers
print('\n=== EMPIRICAL KEYWORD CHECK ACROSS ALL PAPERS ===')
empirical_papers = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        # Extract year for these papers
        year = None
        venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
        if venue_match:
            year = 2000 + int(venue_match.group(1))
        else:
            year_match = re.search(r"\b(20\d{2})\b", text)
            if year_match:
                year = int(year_match.group(1))
        
        empirical_papers.append({'title': title, 'year': year})

print(f'Papers with "empirical" keyword: {len(empirical_papers)}')

# Filter for post-2016
post_2016_empirical = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
print(f'Post-2016 empirical papers: {len(post_2016_empirical)}')

# Show them
if post_2016_empirical:
    print('\nPost-2016 empirical papers:')
    for i, paper in enumerate(post_2016_empirical[:20]):
        print(f"{i+1}. {paper['title']} ({paper['year']})")

# Check if they have citations
citation_titles = [c['title'].lower() for c in citations]
matching = []
for paper in post_2016_empirical:
    if paper['title'].lower() in citation_titles:
        matching.append(paper['title'])

print(f'\nPost-2016 empirical papers with citation records: {len(matching)}')

# Build final results
citation_map = {c['title'].lower(): int(c['total_citations']) for c in citations}

final_results = []
for paper in post_2016_empirical:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        final_results.append({
            'title': paper['title'],
            'total_citations': citation_map[title_lower]
        })

# Sort
def sort_func(item):
    return item['total_citations']
final_results.sort(key=sort_func, reverse=True)

print(f'\nFinal results count: {len(final_results)}')
print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': []}

exec(code, env_args)
