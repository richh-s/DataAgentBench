code = """import json, re

# Load data
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# Check what papers exist - analyze first 20 papers thoroughly
print('=== ANALYZING PAPER SAMPLE ===')
physical_activity_terms = [
    'physical activity',
    'fitness',
    'exercise',
    'workout',
    'sedentary',
    'step count',
    'step tracking',
    'activity tracking'
]

sample_analysis = []
for i, doc in enumerate(papers[:50]):  # Check first 50 papers
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Count occurrences of PA terms
    text_lower = text.lower()
    pa_term_counts = {}
    for term in physical_activity_terms:
        count = text_lower.count(term)
        if count > 0:
            pa_term_counts[term] = count
    
    # Extract year
    year = None
    
    # Look at actual text structure to find year
    header_lines = text.split('\n')[:20]  # First 20 lines
    header_text = '\n'.join(header_lines)
    
    # Find all years in header
    year_matches = re.findall(r'\b20\d{2}\b', header_text)
    valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
    
    if valid_years:
        year = valid_years[0]
    
    # Look for specific patterns
    patterns = [
        r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})',
        r'\b(20\d{2})\b\s*(?:ACM|IEEE|Springer|DOI)',
        r'(?:CHI|UbiComp|CSCW|DIS)\s*\'?(\d{2})',
        r'\b(20\d{2})\b.*?(?:conference|proceeding|published)'
    ]
    
    found_years = []
    for pattern in patterns:
        matches = re.findall(pattern, header_text, re.IGNORECASE)
        found_years.extend(matches)
    
    if found_years:
        # Take the most specific year
        for y in found_years:
            if len(y) == 4 and 2010 <= int(y) <= 2025:
                year = int(y)
                break
            elif len(y) == 2 and int(y) < 50:
                year = 2000 + int(y)
                break
    
    has_pa = len(pa_term_counts) > 0
    
    sample_analysis.append({
        'index': i,
        'title': title,
        'has_physical_activity': has_pa,
        'pa_terms': pa_term_counts,
        'year': year,
        'year_candidates': valid_years,
        'found_year_patterns': found_years
    })
    
    if has_pa:
        print(f"Paper {i}: {title[:80]}")
        print(f"  Has PA terms: {pa_term_counts}")
        print(f"  Year found: {year}")
        print(f"  Year candidates: {valid_years}")
        print(f"  Year patterns: {found_years}")
        print()

# Now process ALL papers
all_pa_papers = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check for physical activity domain
    has_pa = any(term in text_lower for term in physical_activity_terms)
    
    if not has_pa:
        continue
    
    # Extract year more aggressively
    year = None
    
    # Try all patterns
    patterns = [
        r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})',
        r'\b(20\d{2})\b\s*(?:ACM|IEEE|Springer|DOI|ISBN)',
        r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*\'?(\d{2})',
        r'(?:Published|Presented|Proceedings).*?\b(20\d{2})\b',
        r'\b(20\d{2})\b.*?(?:conference|proceeding|symposium)',
        r'UBICOMP\s*[\'‘]?(\d{2})'
    ]
    
    header_text = '\n'.join(text.split('\n')[:30])
    
    for pattern in patterns:
        matches = re.findall(pattern, header_text, re.IGNORECASE)
        for match in matches:
            if len(match) == 4:
                year_int = int(match)
                if 2010 <= year_int <= 2025:
                    year = year_int
                    break
            elif len(match) == 2:
                year_int = int(match)
                if year_int < 50:
                    year = 2000 + year_int
                    break
        if year:
            break
    
    # Last resort: look for any 4-digit year in header
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', header_text)
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = valid_years[0]
    
    if year:
        all_pa_papers.append({
            'title': title,
            'year': year
        })

print(f"=== SUMMARY ===")
print(f"Total papers with PA terms: {len(all_pa_papers)}")

# Check year distribution
from collections import Counter
year_dist = Counter([p['year'] for p in all_pa_papers])
print(f"\nYear distribution:")
for yr in sorted(year_dist.keys()):
    print(f"  {yr}: {year_dist[yr]} papers")

# Filter for 2016
papers_2016 = [p for p in all_pa_papers if p['year'] == 2016]
print(f"\n2016 papers: {len(papers_2016)}")

# Get results with citations
final_results = []
for paper in papers_2016:
    title = paper['title']
    citations = citation_lookup.get(title, 0)
    final_results.append({
        'title': title,
        'total_citation_count': citations
    })

# Sort
final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("\nFinal results:")
for r in final_results:
    print(f"  {r['title']}: {r['total_citation_count']} citations")

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
