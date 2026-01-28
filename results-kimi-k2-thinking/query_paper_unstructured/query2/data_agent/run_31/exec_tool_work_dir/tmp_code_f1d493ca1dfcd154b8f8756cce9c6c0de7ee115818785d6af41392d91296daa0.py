code = """import json
import re

# Load paper documents
papers_file = 'file_storage/functions.query_db:18.json'
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Extract ACM papers
acm_papers = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if ACM is mentioned in the text (case-insensitive)
    if 'ACM' in text or 'acm' in text:
        acm_papers.append({
            'title': title,
            'filename': filename
        })

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_docs),
    'acm_papers': len(acm_papers),
    'acm_paper_titles': [p['title'] for p in acm_papers]
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample_records': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_papers': 5, 'sample_paper': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:22': {'citations_count': 158, 'papers_count': 5}}

exec(code, env_args)
