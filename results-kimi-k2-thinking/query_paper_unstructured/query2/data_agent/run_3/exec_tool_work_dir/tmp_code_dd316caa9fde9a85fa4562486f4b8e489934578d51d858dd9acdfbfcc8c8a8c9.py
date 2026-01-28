code = """import json
import os
import re

# Load citations data for 2018
citations_file = 'file_storage/functions.query_db:24.json'
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

print('Loaded', len(citations_2018), 'citation records from 2018')

# Load all paper documents
paper_file = 'file_storage/functions.query_db:38.json'
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

print('Loaded', len(paper_docs), 'paper documents')

# Create a list of ACM papers
acm_papers = []
for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt extension
    else:
        title = filename
    
    # Check if paper is ACM publication
    text = doc.get('text', '')
    is_acm = 'ACM' in text or 'acm' in text
    
    if is_acm:
        acm_papers.append({
            'title': title,
            '_id': doc.get('_id')
        })

print('Found', len(acm_papers), 'ACM papers')

# Create a mapping of titles to citation counts for 2018
citation_map = {item['title']: int(item['citation_count']) for item in citations_2018}

# Find ACM papers that have citations in 2018
acm_citations = []
for paper in acm_papers:
    title = paper['title']
    if title in citation_map:
        acm_citations.append({
            'title': title,
            'citation_count': citation_map[title]
        })

print('Found', len(acm_citations), 'ACM papers cited in 2018')

# Calculate average citation count
if acm_citations:
    total_citations = sum(p['citation_count'] for p in acm_citations)
    avg_citations = total_citations / len(acm_citations)
    print('Average citations for ACM papers in 2018:', avg_citations)
    result = {
        'average_citations': round(avg_citations, 2),
        'paper_count': len(acm_citations),
        'total_citations': total_citations
    }
else:
    print('No ACM papers found with citations in 2018')
    result = {
        'average_citations': 0,
        'paper_count': 0,
        'total_citations': 0
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': "<class 'str'>", 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '20'}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': '13'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'count': 39, 'has_data': True}, 'var_functions.execute_python:28': {'type': "<class 'str'>", 'is_list': False, 'is_string': True}, 'var_functions.execute_python:30': {'source': 'file_path_or_other', 'data_type': "<class 'str'>", 'count': 0}, 'var_functions.execute_python:32': {'file_path': 'file_storage/functions.query_db:24.json', 'path_exists': True}, 'var_functions.execute_python:34': {'citations_count': 158, 'paper_count': 5, 'has_citations': True, 'has_papers': True}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
