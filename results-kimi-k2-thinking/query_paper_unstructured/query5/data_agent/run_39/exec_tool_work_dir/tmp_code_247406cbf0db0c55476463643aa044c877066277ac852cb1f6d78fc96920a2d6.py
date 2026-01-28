code = """import json

# Access file paths from variables
papers_file = locals()['var_functions.query_db:6']
citations_file = locals()['var_functions.query_db:4']

# Load data
with open(papers_file, 'r') as f:
    papers_list = json.load(f)

with open(citations_file, 'r') as f:
    citations_list = json.load(f)

# Build citations dictionary
citations_dict = {}
for citation in citations_list:
    title = citation.get('title')
    if title:
        citations_dict[title] = int(citation.get('citation_count', 0))

# Check papers for CHI and sum citations
total_citations = 0

for paper in papers_list:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if title and title in citations_dict:
        text = paper.get('text', '')
        if 'CHI' in text[:2000]:
            total_citations += citations_dict[title]

result = {'total_citation_count': total_citations}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'total_chi_papers': 1, 'papers_with_citations': 0, 'total_citation_count': 16}, 'var_functions.execute_python:24': {'total_chi_papers': 1, 'total_citations_2020': 16}}

exec(code, env_args)
