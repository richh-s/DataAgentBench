code = """import json
import re

# Load 2018 citations data
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents data
papers_file = locals()['var_functions.query_db:16']
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of paper titles to citation counts for 2018
citation_map = {}
for item in citations_2018:
    title = item['title']
    citation_map[title] = int(item['citation_count'])

# Extract paper information from documents with improved patterns
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '')
    
    # Extract source (publisher) - look for ACM, IEEE, PubMed (case-insensitive)
    source = None
    text_lower = text.lower()
    if 'acm' in text_lower:
        source = 'ACM'
    elif 'ieee' in text_lower:
        source = 'IEEE'
    elif 'pubmed' in text_lower:
        source = 'PubMed'
    
    # Extract venue
    venue = None
    venue_patterns = [r'CHI', r'Ubicomp', r'UbiComp', r'CSCW', r'DIS', r'PervasiveHealth', r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH']
    for pattern in venue_patterns:
        match = re.search(pattern, text)
        if match:
            venue = match.group()
            break
    
    # Extract year from various patterns
    year = None
    # Look for copyright year patterns
    year_match = re.search(r'Copyright\s+(?:\xa9\s+)?(19|20)\d{2}', text)
    if not year_match:
        year_match = re.search(r'(19|20)\d{2}\s+(Proceedings|Conference|Symposium)', text)
    if not year_match:
        year_match = re.search(r'(19|20)\d{2}', text)
    if year_match:
        try:
            year = int(year_match.group(1) + year_match.group(0)[-2:])
        except:
            year = int(year_match.group(0))
    
    papers_info.append({
        'title': title,
        'source': source,
        'venue': venue,
        'year': year
    })

# Join with citations data and filter for ACM papers
acm_papers_with_citations = []
for paper in papers_info:
    title = paper['title']
    if title in citation_map and paper['source'] == 'ACM':
        acm_papers_with_citations.append({
            'title': title,
            'citation_count': citation_map[title],
            'year': paper['year'],
            'venue': paper['venue']
        })

# Calculate statistics
if acm_papers_with_citations:
    total_citations = sum(p['citation_count'] for p in acm_papers_with_citations)
    avg_citations = total_citations / len(acm_papers_with_citations)
    result = {
        'acm_papers_count': len(acm_papers_with_citations),
        'total_citations': total_citations,
        'average_citations': round(avg_citations, 2),
        'all_acm_papers': acm_papers_with_citations
    }
else:
    result = {
        'acm_papers_count': 0,
        'total_citations': 0,
        'average_citations': 0,
        'all_acm_papers': []
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:10': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 95}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': 28}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': 58}], 'total_citations': 7949}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'acm_papers_count': 2, 'total_citations': 137, 'average_citations': 68.5, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 50, 'year': 2015, 'venue': 'CHI'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': 87, 'year': 2016, 'venue': 'CHI'}]}}

exec(code, env_args)
