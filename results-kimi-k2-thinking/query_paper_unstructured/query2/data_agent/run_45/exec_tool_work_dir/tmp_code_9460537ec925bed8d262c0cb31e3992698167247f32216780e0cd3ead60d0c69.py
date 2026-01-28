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

# Extract paper information from documents
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '')
    
    # Extract source (publisher) - look for ACM, IEEE, PubMed
    source = None
    if 'ACM' in text or 'acm' in text:
        source = 'ACM'
    elif 'IEEE' in text or 'ieee' in text:
        source = 'IEEE'
    elif 'PubMed' in text or 'pubmed' in text:
        source = 'PubMed'
    
    # Extract venue
    venue = None
    venue_patterns = [r'CHI', r'Ubicomp', r'Ubicomp', r'CSCW', r'DIS', r'PervasiveHealth', r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH']
    for pattern in venue_patterns:
        match = re.search(pattern, text)
        if match:
            venue = match.group()
            break
    
    # Extract year
    year = None
    year_match = re.search(r'(19|20)\d{2}', text)
    if year_match:
        year = int(year_match.group())
    
    papers_info.append({
        'title': title,
        'source': source,
        'venue': venue,
        'year': year
    })

# Join with citations data
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

# Calculate average citation count for ACM papers
if acm_papers_with_citations:
    total_citations = sum(p['citation_count'] for p in acm_papers_with_citations)
    avg_citations = total_citations / len(acm_papers_with_citations)
    result = {
        'acm_papers_count': len(acm_papers_with_citations),
        'total_citations': total_citations,
        'average_citations': round(avg_citations, 2),
        'sample_papers': acm_papers_with_citations[:5]
    }
else:
    result = {
        'acm_papers_count': 0,
        'total_citations': 0,
        'average_citations': 0,
        'sample_papers': []
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.execute_python:10': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'record_count': 158, 'sample': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 95}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': 28}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': 58}], 'total_citations': 7949}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
