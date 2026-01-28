code = """import json
import re

# Load data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# If they're file paths, read them
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    mongo_data = json.load(open(mongo_data))
if isinstance(citations, str) and citations.endswith('.json'):
    citations = json.load(open(citations))

print('Total papers:', len(mongo_data))
print('Total citations:', len(citations))

# Debug: check year distribution
year_counts = {}
empirical_count = 0
post_2016_empirical = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
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
        year_counts[year] = year_counts.get(year, 0) + 1
    
    # Check empirical (broad check)
    text_lower = text.lower()
    has_empirical = False
    
    # Direct mention
    if 'empirical' in text_lower or 'empirically' in text_lower:
        has_empirical = True
        empirical_count += 1
    else:
        # Check for research indicators
        indicators = ['we conducted', 'we performed', 'experiment', 'user study', 'field study', 'participants', 'interview', 'survey', 'case study']
        if sum(1 for ind in indicators if ind in text_lower) >= 2:
            has_empirical = True
            empirical_count += 1
    
    if has_empirical and year and year > 2016:
        post_2016_empirical.append(title)

# Show year distribution
print('\nYear distribution (recent):')
for year in sorted(year_counts.keys(), reverse=True)[:15]:
    print(f'  {year}: {year_counts[year]} papers')

print(f'\nEmpirical papers detected: {empirical_count}')
print(f'Post-2016 empirical papers: {len(post_2016_empirical)}')

# Show sample post-2016 empirical papers
print('\nSample post-2016 empirical papers:')
for i, title in enumerate(post_2016_empirical[:10]):
    print(f'  {i+1}. {title}')

# Check citation titles
print(f'\nSample citation titles:')
citation_titles = [c['title'] for c in citations]
for i, title in enumerate(citation_titles[:10]):
    print(f'  {i+1}. {title}')

# Try exact matching
matches = []
for paper_title in post_2016_empirical:
    if paper_title in citation_titles:
        matches.append(paper_title)

print(f'\nExact title matches: {len(matches)}')
if matches:
    print('Matching papers:')
    for title in matches:
        print(f'  - {title}')
else:
    # Try case-insensitive matching
    citation_titles_lower = {t.lower(): t for t in citation_titles}
    for paper_title in post_2016_empirical:
        if paper_title.lower() in citation_titles_lower:
            print(f'  Case-insensitive match: {paper_title}')

# Build final results using case-insensitive matching
results = []
citation_map = {c['title'].lower(): (c['title'], int(c['total_citations'])) for c in citations}

for paper_title in post_2016_empirical:
    paper_key = paper_title.lower()
    if paper_key in citation_map:
        original_title, citations_count = citation_map[paper_key]
        results.append({
            'title': original_title,
            'total_citations': citations_count
        })

# Sort by citations
def get_citations(p):
    return p['total_citations']
results.sort(key=get_citations, reverse=True)

print(f'\nFinal results count: {len(results)}')
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': []}

exec(code, env_args)
