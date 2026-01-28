code = """import json
import re

# Load data from storage references
mongo_key = 'var_functions.query_db:70'
citation_key = 'var_functions.query_db:71'

# Get the actual data from storage
mongo_data = locals()[mongo_key]
citations = locals()[citation_key]

# Load from file paths if needed
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Check year distribution first
print('=== YEAR DISTRIBUTION IN MONGODB ===')
year_count = {}

for doc in mongo_data:
    text = doc.get('text', '')
    if not text:
        continue
    
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
        year_count[year] = year_count.get(year, 0) + 1

print('Years found:')
for year in sorted(year_count.keys()):
    print('  ' + str(year) + ': ' + str(year_count[year]) + ' papers')

# Check for empirical keyword across all papers
print('\n=== EMPIRICAL KEYWORD CHECK ===')
empirical_papers = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    if 'empirical' in text.lower() or 'empirically' in text.lower():
        empirical_papers.append(title)

print('Papers with empirical keyword: ' + str(len(empirical_papers)))

# Check citation titles
print('\n=== CITATION TITLES SAMPLE ===')
citation_titles = [cit['title'] for cit in citations]
print('First 20 citation titles:')
for i, title in enumerate(citation_titles[:20]):
    print('  ' + str(i+1) + '. ' + title)

# Check MongoDB titles
print('\n=== MONGODB TITLES SAMPLE ===')
mongo_titles = []
for doc in mongo_data[:20]:
    filename = doc.get('filename', '')
    if filename:
        mongo_titles.append(filename.replace('.txt', ''))

print('First 20 MongoDB titles:')
for i, title in enumerate(mongo_titles):
    print('  ' + str(i+1) + '. ' + title)

# Let's check for exact title matches
print('\n=== TITLE MATCHING CHECK ===')
examined = 0
matches_found = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    examined += 1
    
    if title in citation_titles:
        matches_found.append(title)
    
    if examined >= 100:  # Check first 100
        break

print('Examined ' + str(examined) + ' papers')
print('Found ' + str(len(matches_found)) + ' exact title matches')

# Now let's properly find post-2016 empirical papers
print('\n=== FINDING POST-2016 EMPIRICAL PAPERS ===')
qualified_papers = []

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
    
    # Check empirical
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    # Apply filters
    if year and year > 2016 and has_empirical:
        qualified_papers.append({'title': title, 'year': year})

print('Post-2016 empirical papers: ' + str(len(qualified_papers)))

# Check which of these have citations
citation_map = {}
for cit in citations:
    citation_map[cit['title']] = int(cit['total_citations'])

final_results = []
for paper in qualified_papers:
    if paper['title'] in citation_map:
        final_results.append({
            'title': paper['title'],
            'total_citations': citation_map[paper['title']]
        })

print('Papers with citation data: ' + str(len(final_results)))

# Sort by citations
def sort_by_citations(item):
    return item['total_citations']
final_results.sort(key=sort_by_citations, reverse=True)

print('\n__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': [], 'var_functions.execute_python:120': [], 'var_functions.execute_python:124': []}

exec(code, env_args)
