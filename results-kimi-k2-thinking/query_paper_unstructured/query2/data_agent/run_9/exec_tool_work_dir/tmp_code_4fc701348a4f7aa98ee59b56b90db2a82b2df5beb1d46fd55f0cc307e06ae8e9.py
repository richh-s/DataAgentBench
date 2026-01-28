code = """import json
import re

# Load the paper documents
papers_file = locals()['var_functions.query_db:16']
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information from MongoDB documents
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Extract source/publisher - look for ACM, IEEE, PubMed in the text
    source = []
    if 'ACM' in text or 'acm' in text:
        source.append('ACM')
    if 'IEEE' in text or 'ieee' in text:
        source.append('IEEE')
    if 'PubMed' in text or 'pubmed' in text or 'Pub Med' in text:
        source.append('PubMed')
    
    # Also look for publisher mentions in headers
    acm_patterns = ['ACM', 'Association for Computing Machinery', 'acm.org', 'dx.doi.org']
    ieee_patterns = ['IEEE', 'Institute of Electrical and Electronics Engineers', 'ieee.org']
    
    for pattern in acm_patterns:
        if pattern in text and 'ACM' not in source:
            source.append('ACM')
    for pattern in ieee_patterns:
        if pattern in text and 'IEEE' not in source:
            source.append('IEEE')
    
    papers_info.append({
        'title': title,
        'filename': filename,
        'source': source
    })

print('__RESULT__:')
print(json.dumps(papers_info, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample': {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'citations_2018_count': 158, 'paper_docs_count': 5}}

exec(code, env_args)
