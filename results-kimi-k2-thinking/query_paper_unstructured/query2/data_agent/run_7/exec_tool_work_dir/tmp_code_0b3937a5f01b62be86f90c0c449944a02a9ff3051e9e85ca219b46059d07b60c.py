code = """import json
import re

# Load the papers data from the file
papers_file = locals()['var_functions.query_db:2']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Extract paper information
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is published by ACM
    # Look for ACM indicators in the text
    is_acm = False
    
    # Common ACM indicators
    acm_patterns = [
        'ACM Classification Keywords',
        'ACM 978-1-4503',
        'ACM,',
        'Association for Computing Machinery',
        'Permission to make digital or hard copies of all or part of this work',
        'http://dx.doi.org/10.1145/',
        'Ubicomp',  # Often ACM
        'CHI',      # Often ACM
        'CSCW',     # Often ACM
    ]
    
    for pattern in acm_patterns:
        if pattern in text:
            is_acm = True
            break
    
    if is_acm:
        papers_info.append({
            'title': title,
            'filename': filename,
            'is_acm': True
        })

print('__RESULT__:')
print(json.dumps({
    "total_papers": len(papers_data),
    "acm_papers": len(papers_info),
    "sample_acm_papers": papers_info[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'status': 'success', 'citations_count': 158, 'sample_citations': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}}

exec(code, env_args)
