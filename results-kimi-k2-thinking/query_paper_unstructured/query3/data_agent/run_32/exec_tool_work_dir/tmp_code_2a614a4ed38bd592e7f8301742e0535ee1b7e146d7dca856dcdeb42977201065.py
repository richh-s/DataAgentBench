code = """import json
import re

# Load full data
mongo_key = 'var_functions.query_db:70'
citation_key = 'var_functions.query_db:71'

mongo_data = locals()[mongo_key]
citations = locals()[citation_key]

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Get all paper titles
paper_titles = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        paper_titles.append(title)

print('Total paper titles extracted:', len(paper_titles))
print('\nFirst 20 paper titles:')
for i, title in enumerate(paper_titles[:20]):
    print(f"{i+1}. {title}")

# Get citation titles
citation_titles = [cit['title'] for cit in citations]
print(f'\nTotal citation titles: {len(citation_titles)}')
print('\nFirst 20 citation titles:')
for i, title in enumerate(citation_titles[:20]):
    print(f"{i+1}. {title}")

# Check for matches (exact)
print('\n=== EXACT TITLE MATCHES ===')
matches = []
for paper in paper_titles:
    if paper in citation_titles:
        matches.append(paper)

print(f'Exact matches: {len(matches)}')
for i, title in enumerate(matches[:10]):
    print(f"{i+1}. {title}")

# Now check which papers have empirical keyword
print('\n=== EMPIRICAL PAPERS ===')
empirical_papers = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        empirical_papers.append(title)

print(f'Papers with "empirical" keyword: {len(empirical_papers)}')
for i, title in enumerate(empirical_papers[:10]):
    print(f"{i+1}. {title}")

# Check year distribution more carefully
print('\n=== YEAR DISTRIBUTION ANALYSIS ===')
year_stats = {}
for doc in mongo_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    year = None
    
    # Check for venue pattern
    venue_matches = re.findall(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_matches:
        year = 2000 + int(venue_matches[0])
    else:
        # Check for full year
        year_matches = re.findall(r"\b(20\d{2})\b", text)
        if year_matches:
            year = int(year_matches[0])
    
    if year:
        year_stats[year] = year_stats.get(year, 0) + 1

# Show all years found
sorted_years = sorted(year_stats.items())
print(f'Years range: {sorted_years[0][0]} to {sorted_years[-1][0]}')
print('\nAll years found:')
for year, count in sorted_years:
    print(f'  {year}: {count} papers')

# Check papers after 2016 specifically
print('\n=== POST-2016 ANALYSIS ===')
papers_after_2016 = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    year = None
    venue_matches = re.findall(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_matches:
        year = 2000 + int(venue_matches[0])
    else:
        year_matches = re.findall(r"\b(20\d{2})\b", text)
        if year_matches:
            year = int(year_matches[0])
    
    if year and year > 2016:
        has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
        papers_after_2016.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

print(f'Total papers after 2016: {len(papers_after_2016)}')

# Show post-2016 papers and whether they have empirical keyword
post_2016_empirical = []
for paper in papers_after_2016:
    if paper['has_empirical']:
        post_2016_empirical.append(paper)
        
print(f'Post-2016 papers with "empirical": {len(post_2016_empirical)}')
for i, paper in enumerate(post_2016_empirical[:10]):
    print(f"{i+1}. {paper['title']} ({paper['year']})")

# Build final results
final_results = []
citation_map = {cit['title'].lower(): int(cit['total_citations']) for cit in citations}

for paper in post_2016_empirical:
    title_lower = paper['title'].lower()
    if title_lower in citation_map:
        final_results.append({
            'title': paper['title'],
            'total_citations': citation_map[title_lower]
        })

print(f'\nFinal matching papers: {len(final_results)}')

# Sort and show top
if final_results:
    final_results.sort(key=lambda x: x['total_citations'], reverse=True)
    print('\nTop matching papers:')
    for i, paper in enumerate(final_results[:10]):
        print(f"{i+1}. {paper['title']} - {paper['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': []}

exec(code, env_args)
