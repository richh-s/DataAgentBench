code = """import json

# Load all papers and citations
papers_path = locals()['var_functions.query_db:6']
citations_path = locals()['var_functions.query_db:4']

with open(papers_path, 'r') as f:
    all_papers = json.load(f)

with open(citations_path, 'r') as f:
    all_citations = json.load(f)

# Build citation lookup for 2020
citation_lookup = {item['title']: int(item['citation_count']) for item in all_citations}

# Better CHI detection with multiple patterns
import re

chi_total = 0
papers_found = 0
matches = []

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Multiple patterns to identify CHI papers
    header = text[:3000].upper()
    
    # Check if CHI appears and it's not just a word in the text
    is_chi = False
    
    # Pattern 1: CHI with year format
    if re.search(r'CHI\s*\'?(\d{2}|\d{4})', text):
        is_chi = True
    # Pattern 2: Proceedings of CHI
    elif 'PROCEEDINGS OF THE' in header and 'CHI' in header:
        is_chi = True
    # Pattern 3: ACM CHI Conference
    elif 'ACM' in header and 'CHI' in header and 'CONFERENCE' in header:
        is_chi = True
    # Pattern 4: CHI Conference on Human Factors
    elif 'CHI' in header and 'HUMAN FACTORS' in header:
        is_chi = True
    
    if is_chi and title in citation_lookup:
        count = citation_lookup[title]
        chi_total += count
        papers_found += 1
        matches.append({'title': title, 'citations': count})

result = {
    'total_citations_2020': chi_total,
    'chi_papers_count': papers_found,
    'sample_matches': matches[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'total_chi_papers': 1, 'papers_with_citations': 0, 'total_citation_count': 16}, 'var_functions.execute_python:24': {'total_chi_papers': 1, 'total_citations_2020': 16}}

exec(code, env_args)
