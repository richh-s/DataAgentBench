code = """import json
import re

# Load citations data for 2018
citations_file = 'file_storage/functions.query_db:2.json'
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load all paper documents
papers_file = 'file_storage/functions.query_db:26.json'
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of paper titles to publication info
paper_info = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if ACM is the publisher (case-insensitive)
    is_acm = 'ACM' in text or 'acm' in text
    
    paper_info[title] = {
        'title': title,
        'is_acm': is_acm,
        'filename': filename
    }

print('__RESULT__:')
print(json.dumps({
    'total_citations_2018': len(citations_2018),
    'total_papers': len(paper_docs),
    'papers_with_info': len(paper_info)
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample_records': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_papers': 5, 'sample_paper': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:22': {'citations_count': 158, 'papers_count': 5}, 'var_functions.execute_python:24': {'total_papers': 5, 'acm_papers': 5, 'acm_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
