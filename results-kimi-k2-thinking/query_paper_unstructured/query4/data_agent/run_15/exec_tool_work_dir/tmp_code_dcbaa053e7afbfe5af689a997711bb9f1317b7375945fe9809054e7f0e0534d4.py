code = """import json, re

# Load data files
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file, 'r') as f:
    citations = json.load(f)
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Build citation lookup dictionary
citation_lookup = {}
for rec in citations:
    citation_lookup[rec['title']] = int(rec['total_citations'])

# Find all 2016 papers regardless of domain first
all_papers_with_years = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year using multiple methods
    year = None
    
    # Method 1: Copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Method 2: Conference header with year
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Method 3: Published/proceedings with year
    if not year:
        pub_match = re.search(r'(?:published|proceeding|presentation).*?\b(20\d{2})\b', text[:3000], re.IGNORECASE)
        if pub_match:
            year = int(pub_match.group(1))
    
    # Method 4: Fallback - first reasonable year in header
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year:
        all_papers_with_years.append({
            'title': title,
            'year': year,
            'text': text
        })

from collections import Counter
year_counts = Counter([p['year'] for p in all_papers_with_years])

print('=== OVERALL DATASET STATISTICS ===')
print('Total papers with valid years: ' + str(len(all_papers_with_years)))
print('Year range: ' + str(min(year_counts.keys())) + ' - ' + str(max(year_counts.keys())))
print()
print('Papers by year:')
for year in sorted(year_counts.keys()):
    print('  ' + str(year) + ': ' + str(year_counts[year]) + ' papers')

# Filter 2016 papers
papers_2016 = [p for p in all_papers_with_years if p['year'] == 2016]
print()
print('=== 2016 PAPERS ===')
print('Total 2016 papers: ' + str(len(papers_2016)))

# Define physical activity keywords
pa_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'step count', 'running', 'walking', 'sports', 'active']

# Find 2016 papers in physical activity domain
results = []

for paper in papers_2016:
    title_lower = paper['title'].lower()
    text_lower = paper['text'].lower()
    
    # Check if paper is in physical activity domain
    in_pa_domain = any(keyword in title_lower or keyword in text_lower for keyword in pa_keywords)
    
    if in_pa_domain:
        total_citations = citation_lookup.get(paper['title'], 0)
        results.append({
            'title': paper['title'],
            'total_citation_count': total_citations
        })

# Sort by citation count (descending)
def get_citations(item):
    return item['total_citation_count']

results.sort(key=get_citations, reverse=True)

print()
print('=== 2016 PHYSICAL ACTIVITY PAPERS ===')
print('Found ' + str(len(results)) + ' papers:')
for result in results:
    print('Title: ' + result['title'])
    print('Total citation count: ' + str(result['total_citation_count']))
    print()

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': []}

exec(code, env_args)
