code = """import json
import re

# Load the data
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Let's start with a basic data exploration
print('=== DATASET OVERVIEW ===')
print(f'MongoDB papers: {len(mongo_data)}')
print(f'Citation records: {len(citations)}')

# Sample the data to understand structure
print('\n=== MONGODB SAMPLE (first 3 papers) ===')
for i in range(min(3, len(mongo_data))):
    filename = mongo_data[i].get('filename', 'NO FILE')
    text_preview = mongo_data[i].get('text', '')[:100]
    print(f"{i+1}. File: {filename}")
    print(f"   Text preview: {text_preview}...")

print('\n=== CITATION SAMPLE (first 3 records) ===')
for i in range(min(3, len(citations))):
    title = citations[i].get('title', 'NO TITLE')
    count = citations[i].get('total_citations', '0')
    print(f"{i+1}. Title: {title}")
    print(f"   Citations: {count}")

# Now let's comprehensively examine all papers for years and empirical status
print('\n=== PAPER ANALYSIS ===')
papers_with_years = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    
    # Pattern 1: Venue format (CHI '17, Ubicomp '15, etc.)
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        # Pattern 2: Full year (2017, 2018, etc.)
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check for empirical keyword
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Check if has citation data
    has_citation = title in [c['title'] for c in citations]
    
    if year:  # Only track papers where we found a year
        papers_with_years.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical,
            'has_citation': has_citation
        })

# Sort by year and analyze
papers_by_year = {}
for p in papers_with_years:
    year = p['year']
    papers_by_year[year] = papers_by_year.get(year, 0) + 1

print('\n=== YEAR DISTRIBUTION ===')
for year in sorted(papers_by_year.keys()):
    count = papers_by_year[year]
    print(f"  {year}: {count} papers")

# Show papers after 2016
post_2016 = [p for p in papers_with_years if p['year'] > 2016]
print(f'\n=== POST-2016 PAPERS: {len(post_2016)} ===')

# Of these, show empirical ones
post_2016_empirical = [p for p in post_2016 if p['has_empirical']]
print(f'Post-2016 EMPIRICAL papers: {len(post_2016_empirical)}')

if post_2016_empirical:
    print('\nPost-2016 empirical papers:')
    for i, p in enumerate(post_2016_empirical[:20]):
        citation_flag = " (has citation)" if p['has_citation'] else ""
        print(f"  {i+1}. {p['title']} ({p['year']}){citation_flag}")
else:
    print('\nNo post-2016 empirical papers found!')
    print('\nChecking all empirical papers regardless of year:')
    all_empirical = [p for p in papers_with_years if p['has_empirical']]
    print(f'Total empirical papers (any year): {len(all_empirical)}')
    
    if all_empirical:
        print('\nSample empirical papers:')
        for i, p in enumerate(all_empirical[:10]):
            print(f"  {i+1}. {p['title']} ({p['year']})")

# Now build results for papers with citations
final_results = []
citation_map = {c['title']: int(c['total_citations']) for c in citations}

for paper in post_2016_empirical:
    if paper['has_citation']:
        final_results.append({
            'title': paper['title'],
            'total_citations': citation_map[paper['title']]
        })

# Sort by citations
def cit_sort(x):
    return x['total_citations']
final_results.sort(key=cit_sort, reverse=True)

print(f'\n=== FINAL MATCHING PAPERS: {len(final_results)} ===')
if final_results:
    print('\nTop papers by citations:')
    for i, p in enumerate(final_results):
        print(f"{i+1}. {p['title']} - {p['total_citations']} citations")
else:
    print('\nNo papers match all criteria (post-2016, empirical, has citations)')
    
    # Debug: Check criteria individually
    debug = {
        'post_2016_total': len(post_2016),
        'post_2016_empirical': len(post_2016_empirical),
        'total_with_citations': len([p for p in post_2016 if p['has_citation']])
    }
    print('\nDebug counts:')
    for k, v in debug.items():
        print(f"  {k}: {v}")

print('\n__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': []}

exec(code, env_args)
