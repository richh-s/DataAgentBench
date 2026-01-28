code = """import json
import re

# Load data from storage
mongo_key = 'var_functions.query_db:70'
citation_key = 'var_functions.query_db:71'

# Get actual data from storage variables
mongo_data = locals()[mongo_key]
citations = locals()[citation_key]

# If they're file paths (strings with .json), read them
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Build citation map for fast lookup
citation_map = {cit['title']: int(cit['total_citations']) for cit in citations}

# Process all papers
papers_with_metadata = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check empirical
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Check citation
    has_citation = title in citation_map
    citation_count = citation_map.get(title, 0)
    
    papers_with_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'has_citation': has_citation,
        'citation_count': citation_count
    })

# Analyze the data
print('=== DATA ANALYSIS ===')
print(f'Total papers processed: {len(papers_with_metadata)}')

# Year distribution
year_counts = {}
for paper in papers_with_metadata:
    year = paper['year']
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1

print('\nYear distribution:')
years_sorted = sorted(year_counts.items())
for year, count in years_sorted:
    print(f'  {year}: {count} papers')

# Summary stats
total_post_2016 = len([p for p in papers_with_metadata if p['year'] and p['year'] > 2016])
total_empirical = len([p for p in papers_with_metadata if p['has_empirical']])
total_with_citations = len([p for p in papers_with_metadata if p['has_citation']])

print(f'\nTotal post-2016 papers: {total_post_2016}')
print(f'Total empirical papers (any year): {total_empirical}')
print(f'Total papers with citations: {total_with_citations}')

# Final filtering
final_papers = []
for paper in papers_with_metadata:
    if paper['year'] and paper['year'] > 2016 and paper['has_empirical'] and paper['has_citation']:
        final_papers.append({
            'title': paper['title'],
            'total_citations': paper['citation_count']
        })

# Sort by citations
final_papers.sort(key=lambda x: x['total_citations'], reverse=True)

print(f'\nFINAL RESULTS: {len(final_papers)} papers')

if final_papers:
    print('\nTop papers:')
    for i, paper in enumerate(final_papers):
        print(f"{i+1}. {paper['title']} - {paper['total_citations']} citations")
else:
    print('No papers match all criteria!')

print('\n__RESULT__:')
print(json.dumps(final_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': []}

exec(code, env_args)
