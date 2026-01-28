code = """import json
import os
import glob

# Find and load citations data for 2020
citation_files = glob.glob('/tmp/*query_db*44*') + glob.glob('/tmp/*query_db*42*')
if not citation_files:
    print('No citation files found')
    citations_2020 = []
else:
    with open(citation_files[0], 'r') as f:
        citations_2020 = json.load(f)

print('Loaded', len(citations_2020), 'citation records')

# Load papers data
paper_files = glob.glob('/tmp/*query_db*2*')
if not paper_files:
    print('No papers file found')
    papers = []
else:
    with open(paper_files[0], 'r') as f:
        papers = json.load(f)

print('Loaded', len(papers), 'paper documents')

# Extract potential CHI papers by looking for CHI in text
chi_paper_titles = set()
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Simple check: if CHI appears in first 1000 chars of text
    if text[:1000].upper().find('CHI') >= 0:
        # Additional context check
        header = text[:1000]
        if header.find('Proceedings') >= 0 or header.find('Conference') >= 0 or header.find('ACM') >= 0:
            chi_paper_titles.add(title.lower())

print('Found', len(chi_paper_titles), 'potential CHI papers')

# Sum citations for CHI papers
total_citations = 0
chi_citation_titles = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_paper_titles:
        count = int(cite.get('citation_count', 0))
        total_citations += count
        chi_citation_titles.append(cite_title)

print('Matched', len(chi_citation_titles), 'CHI papers with citations')

result = {
    'total_citation_count_for_chi_papers_in_2020': total_citations,
    'chi_papers_matched': len(chi_citation_titles),
    'total_chi_papers_found': len(chi_paper_titles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
