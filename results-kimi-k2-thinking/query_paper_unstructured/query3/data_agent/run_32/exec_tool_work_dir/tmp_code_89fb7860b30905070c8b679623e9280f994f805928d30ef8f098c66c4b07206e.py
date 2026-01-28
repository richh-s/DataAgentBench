code = """import json
import re

# Load data
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Check year extraction and empirical keyword
year_dist = {}
empirical_by_year = {}

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
        year_dist[year] = year_dist.get(year, 0) + 1
        
        # Check empirical
        has_empirical = 'empirical' in text.lower()
        if has_empirical:
            empirical_by_year[year] = empirical_by_year.get(year, 0) + 1

# Show year distribution
print('Year distribution:')
for year in sorted(year_dist.keys()):
    empirical_count = empirical_by_year.get(year, 0)
    print(f'  {year}: {year_dist[year]} papers ({empirical_count} empirical)')

# Check post-2016
post_2016_total = sum(count for year, count in year_dist.items() if year > 2016)
post_2016_empirical = sum(count for year, count in empirical_by_year.items() if year > 2016)

print(f'\nPost-2016 total: {post_2016_total}')
print(f'Post-2016 empirical: {post_2016_empirical}')

# Build list of post-2016 empirical papers
empirical_papers_list = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    if year and year > 2016 and 'empirical' in text.lower():
        empirical_papers_list.append(title)

print(f'\nEmpirical papers after 2016: {len(empirical_papers_list)}')
for i, title in enumerate(empirical_papers_list[:20]):
    print(f'  {i+1}. {title}')

# Build citation map
citation_map = {}
for cit in citations:
    citation_map[cit['title'].lower()] = int(cit['total_citations'])

# Find matches
matches = []
for title in empirical_papers_list:
    if title.lower() in citation_map:
        matches.append({
            'title': title,
            'total_citations': citation_map[title.lower()]
        })

print(f'\nMatches with citations: {len(matches)}')

# Sort by citations
def get_citations(item):
    return item['total_citations']
matches.sort(key=get_citations, reverse=True)

# Show top matches
if matches:
    print('\nTop matches:')
    for i, match in enumerate(matches[:20]):
        print(f"{i+1}. {match['title']} - {match['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': []}

exec(code, env_args)
