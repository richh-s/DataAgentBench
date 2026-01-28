code = """import json
import re

# Load data files
citation_path = locals()['var_functions.query_db:0']
papers_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Initial diagnostics
print('=== DATA OVERVIEW ===')
print('Total citations in database: ' + str(len(citations)))
print('Total papers in database: ' + str(len(papers)))
print('\nSample citation titles:')
for i in range(min(3, len(citations))):
    print('  ' + citations[i]['title'][:80])

print('\nSample paper filenames:')
for i in range(min(3, len(papers))):
    filename = papers[i].get('filename', '')
    print('  ' + filename[:80])

# Analyze year patterns and empirical papers
year_distribution = {}
empirical_distribution = {}
all_empirical_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Extract year using multiple patterns
    year = None
    
    # Pattern 1: Four digit year like 2017, 2018, etc.
    match = re.search(r'\b(20[1-2][0-9])\b', text)
    if match:
        year = int(match.group(1))
    else:
        # Pattern 2: Two digit year in conference format like '17, '18
        match = re.search(r"\B'([0-9]{2})\b", text)
        if match:
            year_num = int(match.group(1))
            year = 2000 + year_num if year_num < 50 else 1900 + year_num
        else:
            # Pattern 3: Year mentioned in text
            match = re.search(r'\b(201[7-9]|202[0-9])\b', text[:500])
            if match:
                year = int(match.group(1))
    
    has_empirical = 'empirical' in text.lower()
    
    if year:
        year_distribution[year] = year_distribution.get(year, 0) + 1
        if has_empirical:
            empirical_distribution[year] = empirical_distribution.get(year, 0) + 1
            if year > 2016:
                all_empirical_papers.append({
                    'title': title,
                    'year': year,
                    'text_preview': text[:200]
                })

print('\n=== YEAR DISTRIBUTION ===')
sorted_years = sorted(year_distribution.keys())
for year in sorted_years:
    emp_count = empirical_distribution.get(year, 0)
    total_count = year_distribution[year]
    print(f'Year {year}: {emp_count} empirical / {total_count} total')

print('\n=== EMPIRICAL PAPERS AFTER 2016 ===')
print(f'Total: {len(all_empirical_papers)} papers')

# Check for title matches with citations
if len(all_empirical_papers) > 0:
    print('\nFirst 5 empirical papers after 2016:')
    for i, paper in enumerate(all_empirical_papers[:5]):
        print(f"{i+1}. {paper['title']}")
        print(f"   Year: {paper['year']}")

# Try to match titles using normalization
citation_titles = set(c['title'] for c in citations)
magical_matches = []

for emp_pos, emp_paper in enumerate(all_empirical_papers):
    paper_title_clean = re.sub(r'[^a-zA-Z0-9]', '', emp_paper['title'].lower())
    
    for cit_title in citation_titles:
        cit_title_clean = re.sub(r'[^a-zA-Z0-9]', '', cit_title.lower())
        
        if paper_title_clean == cit_title_clean:
            # Found a match, get citation count
            citation_count = 0
            for c in citations:
                if c['title'] == cit_title:
                    citation_count = int(c['total_citations'])
                    break
            
            magical_matches.append({
                'title': emp_paper['title'],
                'year': emp_paper['year'],
                'total_citations': citation_count
            })
            break

print('\n=== MATCH WITH CITATIONS ===')
print(f'Papers matched with citation data: {len(magical_matches)}')

if len(magical_matches) > 0:
    print('\nTop 10 by citation count:')
    magical_matches.sort(key=lambda x: x['total_citations'], reverse=True)
    for i, paper in enumerate(magical_matches[:10]):
        title_part = paper['title'][:70]
        print(f"{i+1}. {title_part}...")
        print(f"   Year: {paper['year']}, Citations: {paper['total_citations']}")

# Return the final results
print('\n__RESULT__:')
print(json.dumps(magical_matches, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': []}

exec(code, env_args)
