code = """import json, re

# Load data
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

print('=== DATASET OVERVIEW ===')
print(f'Total papers in database: {len(papers)}')
print(f'Total citation records: {len(citations)}')

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}
print(f'Unique papers with citation data: {len(citation_lookup)}')

# Check sample citation entries
print('\nSample citation entries:')
for i, rec in enumerate(citations[:5]):
    print(f"  {i+1}. {rec['title'][:60]}...: {rec['total_citations']} citations")

# Analyze ALL papers thoroughly
print('\n=== ANALYZING ALL PAPERS ===')

all_paper_info = []
for i, doc in enumerate(papers):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year using all possible methods
    year = None
    year_methods = []
    
    # Method 1: Copyright line
    m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if m:
        year = int(m.group(1))
        year_methods.append('copyright')
    
    # Method 2: Conference header
    if not year:
        m = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if m:
            yr = int(m.group(1))
            if yr < 50:
                year = 2000 + yr
                year_methods.append('conference')
    
    # Method 3: Published/proceedings
    if not year:
        m = re.search(r'(?:published|proceeding|presentation).*?\b(20\d{2})\b', text[:3000], re.I)
        if m:
            year = int(m.group(1))
            year_methods.append('published')
    
    # Method 4: Year with publisher
    if not year:
        m = re.search(r'\b(20\d{2})\b\s+(?:ACM|IEEE|PubMed|DOI|ISBN)', text[:3000])
        if m:
            year = int(m.group(1))
            year_methods.append('publisher')
    
    # Method 5: Any reasonable year in header
    if not year:
        years = re.findall(r'\b20\d{2}\b', text[:2000])
        for y in years:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                year_methods.append('header')
                break
    
    # Check for various domains
    text_lower = text.lower()
    title_lower = title.lower()
    
    domains = []
    if 'physical activity' in text_lower or 'physical activity' in title_lower:
        domains.append('physical activity')
    if 'fitness' in text_lower or 'fitness' in title_lower:
        domains.append('fitness')
    if 'exercise' in text_lower or 'exercise' in title_lower:
        domains.append('exercise')
    if 'food' in text_lower or 'diet' in text_lower:
        domains.append('food')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower or 'anxiety' in text_lower or 'depression' in text_lower:
        domains.append('mental')
    if 'health' in text_lower:
        domains.append('health')
    if 'self-tracking' in text_lower or 'personal informatics' in text_lower:
        domains.append('self-tracking')
    
    all_paper_info.append({
        'title': title,
        'year': year,
        'domains': domains,
        'year_methods': year_methods
    })
    
    # Print first 10 papers for debugging
    if i < 10:
        print(f"Paper {i+1}: {title[:70]}")
        print(f"  Year: {year} (methods: {year_methods})")
        print(f"  Domains: {domains}")
        print()

# Overall statistics
print('\n=== OVERALL STATISTICS ===')
valid_years = [p['year'] for p in all_paper_info if p['year'] is not None]
print(f'Papers with valid years: {len(valid_years)}')

if valid_years:
    year_counts = {}
    for year in valid_years:
        year_counts[year] = year_counts.get(year, 0) + 1
    
    print('Papers by year:')
    for year in sorted(year_counts.keys()):
        print(f'  {year}: {year_counts[year]}')
    
    # Check 2016 specifically
    papers_2016 = [p for p in all_paper_info if p['year'] == 2016]
    print(f'\nTotal 2016 papers: {len(papers_2016)}')
    
    if papers_2016:
        print('\nAll 2016 papers:')
        for p in papers_2016:
            citations = citation_lookup.get(p['title'], 0)
            print(f"  - {p['title']}")
            print(f"    Domains: {p['domains']}")
            print(f"    Citations: {citations}")
    
    # Check physical activity papers from 2016
    pa_2016 = [p for p in papers_2016 if any(d in ['physical activity', 'fitness', 'exercise'] for d in p['domains'])]
    print(f'\n2016 physical activity papers: {len(pa_2016)}')
    
    # Prepare final results
    final_results = []
    for p in pa_2016:
        citations = citation_lookup.get(p['title'], 0)
        final_results.append({
            'title': p['title'],
            'total_citation_count': citations
        })
    
    # Sort by citation count
    final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)
    
    print('\n=== FINAL RESULTS ===')
    for r in final_results:
        print(f"Title: {r['title']}")
        print(f"Total citation count: {r['total_citation_count']}")
        print()

else:
    print('No papers with valid publication years found in the dataset.')
    final_results = []

# Output final JSON
print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
