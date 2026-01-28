code = """import json
import re

# Load the citations data from 2018
citations_file = locals()['var_functions.query_db:0']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load all paper documents
papers_file = locals()['var_functions.query_db:2']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Create a set of ACM paper titles from our paper documents
acm_titles = set()
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for ACM indicators in the text
    acm_patterns = [
        'ACM Classification Keywords',
        'ACM 978-1-4503',
        'Association for Computing Machinery',
        'http://dx.doi.org/10.1145/',
    ]
    
    is_acm = any(pattern in text for pattern in acm_patterns)
    
    if is_acm and title:
        acm_titles.add(title)

# Now find which papers in the 2018 citations are ACM papers
acm_citations = []
for citation in citations_data:
    citation_title = citation.get('title', '')
    if citation_title in acm_titles:
        acm_citations.append({
            'title': citation_title,
            'citation_count': int(citation.get('citation_count', 0))
        })

# Calculate average citation count
if acm_citations:
    avg_citations = sum(c['citation_count'] for c in acm_citations) / len(acm_citations)
    result = {
        'acm_papers_found': len(acm_citations),
        'total_citations_2018': len(citations_data),
        'average_citation_count': round(avg_citations, 2),
        'acm_citations': acm_citations
    }
else:
    result = {
        'acm_papers_found': 0,
        'total_citations_2018': len(citations_data),
        'average_citation_count': 0,
        'note': 'No ACM papers found in the 2018 citations'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'status': 'success', 'citations_count': 158, 'sample_citations': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.execute_python:10': {'total_papers': 5, 'acm_papers': 5, 'sample_acm_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'is_acm': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'is_acm': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'is_acm': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'is_acm': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'is_acm': True}]}}

exec(code, env_args)
