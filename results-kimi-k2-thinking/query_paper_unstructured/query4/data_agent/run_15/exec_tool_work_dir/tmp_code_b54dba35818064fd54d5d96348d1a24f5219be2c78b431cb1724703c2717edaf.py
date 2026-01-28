code = """import json
import re

# Load all data files
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file, 'r') as f:
    citations = json.load(f)
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Build citation lookup table
citation_lookup = {}
for record in citations:
    title = record.get('title', '')
    count = int(record.get('total_citations', 0))
    citation_lookup[title] = count

# First, let's see what papers exist and their years
all_papers_info = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year - try multiple approaches
    year = None
    
    # 1. Check copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # 2. Check conference header
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # 3. Check for year with publisher
    if not year:
        pub_match = re.search(r'\b(20\d{2})\s+(?:ACM|IEEE|PubMed|DOI|ISBN)\b', text[:3000])
        if pub_match:
            year = int(pub_match.group(1))
    
    # 4. Fallback: first reasonable year in text
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    if year:
        all_papers_info.append({
            'title': title,
            'year': year,
            'text': text
        })

# Show overall statistics
from collections import Counter
year_counts = Counter([p['year'] for p in all_papers_info])

print('=== OVERALL PAPER STATISTICS ===')
print(f'Total papers with valid years: {len(all_papers_info)}')
print(f'Year range: {min(year_counts.keys()) if year_counts else "N/A"} - {max(year_counts.keys()) if year_counts else "N/A"}')

print('\n=== PAPERS BY YEAR ===')
for year in sorted(year_counts.keys()):
    print(f'{year}: {year_counts[year]} papers')

# Check specifically for 2016
papers_2016 = [p for p in all_papers_info if p['year'] == 2016]
print(f'\n=== 2016 PAPERS ===')
print(f'Total 2016 papers: {len(papers_2016)}')

# Check domains for 2016 papers
domain_keywords = [
    'physical activity',
    'fitness',
    'exercise', 
    'workout',
    'sedentary',
    'step count',
    'food',
    'diet',
    'nutrition',
    'sleep',
    'mental',
    'anxiety',
    'health',
    'wellness',
    'productivity',
    'self-tracking',
    'personal informatics'
]

print('\n=== DOMAIN ANALYSIS FOR 2016 PAPERS ===')
papers_2016_with_domains = []

for paper in papers_2016:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    domains = []
    for keyword in domain_keywords:
        if keyword in text_lower or keyword in title_lower:
            domains.append(keyword)
    
    papers_2016_with_domains.append({
        'title': paper['title'],
        'domains': list(set(domains))  # Remove duplicates
    })
    
    if domains:
        print(f"Paper: {paper['title']}")
        print(f"Domains: {', '.join(domains)}")
        print()

# Find papers with physical activity domain
pa_papers_2016 = [p for p in papers_2016_with_domains if any(kw in p['domains'] for kw in ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'step count'])]

print(f'=== 2016 PHYSICAL ACTIVITY PAPERS ===')
print(f'Count: {len(pa_papers_2016)}')

# Add citation counts and prepare final results
final_results = []
for paper in pa_papers_2016:
    title = paper['title']
    total_citations = citation_lookup.get(title, 0)
    final_results.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by citation count
def sort_key_func(item):
    return item['total_citation_count']

final_results.sort(key=sort_key_func, reverse=True)

print('\nResults with citations:')
for result in final_results:
    print(f"Title: {result['title']}")
    print(f"Total citation count: {result['total_citation_count']}")
    print()

# Output final results
print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': []}

exec(code, env_args)
