code = """import json
import re

# Load data
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file, 'r') as f:
    citations = json.load(f)
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# Extract all papers with valid years
all_papers = []
valid_years = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year
    year = None
    
    # Method 1: Copyright line
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
    
    # Method 3: First reasonable year
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year:
        all_papers.append({
            'title': title,
            'year': year,
            'text': text
        })
        valid_years.append(year)

# Overall statistics
from collections import Counter
year_dist = Counter(valid_years)
print('=== DATASET OVERVIEW ===')
print(f'Total papers with valid years: {len(all_papers)}')
print(f'Year range: {min(valid_years)} - {max(valid_years)}')

print('\n=== ALL YEARS PRESENT ===')
for year in sorted(year_dist.keys()):
    print(f'{year}: {year_dist[year]} papers')

# Check 2016 specifically
print('\n=== 2016 PAPERS ===')
papers_2016 = [p for p in all_papers if p['year'] == 2016]
print(f'Total 2016 papers: {len(papers_2016)}')

# Analyze domains in 2016 papers
physical_activity_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'active living', 'step', 'running', 'walking', 'sports']

print('\n=== CHECKING 2016 PAPERS FOR PHYSICAL ACTIVITY DOMAIN ===')
results = []

for paper in papers_2016:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    # Check for physical activity related terms
    has_physical_activity = any(keyword in text_lower or keyword in title_lower for keyword in physical_activity_keywords)
    
    if has_physical_activity:
        total_citations = citation_lookup.get(paper['title'], 0)
        results.append({
            'title': paper['title'],
            'total_citation_count': total_citations
        })

print(f'Found {len(results)} papers from 2016 in physical activity domain:')

# Sort by citations
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

for result in results:
    print(f"  - {result['title']}")
    print(f"    Total citations: {result['total_citation_count']}")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': []}

exec(code, env_args)
