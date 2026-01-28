code = """import json
import re

# Load data from storage
mongo_path = locals()['var_functions.query_db:70']
citation_path = locals()['var_functions.query_db:71']

with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

with open(citation_path, 'r') as f:
    citations = json.load(f)

# Build citation map
citation_map = {cit['title']: int(cit['total_citations']) for cit in citations}

# Check ALL papers for years and empirical status
all_papers = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year - try multiple patterns
    year = None
    # Pattern 1: Venue format (CHI '17, UbiComp '15, etc.)
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern 2: Full year (2017, 2018, etc.)
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical keyword
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Check if has citation data
    has_citation = title in citation_map
    
    all_papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'has_citation': has_citation,
        'citations': citation_map.get(title, 0)
    })

# Show paper distribution
print(f'Total papers processed: {len(all_papers)}')

# Year distribution
year_counts = {}
for p in all_papers:
    year = p['year']
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1

print('\nYear distribution:')
for year in sorted(year_counts.keys()):
    print(f'  {year}: {year_counts[year]} papers')

# Empirical papers by year
empirical_by_year = {}
for p in all_papers:
    if p['has_empirical'] and p['year']:
        year = p['year']
        empirical_by_year[year] = empirical_by_year.get(year, 0) + 1

print('\nEmpirical papers by year:')
for year in sorted(empirical_by_year.keys()):
    print(f'  {year}: {empirical_by_year[year]} papers')

# Check if there are ANY post-2016 papers
post_2016_papers = [p for p in all_papers if p['year'] and p['year'] > 2016]
print(f'\nTotal post-2016 papers: {len(post_2016_papers)}')

post_2016_empirical = [p for p in post_2016_papers if p['has_empirical']]
print(f'Post-2016 empirical papers: {len(post_2016_empirical)}')

# Check which have citations
post_2016_empirical_with_citations = [p for p in post_2016_empirical if p['has_citation']]
print(f'Post-2016 empirical with citations: {len(post_2016_empirical_with_citations)}')

# Show sample papers that DON'T match to understand why
if len(post_2016_empirical_with_citations) == 0 and post_2016_empirical:
    print('\nSample post-2016 empirical papers (no citation match):')
    for i, p in enumerate(post_2016_empirical[:10]):
        print(f"  {i+1}. {p['title']} ({p['year']})")
    
    print('\nSample citation titles to compare:')
    for i, title in enumerate(list(citation_map.keys())[:10]):
        print(f"  {i+1}. {title}")

# Filter for the final answer
final_answer = []
for p in post_2016_empirical_with_citations:
    final_answer.append({
        'title': p['title'],
        'total_citations': p['citations']
    })

# Sort by citations
final_answer.sort(key=lambda x: x['total_citations'], reverse=True)

print('\n=== FINAL RESULTS ===')
print(f'Count: {len(final_answer)}')

if final_answer:
    print('\nTop papers:')
    for i, p in enumerate(final_answer):
        print(f"{i+1}. {p['title']} - {p['total_citations']} citations")

print('\n__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': []}

exec(code, env_args)
