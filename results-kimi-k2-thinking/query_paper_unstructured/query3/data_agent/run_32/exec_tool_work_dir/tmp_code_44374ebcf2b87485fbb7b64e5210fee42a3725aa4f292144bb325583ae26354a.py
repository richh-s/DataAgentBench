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

print('=== DATA SUMMARY ===')
print('Total papers:', len(mongo_data))
print('Total citations:', len(citations))

# Check year distribution and empirical keyword
year_counts = {}
empirical_counts = {}
papers_with_years = []

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
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        
        has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
        if has_empirical:
            empirical_counts[year] = empirical_counts.get(year, 0) + 1
            papers_with_years.append((title, year, text))

print('\nYear distribution:')
for year in sorted(year_counts.keys()):
    print('  ' + str(year) + ': ' + str(year_counts[year]) + ' papers (' + str(empirical_counts.get(year, 0)) + ' empirical)')

# Filter for post-2016 empirical papers
post_2016_empirical = [(t, y) for t, y, _ in papers_with_years if y > 2016]
print('\nPost-2016 empirical papers found: ' + str(len(post_2016_empirical)))

if post_2016_empirical:
    print('\nSample papers:')
    for i, (title, year) in enumerate(post_2016_empirical[:10]):
        print('  ' + str(i+1) + '. ' + title + ' (' + str(year) + ')')

# Build citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Find matches
results = []
for title, year in post_2016_empirical:
    title_lower = title.lower()
    if title_lower in citation_map:
        results.append({'title': title, 'total_citations': citation_map[title_lower]})

print('\nPapers with citation data: ' + str(len(results)))

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': []}

exec(code, env_args)
