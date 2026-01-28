code = """import json
import os
import re

# Load citations data
citations_key = 'var_functions.query_db:0'
citations_data = locals()[citations_key]
if isinstance(citations_data, str) and os.path.exists(citations_data):
    with open(citations_data, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_data

# Load paper documents - ALL of them
papers_key = 'var_functions.query_db:6'
papers_data = locals()[papers_key]
if isinstance(papers_data, str) and os.path.exists(papers_data):
    with open(papers_data, 'r') as f:
        all_papers = json.load(f)
else:
    all_papers = papers_data

print('Total papers available:', len(all_papers))

# Look for CHI papers by examining text for CHI conference patterns
chi_papers = set()
chi_details = []

# Patterns to identify CHI papers
chi_patterns = [
    r'CHI\s+\d{4}',           # CHI 2019, CHI 2020
    r'CHI\s+\'\d{2}',         # CHI '19, CHI '20
    r'CHI\s+CONFERENCE',     # CHI CONFERENCE
    r'PROCEEDINGS\s+OF\s+CHI',  # PROCEEDINGS OF CHI
    r'ACM\s+CHI',            # ACM CHI
]

for doc in all_papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    text_upper = text.upper()
    
    # Check if text contains CHI
    if 'CHI' in text_upper:
        # Use regex patterns for more precise matching
        for pattern in chi_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                chi_papers.add(title)
                chi_details.append({'title': title, 'pattern': pattern})
                break

print('CHI papers identified:', len(chi_papers))
print('Example CHI papers:', list(chi_papers)[:5])

# Now count citations for these CHI papers in 2020
total_chi_citations = 0
chi_cited_count = 0
matched_titles = []

for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_papers:
        count = int(citation.get('citation_count', 0))
        total_chi_citations += count
        chi_cited_count += 1
        matched_titles.append({'title': citation_title, 'count': count})

result = {
    'chi_papers_identified': len(chi_papers),
    'chi_papers_cited_in_2020': chi_cited_count,
    'total_chi_citations_2020': total_chi_citations,
    'sample_matched_papers': matched_titles[:10],
    'all_2020_citations_total': len(citations_2020)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully', 'var_functions.execute_python:14': {'chi_papers_total': 5, 'chi_papers_cited': 4, 'total_citations_2020': 243, 'sample_matched_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.execute_python:18': {'chi_papers_total': 0, 'chi_papers_cited_2020': 0, 'total_citations_2020': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': {'chi_papers': 0, 'chi_cited_2020': 0, 'total_citations': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:34': {'chi_papers_identified': 0, 'chi_papers_cited_in_2020': 0, 'total_citation_count_2020': 0}, 'var_functions.execute_python:36': {'target_paper_found': True, 'target_paper_citations': 16, 'sample_matches': {'A Lived Informatics Model of Personal Informatics': 77, 'A Trip to the Moon: Personalized Animated Movies for Self-reflection': 98, 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation': 52}}, 'var_functions.execute_python:38': {'total_2020_citations': 188, 'total_papers': 5}, 'var_functions.execute_python:42': {'total_2020_citations_all_papers': 9576, 'number_of_cited_papers': 188}}

exec(code, env_args)
