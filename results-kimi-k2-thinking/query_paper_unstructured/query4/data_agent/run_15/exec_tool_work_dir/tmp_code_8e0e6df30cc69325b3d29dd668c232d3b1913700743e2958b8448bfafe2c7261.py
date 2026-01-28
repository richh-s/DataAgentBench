code = """import json, re, os

# Load both datasets
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup table
citation_lookup = {}
for rec in citations:
    citation_lookup[rec['title']] = int(rec['total_citations'])

# Step 1: Extract years from ALL papers systematically
papers_by_year = {}
all_papers_info = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year 
    year = None
    
    # Method 1: Look for copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Method 2: Conference header
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Method 3: Any 4-digit year
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year:
        if year not in papers_by_year:
            papers_by_year[year] = 0
        papers_by_year[year] += 1
        
        all_papers_info.append({
            'title': title,
            'year': year,
            'text': text
        })

print('=== YEARS PRESENT IN DATASET ===')
for year in sorted(papers_by_year.keys()):
    print(f'  {year}: {papers_by_year[year]} papers')

# Step 2: Check physical activity keywords in ALL papers (any year)
print('\n=== PHYSICAL ACTIVITY PAPERS (ALL YEARS) ===')
pa_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'step', 'running', 'walking', 'sports']

pa_papers_all = []
for paper in all_papers_info:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    has_pa = any(term in text_lower or term in title_lower for term in pa_keywords)
    
    if has_pa:
        pa_papers_all.append(paper)

if pa_papers_all:
    print(f'Found {len(pa_papers_all)} PA papers across all years')
    
    # Show distribution
    pa_by_year = {}
    for paper in pa_papers_all:
        year = paper['year']
        pa_by_year[year] = pa_by_year.get(year, 0) + 1
    
    print('\nPA papers by year:')
    for year in sorted(pa_by_year.keys()):
        print(f'  {year}: {pa_by_year[year]} papers')
else:
    print('No papers with physical activity terms found at all!')

# Step 3: Check specifically for 2016
print('\n=== 2016 PAPERS CHECK ===')
papers_2016 = [p for p in all_papers_info if p['year'] == 2016]
print(f'Total 2016 papers: {len(papers_2016)}')

# Debug: check what 2016 papers actually contain
if papers_2016:
    print('\nFirst 10 papers from 2016 (checking for PA terms):')
    for i, paper in enumerate(papers_2016[:10]):
        text_lower = paper['text'].lower()
        found_terms = [term for term in pa_keywords if term in text_lower or term in paper['title'].lower()]
        
        print(f'  {i+1}. {paper["title"]}")
        print(f'      Found PA terms: {found_terms}')

# Step 4: Find actual 2016 PA papers
print('\n=== 2016 PHYSICAL ACTIVITY PAPERS ===')
pa_2016 = []
for paper in papers_2016:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    in_pa_domain = any(term in text_lower or term in title_lower for term in pa_keywords)
    
    if in_pa_domain:
        total_citations = citation_lookup.get(paper['title'], 0)
        pa_2016.append({
            'title': paper['title'],
            'total_citation_count': total_citations
        })

# Sort by citations
pa_2016.sort(key=lambda x: x['total_citation_count'], reverse=True)

# Show results
print(f'Found {len(pa_2016)} papers:')
for result in pa_2016:
    print(f'  Title: {result["title"]}")
    print(f'  Total citations: {result["total_citation_count"]}')
    print()

# If none found, list all 2016 papers to see what exists
if not pa_2016:
    print('No physical activity papers from 2016 found!')
    print('All 2016 papers:')
    for paper in papers_2016:
        citations = citation_lookup.get(paper['title'], 0)
        print(f'  - {paper["title"]} ({citations} citations)')

print()
print('__RESULT__:')
print(json.dumps(pa_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': [], 'var_functions.execute_python:68': []}

exec(code, env_args)
