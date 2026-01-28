code = """import json
import re

# Load the papers data
papers_file = locals()['var_functions.query_db:26']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Extract metadata from all papers
paper_metadata = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year using multiple patterns
    year = None
    # Pattern 1: Venue with year (e.g., "CHI 2016", "UbiComp '16")
    venue_patterns = [
        (r'\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*["\']?16\b', 2016),
        (r'\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+2016\b', 2016),
        (r'\b2015\b', 2015),
        (r'\b2014\b', 2014),
        (r'\b2013\b', 2013),
    ]
    
    for pattern, yr in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            year = yr
            break
    
    # Pattern 2: Copyright year
    if not year:
        copyright_match = re.search(r'Copyright\s*\u00a9?\s*(\d{4})\b', text, re.IGNORECASE)
        if copyright_match:
            year = int(copyright_match.group(1))
    
    # Extract domains
    domains = []
    text_lower = text.lower()
    if 'physical activity' in text_lower:
        domains.append('physical activity')
    if 'food' in text_lower:
        domains.append('food')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'mental' in text_lower:
        domains.append('mental')
    if 'finances' in text_lower or 'financial' in text_lower:
        domains.append('finances')
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'domains': domains,
        'domain_str': ', '.join(domains) if domains else 'none'
    })

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'papers_with_years': [p for p in paper_metadata if p['year'] is not None],
    'year_distribution': {str(yr): len([p for p in paper_metadata if p['year'] == yr]) for yr in [2013,2014,2015,2016]},
    'domain_distribution': {}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'papers_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:12': {'total_papers': 5, 'papers_2016_physical_activity': 0, 'sample_titles': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'papers_loaded': 5, 'citations_loaded': 1405}, 'var_functions.execute_python:22': {'papers_found': 0, 'titles': [], 'total_citations': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
