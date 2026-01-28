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
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    year = None
    
    # Check for 2016 in various patterns
    if re.search(r'CHI\s+2016', text, re.IGNORECASE):
        year = 2016
    elif re.search(r"CHI\s*'16", text, re.IGNORECASE):
        year = 2016
    elif re.search(r'UbiComp\s+2016', text, re.IGNORECASE):
        year = 2016
    elif re.search(r"UbiComp\s*'16", text, re.IGNORECASE):
        year = 2016
    elif re.search(r'CSCW\s+2016', text, re.IGNORECASE):
        year = 2016
    elif re.search(r"CSCW\s*'16", text, re.IGNORECASE):
        year = 2016
    elif re.search(r'Copyright.*2016', text, re.IGNORECASE):
        year = 2016
    
    # Check domain
    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'
    
    return {'title': title, 'year': year, 'domain': domain}

# Find papers from 2016 in physical activity domain
papers_2016_pa = []
for paper in papers:
    meta = extract_paper_metadata(paper)
    if meta['year'] == 2016 and meta['domain'] == 'physical activity':
        papers_2016_pa.append(meta)

# Create title set for matching
title_set = set(p['title'] for p in papers_2016_pa)

# Calculate total citations
total_citations = 0
for cit in citations:
    if cit.get('title') in title_set:
        total_citations += int(cit.get('citation_count', 0))

print('__RESULT__:')
result = {
    'papers_found': len(papers_2016_pa),
    'titles': [p['title'] for p in papers_2016_pa],
    'total_citations': total_citations
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:10': {'papers_count': 5, 'citations_count': 1405}, 'var_functions.execute_python:12': {'total_papers': 5, 'papers_2016_physical_activity': 0, 'sample_titles': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'papers_loaded': 5, 'citations_loaded': 1405}}

exec(code, env_args)
