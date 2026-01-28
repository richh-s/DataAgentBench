code = """import json
import re

# Access the data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# Load from files if needed
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Comprehensive analysis to find the issue
print('=== COMPREHENSIVE DEBUG ANALYSIS ===')
print(f'Total papers in MongoDB: {len(mongo_data)}')
print(f'Total citation records: {len(citations)}')

# Check year distribution
print('\n=== YEAR DISTRIBUTION (showing all years) ===')
year_counts = {}
papers_with_years = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year using all possible patterns
    year = None
    
    # Pattern 1: Venue notation like CHI '17, UbiComp '15
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        # Pattern 2: Full year like 2017, 2018, etc.
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
        else:
            # Pattern 3: Try to find any 4-digit number that looks like a year
            any_year = re.search(r"\b(19|20)\d{2}\b", text)
            if any_year:
                year = int(any_year.group(0))
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        papers_with_years.append((title, year, text))

# Show all years
for year in sorted(year_counts.keys()):
    print(f'  {year}: {year_counts[year]} papers')

# Show post-2016 summary
post_2016_count = sum(count for year, count in year_counts.items() if year > 2016)
print(f'\nPost-2016 papers: {post_2016_count}')

# Check empirical keyword distribution
print('\n=== EMPIRICAL KEYWORD ANALYSIS ===')
empirical_by_year = {}
all_empirical_papers = []

for title, year, text in papers_with_years:
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        empirical_by_year[year] = empirical_by_year.get(year, 0) + 1
        all_empirical_papers.append((title, year))

print('Empirical papers by year:')
for year in sorted(empirical_by_year.keys()):
    print(f'  {year}: {empirical_by_year[year]} empirical papers')

# Show post-2016 empirical papers
post_2016_empirical = [(t, y) for t, y in all_empirical_papers if y > 2016]
print(f'\nPost-2016 empirical papers found: {len(post_2016_empirical)}')

if post_2016_empirical:
    print('\nPost-2016 empirical papers:')
    for i, (title, year) in enumerate(post_2016_empirical[:20]):
        print(f"  {i+1}. {title} ({year})")
else:
    print('No post-2016 empirical papers found!')
    # Show some empirical papers regardless of year
    print('\nAll empirical papers (any year):')
    for i, (title, year) in enumerate(all_empirical_papers[:10]):
        print(f"  {i+1}. {title} ({year})")

# Check citation matching
print('\n=== CITATION MATCHING ANALYSIS ===')
citation_titles = [cit['title'] for cit in citations]
citation_titles_lower = {t.lower(): t for t in citation_titles}

# Try to match empirical papers
matching_empirical = []
for title, year in post_2016_empirical:
    title_lower = title.lower()
    if title_lower in citation_titles_lower:
        original_title = citation_titles_lower[title_lower]
        # Find citation count
        for cit in citations:
            if cit['title'] == original_title:
                matching_empirical.append({
                    'title': title,
                    'year': year,
                    'total_citations': int(cit['total_citations'])
                })
                break

print(f'Empirical papers with citation matches: {len(matching_empirical)}')

if matching_empirical:
    # Sort by citations
    matching_empirical.sort(key=lambda x: x['total_citations'], reverse=True)
    
    print('\nMatching papers:')
    for i, paper in enumerate(matching_empirical[:20]):
        print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['total_citations']} citations")
else:
    print('No matches found!')
    
    # Show citation titles for comparison
    print('\nSample citation titles:')
    for i, title in enumerate(citation_titles[:20]):
        print(f"  {i+1}. {title}")

# Final answer
final_answer = matching_empirical

print('\n=== FINAL ANSWER PREPARATION ===')
print(f'Total papers to return: {len(final_answer)}')

# Format for final output
output_list = []
for paper in final_answer:
    output_list.append({
        'title': paper['title'],
        'total_citations': paper['total_citations']
    })

print('__RESULT__:')
print(json.dumps(output_list))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': []}

exec(code, env_args)
