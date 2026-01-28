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

# Create mapping of paper titles to ACM status
title_to_acm = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if ACM is mentioned (publisher)
    is_acm = bool(re.search(r'\bACM\b', text, re.IGNORECASE))
    
    if title:
        title_to_acm[title] = is_acm

# Find ACM papers cited in 2018
acm_citations = []
non_acm_citations = []

for citation in citations_2018:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if this title is an ACM paper
    if title in title_to_acm and title_to_acm[title]:
        acm_citations.append(citation_count)
    else:
        non_acm_citations.append(citation_count)

# Calculate average for ACM papers
avg_acm_citations = sum(acm_citations) / len(acm_citations) if acm_citations else 0

print('__RESULT__:')
print(json.dumps({
    'total_cited_papers_2018': len(citations_2018),
    'acm_papers_cited_in_2018': len(acm_citations),
    'non_acm_papers_cited_in_2018': len(non_acm_citations),
    'average_citation_count_acm': round(avg_acm_citations, 2),
    'acm_citation_counts': acm_citations[:10]  # Sample
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample_records': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_papers': 5, 'sample_paper': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:22': {'citations_count': 158, 'papers_count': 5}, 'var_functions.execute_python:24': {'total_papers': 5, 'acm_papers': 5, 'acm_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_citations_2018': 158, 'total_papers': 99, 'papers_with_info': 99}, 'var_functions.execute_python:30': {'total_papers_in_db': 99, 'acm_papers_total': 95, 'sample_titles': [['A Lived Informatics Model of Personal Informatics', True], ['A Stage-based Model of Personal Informatics Systems', True], ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', True], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', True], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', True]]}}

exec(code, env_args)
