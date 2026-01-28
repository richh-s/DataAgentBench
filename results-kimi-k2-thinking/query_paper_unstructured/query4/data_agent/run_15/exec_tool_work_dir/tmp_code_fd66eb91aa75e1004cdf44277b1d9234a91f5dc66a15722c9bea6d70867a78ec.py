code = """import json, re

# Load citation summaries
cit_path = locals()['var_functions.query_db:34']
with open(cit_path) as f:
    citations = json.load(f)

# Load paper documents
paper_path = locals()['var_functions.query_db:2']
with open(paper_path) as f:
    papers = json.load(f)

print('=== LOADED ===')
print(f'Papers: {len(papers)}')
print(f'Citation summaries: {len(citations)}')

# Build citation lookup table
cit_lookup = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    cit_lookup[title] = count

print(f'Unique papers with citation data: {len(cit_lookup)}')
print(f'Example: {list(cit_lookup.items())[0]}')

# Find all physical activity papers
pa_papers = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check for physical activity in text
    if 'physical activity' not in text.lower():
        continue
    
    # Extract year
    year = None
    
    # Try copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Try conference header
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:2000])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Try general search
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:3000])
        for y in year_matches:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                break
    
    if year:
        pa_papers.append({'title': title, 'year': year})

print(f'\nPhysical activity papers total: {len(pa_papers)}')

# Count by year
from collections import Counter
year_counts = Counter([p['year'] for p in pa_papers])
for yr in sorted(year_counts.keys()):
    print(f'  {yr}: {year_counts[yr]}')

# Filter 2016
papers_2016 = [p for p in pa_papers if p['year'] == 2016]
print(f'\n2016 physical activity papers: {len(papers_2016)}')

results = []
for p in papers_2016:
    title = p['title']
    citations = cit_lookup.get(title, 0)
    results.append({'title': title, 'total_citation_count': citations})

# Sort by citation count
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

for r in results:
    print(f"Title: {r['title']}")
    print(f"Citations: {r['total_citation_count']}")
    print()

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': []}

exec(code, env_args)
