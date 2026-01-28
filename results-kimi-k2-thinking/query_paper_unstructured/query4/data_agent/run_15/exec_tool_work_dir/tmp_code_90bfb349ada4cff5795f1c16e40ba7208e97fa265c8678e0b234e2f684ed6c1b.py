code = """import json, re, os

# Load all data
cit_file = locals()['var_functions.query_db:34']
with open(cit_file) as f:
    citations = json.load(f)

paper_file = locals()['var_functions.query_db:2']
with open(paper_file) as f:
    papers = json.load(f)

print('=== DATA LOADED ===')
print(f'Citations: {len(citations)}')
print(f'Papers: {len(papers)}')

# Build citation lookup map
citation_map = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    citation_map[title] = count

print(f'Unique papers in citations: {len(citation_map)}')

# Define physical activity domain keywords
pa_keywords = [
    'physical activity',
    'fitness',
    'exercise',
    'workout',
    'active living',
    'sedentary',
    'step count',
    'calorie burn',
    'heart rate',
    'sports',
    'running',
    'walking',
    'cycling'
]

# Process all papers to find physical activity domain papers
pa_papers_all = []

for i, doc in enumerate(papers):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '').lower()
    
    # Check if paper is in physical activity domain (any keyword)
    is_pa_domain = any(keyword in text or keyword in title.lower() for keyword in pa_keywords)
    
    if not is_pa_domain:
        continue
    
    # Extract publication year from original text (not lowercase)
    orig_text = doc.get('text', '')
    year = None
    
    # Method 1: Copyright line (most reliable)
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', orig_text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
        source = 'copyright'
    
    # Method 2: Conference header with year
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", orig_text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
                source = 'conference'
    
    # Method 3: Published year in citation format
    if not year:
        pub_match = re.search(r'(?:published|presentation|proceeding).*?\b(20\d{2})\b', orig_text[:3000], re.IGNORECASE)
        if pub_match:
            year = int(pub_match.group(1))
            source = 'published'
    
    # Method 4: Look for year with publisher
    if not year:
        publisher_match = re.search(r'\b(20\d{2})\s+(?:ACM|IEEE|PubMed|DOI|ISBN|Springer)', orig_text[:3000])
        if publisher_match:
            year = int(publisher_match.group(1))
            source = 'publisher'
    
    # Method 5: Fallback - most common year in header
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', orig_text[:2000])
        year_candidates = {}
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year_candidates[y] = year_candidates.get(y, 0) + 1
        
        if year_candidates:
            # Take the most frequent year or the one that looks like publication year
            year = max(year_candidates.items(), key=lambda x: x[1])[0]
            source = 'frequency'
    
    # Only include if we found a valid year
    if year:
        pa_papers_all.append({
            'title': filename.replace('.txt', ''),
            'year': year,
            'source': source
        })
        
        if i < 5:  # Debug first few
            print(f'DEBUG Paper {i+1}: {filename.replace(".txt", "")[:60]}...')
            print(f'  Year: {year} (from {source})')
            print(f'  Is PA: {is_pa_domain}')

print(f'\nTotal physical activity papers: {len(pa_papers_all)}')

# Count by year
from collections import Counter
year_counts = Counter([p['year'] for p in pa_papers_all])
print('\nDistribution by year:')
for yr in sorted(year_counts.keys()):
    print(f'  {yr}: {year_counts[yr]} papers')

# Filter for 2016
papers_2016_pa = [p for p in pa_papers_all if p['year'] == 2016]
print(f'\n2016 physical activity papers: {len(papers_2016_pa)}')

# Get citation counts and prepare final results
final_results = []
for paper in papers_2016_pa:
    title = paper['title']
    total_citations = citation_map.get(title, 0)
    final_results.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by citation count (descending)
final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('\n=== FINAL RESULTS ===')
for result in final_results:
    print(f'Title: {result["title"]}')
    print(f'Total Citations: {result["total_citation_count"]}')
    print()

# Prepare JSON output
output_json = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': []}

exec(code, env_args)
