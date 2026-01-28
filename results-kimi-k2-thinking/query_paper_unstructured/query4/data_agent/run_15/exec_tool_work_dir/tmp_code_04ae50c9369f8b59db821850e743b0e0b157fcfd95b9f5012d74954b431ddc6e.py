code = """import json

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Load citations
citations = locals()['var_functions.query_db:16']

print("=== DATA OVERVIEW ===")
print(f"Total papers: {len(papers)}")
print(f"Total citation records: {len(citations)}")
print()

# Examine first 5 papers in detail
print("=== SAMPLE PAPERS ===")
for i in range(min(5, len(papers))):
    doc = papers[i]
    title = doc.get('filename', '').replace('.txt', '')
    text_start = doc.get('text', '')[:300]
    print(f"Paper {i+1}:")
    print(f"  Title: {title[:80]}")
    print(f"  Text start: {text_start[:100].replace(chr(10), ' ')}")
    print()

# Count all papers by year
import re
from collections import defaultdict

year_counts = defaultdict(int)
pa_year_counts = defaultdict(int)
paper_years = {}

for doc in papers:
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year
    year = None
    matches = re.findall(r'\b20\d{2}\b', text[:2000])
    for m in matches:
        y = int(m)
        if 2010 <= y <= 2025:
            year = y
            break
    
    if year:
        year_counts[year] += 1
        paper_years[title] = year
    
        # Check for physical activity
        if 'physical activity' in text.lower():
            pa_year_counts[year] += 1

print("=== YEAR DISTRIBUTION ===")
for year in sorted(year_counts.keys()):
    total = year_counts[year]
    pa = pa_year_counts[year]
    print(f"{year}: {total} total papers, {pa} physical activity papers")

print()
print("=== 2016 PAPERS ===")
papers_2016 = []
for title, year in paper_years.items():
    if year == 2016:
        papers_2016.append(title)

print(f"Total 2016 papers: {len(papers_2016)}")
for title in papers_2016[:10]:
    print(f"  - {title}")

# Check which 2016 papers mention physical activity
print()
print("=== 2016 PAPERS WITH PHYSICAL ACTIVITY ===")
for doc in papers:
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    
    matches = re.findall(r'\b20\d{2}\b', text[:2000])
    year = None
    for m in matches:
        y = int(m)
        if 2010 <= y <= 2025:
            year = y
            break
    
    if year == 2016 and 'physical activity' in text.lower():
        print(f"  - {title}")

print('__RESULT__:')
print(json.dumps({'total_papers': len(papers), 'papers_2016': len(papers_2016)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': []}

exec(code, env_args)
