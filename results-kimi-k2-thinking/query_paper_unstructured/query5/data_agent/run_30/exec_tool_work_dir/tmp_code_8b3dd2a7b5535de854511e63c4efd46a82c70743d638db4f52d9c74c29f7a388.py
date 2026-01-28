code = """import json

# Access stored data
citations_2020 = locals()['var_functions.query_db:7']
paper_docs = locals()['var_functions.query_db:9']

# Load from file if needed
if isinstance(citations_2020, str) and citations_2020.endswith('.json'):
    with open(citations_2020, 'r') as f:
        citations_2020 = json.load(f)
if isinstance(paper_docs, str) and paper_docs.endswith('.json'):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Build citation map for 2020
citation_map = {}
for item in citations_2020:
    title = item.get('title', '')
    count = int(item.get('citation_count', 0))
    citation_map[title.lower()] = count

# Identify CHI papers from documents
chi_titles = set()
for paper in paper_docs:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '').lower()
    
    # Look for CHI venue in first part of document
    header = text[:2000]
    
    # Check for CHI-related venue markers
    if ('proceedings of chi' in header or 
        'chi conference' in header or 
        'acm chi' in header or
        ('chi' in header and ('acm' in header or 'sigchi' in header))):
        
        title = paper.get('filename', '').replace('.txt', '')
        chi_titles.add(title.lower())

# Match CHI titles with citations
matched = {}
for chi_title in chi_titles:
    if chi_title in citation_map:
        matched[chi_title] = citation_map[chi_title]

# Sum results
total = sum(matched.values())
result = {
    'total_citation_count': total,
    'chi_papers_with_citations': len(matched)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'total_citation_count': 0, 'chi_papers_cited_in_2020': 0, 'sample_papers': []}}

exec(code, env_args)
