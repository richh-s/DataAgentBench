code = """import json

# Load the data
citations = json.load(open('var_functions.query_db:16'))
papers = json.load(open('var_functions.query_db:2'))

# Create sets of titles for matching
citation_titles = set(c['title'].lower() for c in citations if c.get('title'))
paper_titles = set(p['filename'].replace('.txt', '').lower() for p in papers)

print('Total citations in 2020:', len(citations))
print('Total papers:', len(papers))
print('Sample citation titles:', list(citation_titles)[:5])
print('Sample paper titles:', list(paper_titles)[:5])

# Find CHI papers
chi_key_titles = []
for paper in papers:
    text = paper.get('text', '')[:2000].upper()
    if 'CHI' in text:
        title = paper['filename'].replace('.txt', '')
        chi_key_titles.append(title.lower())

print('Potential CHI papers found:', len(chi_key_titles))

# Match with citations
total_cites = 0
for cite in citations:
    if cite['title'].lower() in chi_key_titles:
        total_cites += int(cite['citation_count'])

print('__RESULT__:')
print(json.dumps({'total_citations': total_cites}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}]}

exec(code, env_args)
