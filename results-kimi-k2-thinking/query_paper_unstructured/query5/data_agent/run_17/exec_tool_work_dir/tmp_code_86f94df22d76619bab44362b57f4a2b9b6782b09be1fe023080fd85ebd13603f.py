code = """import json
import os

# Read the file path for CHI papers data
chi_papers_file = locals()['var_functions.query_db:2']

# Load the CHI papers data
with open(chi_papers_file, 'r') as f:
    chi_papers_data = json.load(f)

# Get citations for 2020
citations_2020_data = locals()['var_functions.query_db:5']

# Extract paper titles from CHI papers (from filename without .txt)
chi_titles = []
for paper in chi_papers_data:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    chi_titles.append(title)

# Create a set for faster lookup
chi_titles_set = set(chi_titles)

# Filter citations for 2020 that match CHI papers
chi_citations_2020 = []
total_citations = 0

for citation in citations_2020_data:
    if citation['title'] in chi_titles_set:
        chi_citations_2020.append(citation)
        total_citations += int(citation['citation_count'])

print('__RESULT__:')
print(json.dumps({
    'chi_papers_total': len(chi_titles),
    'matching_citations_count': len(chi_citations_2020),
    'total_citation_count_2020': total_citations,
    'sample_matches': chi_citations_2020[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:8': {'chi_papers_count': 38, 'citations_2020_count': 10}}

exec(code, env_args)
