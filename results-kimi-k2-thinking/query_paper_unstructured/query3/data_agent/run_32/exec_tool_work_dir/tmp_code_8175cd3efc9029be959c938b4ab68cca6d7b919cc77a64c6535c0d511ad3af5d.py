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

print('=== DEBUG ANALYSIS ===')
print(f'Total papers: {len(mongo_data)}')
print(f'Total citations: {len(citations)}')

# Build citation title list
citation_titles = [cit['title'] for cit in citations]
citation_map = {cit['title']: int(cit['total_citations']) for cit in citations}

print(f'\nSample citation titles:')
for i in range(min(5, len(citation_titles))):
    print(f'  {i+1}. {citation_titles[i]}')

# Check year extraction and empirical status
year_distribution = {}
empirical_papers = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    
    # Try conference format: CHI '17, UbiComp '15, etc.
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Try full year
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year:
        year_distribution[year] = year_distribution.get(year, 0) + 1
    
    # Check empirical keyword
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if has_empirical:
        empirical_papers.append({'title': title, 'year': year})

print(f'\nYear distribution:')
for year in sorted(year_distribution.keys())[-15:]:  # Last 15 years
    print(f'  {year}: {year_distribution.get(year, 0)} papers')

print(f'\nTotal empirical papers (any year): {len(empirical_papers)}')

# Check post-2016 empirical
post_2016_empirical = [p for p in empirical_papers if p['year'] and p['year'] > 2016]
print(f'Post-2016 empirical papers: {len(post_2016_empirical)}')

if post_2016_empirical:
    print(f'\nPost-2016 empirical papers:')
    for i, paper in enumerate(post_2016_empirical[:20]):
        has_cit = paper['title'] in citation_map
        cit_count = citation_map.get(paper['title'], 0)
        cit_info = f' - {cit_count} citations' if has_cit else ' (no citations)'
        print(f'  {i+1}. {paper["title"]} ({paper["year"]}){cit_info}')
else:
    print('No post-2016 empirical papers found!')
    print('\nChecking all empirical papers regardless of year:')
    for i, paper in enumerate(empirical_papers[:20]):
        print(f'  {i+1}. {paper["title"]} ({paper["year"]})')

# Check exact title matches between databases
exact_matches = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        if title in citation_map:
            exact_matches.append(title)

print(f'\nExact title matches (any year): {len(exact_matches)}')

# Show matches that might match criteria
qualified_matches = []
for title in exact_matches[:100]:  # Check first 100 matches for performance
    # Find the corresponding MongoDB doc
    for doc in mongo_data:
        filename = doc.get('filename', '')
        if filename and filename.replace('.txt', '') == title:
            text = doc.get('text', '')
            
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
                qualified_matches.append({
                    'title': title,
                    'year': year,
                    'citations': citation_map[title]
                })
            break

print(f'\nQualified matches: {len(qualified_matches)}')

if qualified_matches:
    qualified_matches.sort(key=lambda x: x['citations'], reverse=True)
    print('\nQualified papers:')
    for i, paper in enumerate(qualified_matches):
        print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['citations']} citations")

# Build final answer
final_answer = []
for paper in qualified_matches:
    final_answer.append({
        'title': paper['title'],
        'total_citations': paper['citations']
    })

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': []}

exec(code, env_args)
