code = """import json
import re

# Read the full MongoDB result
papers_file_path = locals()['var_functions.query_db:5']
with open(papers_file_path, 'r') as f:
    papers_raw = json.load(f)

# Process papers to extract title, year, and domain
def extract_paper_info(paper):
    # Extract title from filename
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    text = paper.get('text', '')
    year = None
    
    # Look for year patterns like "2016", "'16", venue years, etc.
    year_patterns = [
        r'\b2016\b',  # Explicit 2016
        r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'16",  # Venue '16
        r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*2016",  # Venue 2016
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            year = 2016
            break
    
    # Also check for copyright year
    if not year:
        copyright_match = re.search(r'Copyright\s*\d{4}.*\b(2016)\b', text, re.IGNORECASE)
        if copyright_match:
            year = 2016
    
    # Check if domain contains "physical activity"
    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'
    
    return {
        'title': title,
        'year': year,
        'domain': domain,
        'raw': paper
    }

# Process all papers
processed_papers = []
for paper in papers_raw:
    processed = extract_paper_info(paper)
    if processed['year'] == 2016 and processed['domain'] == 'physical activity':
        processed_papers.append(processed)

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers_raw),
    'papers_2016_physical_activity': len(processed_papers),
    'sample_titles': [p['title'] for p in processed_papers[:5]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'papers_count': 5, 'citations_count': 1405}}

exec(code, env_args)
