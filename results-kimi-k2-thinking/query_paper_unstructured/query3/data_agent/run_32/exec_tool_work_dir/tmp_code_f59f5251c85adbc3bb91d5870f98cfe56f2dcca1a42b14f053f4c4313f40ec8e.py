code = """import json
import re

# Load all data
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)
        
if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Build citation map quickly
citation_titles = set()
citation_counts = {}
for cit in citations:
    citation_titles.add(cit['title'])
    citation_counts[cit['title']] = int(cit['total_citations'])

# Let's analyze the data more systematically
print('=== MONGODB DATA ANALYSIS ===')
print(f'Total documents: {len(mongo_data)}')

# Check first document
if mongo_data:
    print(f'\nFirst document structure:')
    for key in mongo_data[0].keys():
        print(f'  - {key}')
    
    print(f"\nFirst filename: {mongo_data[0].get('filename', 'NONE')}")
    first_text = mongo_data[0].get('text', '')[:200]
    print(f"First text preview: {first_text}")

# Now let's check ALL papers for years
all_years = []
for doc in mongo_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Try all year patterns
    matches = re.findall(r"[A-Z][a-zA-Z]*\s+'(\d{2})'\b", text)
    if matches:
        for m in matches:
            all_years.append(2000 + int(m))
    
    # Also check full years
    year_matches = re.findall(r"\b(20\d{2})\b", text)
    if year_matches:
        for y in year_matches:
            all_years.append(int(y))

if all_years:
    year_counts = {}
    for y in all_years:
        year_counts[y] = year_counts.get(y, 0) + 1
    
    print(f'\nYear distribution:')
    for year in sorted(year_counts.keys())[-20:]:  # Last 20 years
        print(f'  {year}: {year_counts[year]} papers')

# Check empirical papers
empirical_titles = []
for doc in mongo_data:
    text = doc.get('text', '')
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        filename = doc.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            empirical_titles.append(title)

print(f'\nPapers with empirical keyword: {len(empirical_titles)}')

# Check overlaps with citations
overlap = set(empirical_titles) & citation_titles
print(f'Empirical papers with citations: {len(overlap)}')

# Now let's find the specific matches for the query
final_matches = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Must have citation
    if title not in citation_counts:
        continue
    
    text = doc.get('text', '')
    
    # Check empirical
    if 'empirical' not in text.lower() and 'empirically' not in text.lower():
        continue
    
    # Extract year
    year = None
    
    # Try venue format
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Try full year
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check year filter
    if not year or year <= 2016:
        continue
    
    # Add to results
    final_matches.append({
        'title': title,
        'total_citations': citation_counts[title]
    })

# Sort by citations
final_matches.sort(key=lambda x: x['total_citations'], reverse=True)

print(f'\n=== FINAL RESULTS: {len(final_matches)} papers ===')
for i, paper in enumerate(final_matches[:20]):
    print(f"{i+1}. {paper['title']} - {paper['total_citations']} citations")

print('\n__RESULT__:')
print(json.dumps(final_matches))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': [], 'var_functions.execute_python:130': [], 'var_functions.execute_python:134': [], 'var_functions.execute_python:138': [], 'var_functions.execute_python:140': [], 'var_functions.execute_python:146': []}

exec(code, env_args)
