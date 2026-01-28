code = """import json
import re

# Load data
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# Extract all papers with years
papers_with_years = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Try to find year
    year = None
    
    # Copyright line
    m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if m:
        year = int(m.group(1))
    
    # Conference header
    if not year:
        m = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if m:
            yr = int(m.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Any year
    if not year:
        years = re.findall(r'\b20\d{2}\b', text[:2000])
        for y in years:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                break
    
    if year:
        papers_with_years.append({'title': title, 'year': year, 'text': text})

from collections import Counter
year_counts = Counter([p['year'] for p in papers_with_years])

print('=== YEAR DISTRIBUTION ===')
for year in sorted(year_counts.keys()):
    print(f"{year}: {year_counts[year]} papers")

# Check 2016 specifically
papers_2016 = [p for p in papers_with_years if p['year'] == 2016]
print(f"\n=== 2016 PAPERS ===")
print(f"Total 2016 papers: {len(papers_2016)}")

# Check for PA terms using simple keyword search
pa_results = []

for paper in papers_2016:
    title_lower = paper['title'].lower()
    text_lower = paper['text'].lower()
    
    # Simple keyword check
    is_pa = False
    keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'step', 'running', 'walking', 'sports']
    for kw in keywords:
        if kw in title_lower or kw in text_lower:
            is_pa = True
            break
    
    if is_pa:
        citations = citation_lookup.get(paper['title'], 0)
        pa_results.append({'title': paper['title'], 'total_citation_count': citations})

pa_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print(f"\n=== PHYSICAL ACTIVITY PAPERS (2016) ===")
print(f"Found: {len(pa_results)}")

for result in pa_results:
    print(f"Title: {result['title']}")
    print(f"Citations: {result['total_citation_count']}")
    print()

# If none found, show all 2016 papers
if not pa_results:
    print("No physical activity papers found. All 2016 papers:")
    for paper in papers_2016:
        citations = citation_lookup.get(paper['title'], 0)
        print(f"  - {paper['title']} ({citations} citations)")

print('__RESULT__:')
print(json.dumps(pa_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': [], 'var_functions.execute_python:68': []}

exec(code, env_args)
