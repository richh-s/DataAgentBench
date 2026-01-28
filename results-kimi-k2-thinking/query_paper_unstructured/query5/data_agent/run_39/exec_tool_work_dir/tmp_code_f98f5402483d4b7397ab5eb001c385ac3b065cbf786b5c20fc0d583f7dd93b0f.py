code = """import json
import re

# Get file paths from variables
paper_docs_path = locals()['var_functions.query_db:6']
citations_path = locals()['var_functions.query_db:4']

# Load data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Build citation lookup for 2020
citation_lookup = {}
for item in citations:
    try:
        title = item.get('title', '')
        count = int(item.get('citation_count', 0))
        citation_lookup[title] = count
    except:
        continue

# Process papers
total_citations = 0
chi_papers_count = 0

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if CHI paper (case insensitive)
    if title and 'CHI' in text[:2000]:
        chi_papers_count += 1
        if title in citation_lookup:
            total_citations += citation_lookup[title]

print('__RESULT__:')
print(json.dumps({
    'total_chi_papers': chi_papers_count,
    'papers_with_citations': len([t for t in citation_lookup.keys() if 'CHI' in t]),
    'total_citation_count': total_citations
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
