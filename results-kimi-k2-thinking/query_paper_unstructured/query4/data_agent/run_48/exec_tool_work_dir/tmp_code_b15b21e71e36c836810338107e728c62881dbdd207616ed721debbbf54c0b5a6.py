code = """import json
import re

# Load the papers data
papers_file = locals()['var_functions.query_db:14']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Load the citations data
citations_file = locals()['var_functions.query_db:9']
with open(citations_file, 'r') as f:
    citations = json.load(f)

def extract_paper_metadata(paper):
    """Extract title, year, and domain from paper document"""
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    
    # Pattern 1: Look for explicit year mentions in venue headers
    # e.g., "CHI 2016", "UbiComp 2016", etc.
    if re.search(r'CHI\s+2016', text, re.IGNORECASE) or \
       re.search(r"CHI\s*'16", text, re.IGNORECASE) or \
       re.search(r'UbiComp\s+2016', text, re.IGNORECASE) or \
       re.search(r"UbiComp\s*'16", text, re.IGNORECASE) or \
       re.search(r'CSCW\s+2016', text, re.IGNORECASE) or \
       re.search(r"CSCW\s*'16", text, re.IGNORECASE):
        year = 2016
    
    # Pattern 2: Look for copyright year 2016
    if not year and re.search(r'Copyright.*2016', text, re.IGNORECASE):
        year = 2016
    
    # Pattern 3: Look for 2016 in header area
    if not year:
        header = text[:1000]
        if '2016' in header and ('proceedings' in header.lower() or 'conference' in header.lower()):
            year = 2016
    
    # Extract domain - check if "physical activity" appears
    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'
    
    return {
        'title': title,
        'year': year,
        'domain': domain
    }

# Process all papers to find those from 2016 in physical activity domain
papers_2016_physical_activity = []
for paper in papers:
    metadata = extract_paper_metadata(paper)
    if metadata['year'] == 2016 and metadata['domain'] == 'physical activity':
        papers_2016_physical_activity.append(metadata)

# Create a set of titles for matching with citations
titles_set = set(p['title'] for p in papers_2016_physical_activity)

# Calculate total citations for these papers
total_citations = 0
for citation in citations:
    title = citation.get('title', '')
    if title in titles_set:
        count = int(citation.get('citation_count', 0))
        total_citations += count

print('__RESULT__:')
print(json.dumps({
    'papers_processed': len(papers),
    'papers_2016_physical_activity': len(papers_2016_physical_activity),
    'paper_titles': [p['title'] for p in papers_2016_physical_activity],
    'total_citations': total_citations
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'papers_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:12': {'total_papers': 5, 'papers_2016_physical_activity': 0, 'sample_titles': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'papers_loaded': 5, 'citations_loaded': 1405}}

exec(code, env_args)
