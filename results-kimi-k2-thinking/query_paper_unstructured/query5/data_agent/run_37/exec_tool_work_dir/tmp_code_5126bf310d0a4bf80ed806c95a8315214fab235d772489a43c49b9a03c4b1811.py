code = """import json
import re

# Get the stored results
citations_result = globals().get('var_functions.query_db:5', [])
papers_result = globals().get('var_functions.query_db:6', [])

# If they're file paths, read them
if isinstance(citations_result, str):
    citations_data = json.load(open(citations_result))
else:
    citations_data = citations_result
    
if isinstance(papers_result, str):
    paper_docs = json.load(open(papers_result))
else:
    paper_docs = papers_result

# Find CHI papers
chi_titles = set()
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    if 'CHI' in text.upper():
        title = filename.replace('.txt', '')
        chi_titles.add(title)

# Sum citations for CHI papers in 2020
total = 0
matches = []
for cite in citations_data:
    title = cite.get('title', '')
    count = int(cite.get('citation_count', 0))
    if title in chi_titles:
        total += count
        matches.append({'title': title, 'citations': count})

matches.sort(key=lambda x: x['citations'], reverse=True)

result = {
    'total_citation_count': total,
    'chi_papers_count': len(matches),
    'top_papers': matches[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
