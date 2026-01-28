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

# Analyze the data comprehensively
print('=== DATASET OVERVIEW ===')
print(f'Total papers: {len(mongo_data)}')
print(f'Total citation records: {len(citations)}')

# Extract all years
year_counts = {}
papers_with_years = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    
    # Try multiple patterns for year extraction
    patterns = [
        (r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", lambda x: 2000 + int(x)),  # CHI '17 -> 2017
        (r"\b(20\d{2})\b", lambda x: int(x)),  # 2017 -> 2017
        (r"\b(19\d{2})\b", lambda x: int(x)),  # 1999 -> 1999 (just in case)
    ]
    
    for pattern, converter in patterns:
        match = re.search(pattern, text)
        if match:
            year = converter(match.group(1))
            break
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        papers_with_years.append((title, year, text))

print('\n=== YEAR DISTRIBUTION ===')
sorted_years = sorted(year_counts.items())
print(f'Year range: {sorted_years[0][0]} - {sorted_years[-1][0]}')

# Show all years
for year, count in sorted_years:
    print(f'  {year}: {count} papers')

# Look for post-2016 papers
post_2016_papers = [(t, y, txt) for t, y, txt in papers_with_years if y > 2016]
print(f'\nPost-2016 papers found: {len(post_2016_papers)}')

# Debug empirical detection
print('\n=== EMPIRICAL CONTRIBUTION ANALYSIS ===')

# Papers with direct empirical keyword
empirical_keyword_papers = []
empirical_method_papers = []

for title, year, text in papers_with_years:
    text_lower = text.lower()
    
    # Check 1: Direct mention of "empirical"
    if 'empirical' in text_lower or 'empirically' in text_lower:
        empirical_keyword_papers.append((title, year))
    
    # Check 2: Research methodology indicators
    method_indicators = [
        'we conducted', 'we performed', 'we studied', 'we surveyed',
        'experiment', 'user study', 'field study', 'case study',
        'participants', 'subjects', 'data collection', 'interviewed',
        'survey of', 'interviews with'
    ]
    
    indicator_count = sum(1 for ind in method_indicators if ind in text_lower)
    if indicator_count >= 2:  # Multiple indicators suggest empirical work
        empirical_method_papers.append((title, year, indicator_count))

print(f'Papers with "empirical" keyword: {len(empirical_keyword_papers)}')
print(f'Papers with empirical methodology indicators: {len(empirical_method_papers)}')

# Post-2016 empirical papers
post_2016_empirical = [(t, y) for t, y in empirical_keyword_papers if y > 2016]
print(f'Post-2016 papers with empirical keyword: {len(post_2016_empirical)}')

post_2016_method = [(t, y, c) for t, y, c in empirical_method_papers if y > 2016]
print(f'Post-2016 papers with empirical methods: {len(post_2016_method)}')

# Show sample papers
if post_2016_empirical:
    print('\nSample post-2016 empirical papers:')
    for i, (title, year) in enumerate(post_2016_empirical[:10]):
        print(f'  {i+1}. {title} ({year})')

if post_2016_method:
    print('\nSample post-2016 method papers:')
    for i, (title, year, count) in enumerate(post_2016_method[:10]):
        print(f'  {i+1}. {title} ({year}) - {count} indicators')

# Check title matching
print('\n=== TITLE MATCHING ANALYSIS ===')
citation_titles_lower = {cit['title'].lower(): (cit['title'], int(cit['total_citations'])) for cit in citations}

# Try to find matches for empirical papers
empirical_matches = []
method_matches = []

# Match empirical keyword papers
for title, year in post_2016_empirical:
    title_lower = title.lower()
    if title_lower in citation_titles_lower:
        original_title, citations = citation_titles_lower[title_lower]
        empirical_matches.append({
            'title': original_title,
            'year': year,
            'total_citations': citations
        })

# Match method papers
for title, year, _ in post_2016_method:
    title_lower = title.lower()
    if title_lower in citation_titles_lower:
        original_title, citations = citation_titles_lower[title_lower]
        method_matches.append({
            'title': original_title,
            'year': year,
            'total_citations': citations
        })

print(f'Empirical keyword papers with citations: {len(empirical_matches)}')
print(f'Method indicator papers with citations: {len(method_matches)}')

# Combine and deduplicate
all_papers_map = {}
for paper in empirical_matches + method_matches:
    all_papers_map[paper['title']] = paper

final_results = list(all_papers_map.values())

# Sort by citations
def get_citations(p):
    return p['total_citations']
final_results.sort(key=get_citations, reverse=True)

print(f'\nTotal unique papers: {len(final_results)}')

if final_results:
    print('\nTop papers:')
    for i, paper in enumerate(final_results[:10]):
        print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['total_citations']} citations")
else:
    print('No matching papers found')

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': []}

exec(code, env_args)
