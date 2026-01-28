code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

print('=== DEBUG: Data loaded ===')
print('Citations count:', len(citations))
print('Papers count:', len(papers))

# Let's examine first few papers in detail
print('\n=== DEBUG: First 3 papers ===')
for i in range(min(3, len(papers))):
    paper = papers[i]
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    print(f"\nPaper {i+1}:")
    print(f"  Filename: {filename}")
    print(f"  Title: {title}")
    print(f"  Text length: {len(text)}")
    
    # Find all years in this paper
    years = re.findall(r'\b(20[0-9]{2})\b', text[:2000])
    if years:
        print(f"  Years found: {years}")
    
    # Check if contains empirical
    has_empirical = 'empirical' in text.lower()
    print(f"  Has 'empirical': {has_empirical}")

# Now check ALL papers for empirical and years
print('\n=== DEBUG: Finding empirical papers ===')
empirical_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if not title or not text:
        continue
    
    has_empirical = 'empirical' in text.lower()
    
    if has_empirical:
        # Find years in this paper
        years = re.findall(r'\b(20[0-9]{2})\b', text)
        year = int(years[0]) if years else 0
        
        empirical_papers.append({'title': title, 'year': year, 'years_found': years})

print(f'Found {len(empirical_papers)} papers with "empirical"')

# Check years distribution for empirical papers
year_dist = {}
for p in empirical_papers:
    year = p['year']
    if year > 0:
        year_dist[year] = year_dist.get(year, 0) + 1

print('\nYear distribution for empirical papers:')
for yr in sorted(year_dist.keys()):
    print(f'  {yr}: {year_dist[yr]} papers')

# Find papers after 2016
empirical_after_2016 = [p for p in empirical_papers if p['year'] > 2016]
print(f'\nEmpirical papers after 2016: {len(empirical_after_2016)}')

if len(empirical_after_2016) > 0:
    print('\nSample empirical papers after 2016:')
    for i, p in enumerate(empirical_after_2016[:10]):
        print(f'  {i+1}. {p["title"][:80]} ({p["year"]})')
else:
    # Check the max year
    all_years = []
    for p in empirical_papers:
        if p['year'] > 0:
            all_years.append(p['year'])
    if all_years:
        print(f'\nMax year found in empirical papers: {max(all_years)}')

# Check citation titles
print('\n=== DEBUG: Checking citation titles ===')
citation_titles = [c['title'] for c in citations]
print(f'First 5 citation titles:')
for i, title in enumerate(citation_titles[:5]):
    print(f'  {i+1}. {title[:80]}')

# Check for exact matches
exact_matches = []
emp_titles = [p['title'] for p in empirical_after_2016]
for title in emp_titles:
    if title in citation_titles:
        exact_matches.append(title)

print(f'\nExact title matches: {len(exact_matches)}')

# Try normalized matching
print('\n=== DEBUG: Normalized matching ===')
norm_matches = []
norm_citation_map = {}

for c in citations:
    norm = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    norm_citation_map[norm] = int(c['total_citations'])

for paper in empirical_after_2016:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', paper['title'].lower())
    if norm_title in norm_citation_map:
        norm_matches.append({
            'title': paper['title'],
            'year': paper['year'],
            'citations': norm_citation_map[norm_title]
        })

print(f'Normalized matches: {len(norm_matches)}')

# Final results
results = norm_matches
results.sort(key=lambda x: x['citations'], reverse=True)

print('\n__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:66': []}

exec(code, env_args)
