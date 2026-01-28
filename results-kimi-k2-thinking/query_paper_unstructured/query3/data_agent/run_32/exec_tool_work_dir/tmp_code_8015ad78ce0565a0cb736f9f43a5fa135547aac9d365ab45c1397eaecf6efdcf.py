code = """import json
import re

# Load full data
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)
if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

print('=== DATA OVERVIEW ===')
print(f'Total papers: {len(mongo_data)}')
print(f'Total citation records: {len(citations)}')

# Analyze year distribution
year_counts = {}
papers_with_years = []

print('\n=== YEAR EXTRACTION ANALYSIS ===')
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else 'Untitled'
    
    # Try to extract year
    year = None
    
    # Pattern 1: Venue format (CHI '17, UbiComp '15)
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        # Pattern 2: Full year (2017, 2018)
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        papers_with_years.append((title, year, text))

# Show year distribution
sorted_years = sorted(year_counts.items())
print(f'Year range: {sorted_years[0][0]} - {sorted_years[-1][0]}')
print(f'Years found: {len(year_counts)}')
print('\nYear distribution:')
for year, count in sorted_years:
    print(f'  {year}: {count} papers')

# Check post-2016 count
post_2016 = sum(count for year, count in year_counts.items() if year > 2016)
print(f'\nPost-2016 papers: {post_2016}')

# Analyze empirical mentions
print('\n=== EMPIRICAL KEYWORD ANALYSIS ===')
empirical_count = 0
empirical_papers = []

for title, year, text in papers_with_years:
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        empirical_count += 1
        empirical_papers.append((title, year, text))

print(f'Papers with "empirical" keyword: {empirical_count}')

post_2016_empirical = [(t, y) for t, y, _ in empirical_papers if y > 2016]
print(f'Post-2016 empirical papers: {len(post_2016_empirical)}')

if post_2016_empirical:
    print('\nPost-2016 empirical papers:')
    for title, year in post_2016_empirical[:10]:
        print(f'  - {title} ({year})')

# Check title matching
print('\n=== TITLE MATCHING ANALYSIS ===')
citation_titles = [cit['title'] for cit in citations]
citation_titles_lower = {t.lower(): t for t in citation_titles}

matches = []
for title, year in post_2016_empirical:
    if title.lower() in citation_titles_lower:
        original_title = citation_titles_lower[title.lower()]
        matches.append((original_title, year))
    elif title in citation_titles:
        matches.append((title, year))

print(f'Matching titles: {len(matches)}')

if matches:
    print('\nMatched papers:')
    for title, year in matches[:10]:
        print(f'  - {title} ({year})')
else:
    # Try partial matching
    print('\nNo exact matches. Checking partial matches...')
    for title, year in post_2016_empirical[:10]:
        title_lower = title.lower()
        for cit_title in citation_titles[:10]:
            cit_lower = cit_title.lower()
            if len(title_lower) > 10 and len(cit_lower) > 10:
                if title_lower[:15] in cit_lower or cit_lower[:15] in title_lower:
                    print(f'  Close: "{title}" vs "{cit_title}"')
                    break

# Build final results
citation_map = {cit['title'].lower(): int(cit['total_citations']) for cit in citations}

final_results = []
for title, year in post_2016_empirical:
    title_lower = title.lower()
    if title_lower in citation_map:
        final_results.append({
            'title': title,
            'year': year,
            'total_citations': citation_map[title_lower]
        })

print(f'\n=== FINAL RESULTS ===')
print(f'Count: {len(final_results)}')

if final_results:
    # Sort by citations
    final_results.sort(key=lambda x: x['total_citations'], reverse=True)
    
    print('\nTop 10 papers:')
    for i, paper in enumerate(final_results[:10]):
        print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['total_citations']} citations")

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': []}

exec(code, env_args)
