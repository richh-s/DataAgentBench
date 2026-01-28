code = """import json
import re

# Load all data
citations_path = locals()['var_functions.query_db:4']
papers_path = locals()['var_functions.query_db:6']

with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_path, 'r') as f:
    all_papers = json.load(f)

# Build paper lookup with text
paper_texts = {}
for paper in all_papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        paper_texts[title] = paper.get('text', '')

# More comprehensive CHI pattern matching
chi_citations_total = 0
matched_papers = []

# CHI identification patterns
chi_patterns = [
    re.compile(r'CHI\s*\'?(\d{2}|20\d{2})', re.IGNORECASE),  # CHI '15 or CHI 2015
    re.compile(r'Proceedings of the .*?CHI', re.IGNORECASE),  # Proceedings
    re.compile(r'ACM .*?CHI', re.IGNORECASE),  # ACM CHI
    re.compile(r'CHI Conference.*?Human Factors', re.IGNORECASE),  # Full name
]

for citation in citations_2020:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    
    if title in paper_texts:
        text = paper_texts[title]
        header = text[:4000]  # Look in first 4000 chars
        
        # Check each pattern
        is_chi = any(pattern.search(header) for pattern in chi_patterns)
        
        if is_chi:
            chi_citations_total += count
            matched_papers.append({
                'title': title,
                'citations_2020': count
            })

result = {
    'total_citation_count': chi_citations_total,
    'chi_papers_matched': len(matched_papers),
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'total_chi_papers': 1, 'papers_with_citations': 0, 'total_citation_count': 16}, 'var_functions.execute_python:24': {'total_chi_papers': 1, 'total_citations_2020': 16}, 'var_functions.execute_python:28': {'total_citation_count': 16}, 'var_functions.execute_python:30': {'total_citation_count': 114, 'chi_papers_count': 2, 'sample_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations_2020': 16}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citations_2020': 98}]}}

exec(code, env_args)
