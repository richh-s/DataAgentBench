code = """import json, re, os

# Load data
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# First, let's simply check for ANY 2016 papers regardless of domain
print("=== CHECKING FOR 2016 PAPERS ===")

papers_2016_all = []
papers_with_years = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Look for year in copyright line
    year = None
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    if year == 2016:
        papers_2016_all.append(title)
    
    if year:
        papers_with_years.append({'title': title, 'year': year, 'text': text})

print(f"Total papers found: {len(papers)}")
print(f"Papers with extractable years: {len(papers_with_years)}")
print(f"Papers from 2016 (any domain): {len(papers_2016_all)}")

if papers_2016_all:
    print("\nSample 2016 papers:")
    for title in papers_2016_all[:10]:
        citations = citation_lookup.get(title, 0)
        print(f"  - {title} (citations: {citations})")

# Now check physical activity domain
print("\n=== CHECKING PHYSICAL ACTIVITY DOMAN ===")

# Define PA keywords more broadly
pa_terms = ['physical activity', 'fitness', 'exercise', 'workout', 'active', 'steps', 'running', 'walking', 'sports']

pa_papers_found = []
for paper in papers_with_years:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    # Check for PA terms
    has_pa = any(term in text_lower or term in title_lower for term in pa_terms)
    
    if has_pa:
        pa_papers_found.append(paper)

print(f"Physical activity papers (all years): {len(pa_papers_found)}")

# Check year distribution of PA papers
from collections import Counter
pa_years = Counter([p['year'] for p in pa_papers_found])
print("PA papers by year:")
for yr in sorted(pa_years.keys()):
    print(f"  {yr}: {pa_years[yr]}")

# Check 2016 specifically
pa_2016 = [p for p in pa_papers_found if p['year'] == 2016]
print(f"\n2016 PA papers: {len(pa_2016)}")

# Get final results
final_results = []
for paper in pa_2016:
    title = paper['title']
    citations = citation_lookup.get(title, 0)
    final_results.append({
        'title': title,
        'total_citation_count': citations
    })

# Sort by citations
final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("\n=== FINAL RESULTS ===")
for result in final_results:
    print(f"Title: {result['title']}")
    print(f"Total citation count: {result['total_citation_count']}")
    print()

if not final_results:
    print("No papers from 2016 in physical activity domain were found in the dataset.")

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
