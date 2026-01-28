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

# Build citation map for exact matching
citation_map = {}
for cit in citations:
    citation_map[cit['title']] = int(cit['total_citations'])

# Comprehensive analysis
print('=== COMPREHENSIVE DATA ANALYSIS ===')
print(f'Total papers: {len(mongo_data)}')
print(f'Total citations: {len(citations)}')

# Check year distribution
year_counts = {}
empirical_by_year = {}
papers_with_data = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year - try multiple patterns
    year = None
    
    # Pattern 1: Conference venue format (CHI '17, UbiComp '15, etc.)
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        # Pattern 2: Full year format (2017, 2018, etc.)
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
        else:
            # Pattern 3: Any 4-digit year pattern
            any_year = re.search(r"\b(19|20)\d{2}\b", text)
            if any_year:
                year = int(any_year.group(0))
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        
        # Check for empirical contribution
        has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
        
        if has_empirical:
            empirical_by_year[year] = empirical_by_year.get(year, 0) + 1
        
        papers_with_data.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical,
            'has_citation': title in citation_map
        })

# Show year distribution
print('\n=== YEAR DISTRIBUTION ===')
for year in sorted(year_counts.keys()):
    total = year_counts[year]
    empirical = empirical_by_year.get(year, 0)
    print(f'  {year}: {total} papers ({empirical} empirical)')

# Show post-2016 summary
post_2016_total = sum(count for year, count in year_counts.items() if year > 2016)
post_2016_empirical = sum(count for year, count in empirical_by_year.items() if year > 2016)

print(f'\n=== SUMMARY ===')
print(f'Post-2016 total papers: {post_2016_total}')
print(f'Post-2016 empirical papers: {post_2016_empirical}')

# Show specific post-2016 empirical papers
post_2016_empirical_papers = [p for p in papers_with_data if p['year'] > 2016 and p['has_empirical']]

print(f'\nPost-2016 empirical papers found: {len(post_2016_empirical_papers)}')

if post_2016_empirical_papers:
    print('\nPost-2016 empirical papers:')
    for i, paper in enumerate(post_2016_empirical_papers[:20]):
        citation_info = f" - {citation_map[paper['title']]} citations" if paper['has_citation'] else " (no citation data)"
        print(f"  {i+1}. {paper['title']} ({paper['year']}){citation_info}")
else:
    print('\nNo post-2016 empirical papers found in the dataset!')
    
    # Show all empirical papers regardless of year
    all_empirical = [p for p in papers_with_data if p['has_empirical']]
    if all_empirical:
        print(f'\nEmpirical papers (any year): {len(all_empirical)}')
        for i, paper in enumerate(all_empirical[:10]):
            print(f"  {i+1}. {paper['title']} ({paper['year']})")

# Find papers that meet all criteria (post-2016, empirical, has citations)
final_papers = [p for p in post_2016_empirical_papers if p['has_citation']]

print(f'\n=== FINAL RESULTS ===')
print(f'Papers meeting all criteria: {len(final_papers)}')

# Build final answer
answer_data = []
for paper in final_papers:
    answer_data.append({
        'title': paper['title'],
        'total_citations': citation_map[paper['title']]
    })

# Sort by citations descending
answer_data.sort(key=lambda x: x['total_citations'], reverse=True)

if answer_data:
    print('\nPapers with title and total citation count:')
    for i, paper in enumerate(answer_data):
        print(f"{i+1}. {paper['title']} - {paper['total_citations']} citations")
else:
    print('\nNo papers found meeting the criteria.')
    print('This could mean:')
    print('1. No papers after 2016 in the dataset')
    print('2. No papers with "empirical" keyword after 2016')
    print('3. Title matching issues between databases')

print('__RESULT__:')
print(json.dumps(answer_data))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': []}

exec(code, env_args)
