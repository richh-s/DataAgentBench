code = """import json, glob, os, re

# Load 2020 citations
citation_path = '/tmp/var_functions.query_db:62'
with open(citation_path, 'r') as f:
    citations_2020 = json.load(f)

# Load papers
papers_path = '/tmp/var_functions.query_db:2'
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Citations loaded:', len(citations_2020))
print('Papers loaded:', len(papers))

# Create a mapping of paper titles to their venue info
paper_venues = {}
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if CHI paper by looking for CHI in first 50 lines
    lines = text.split('\n')[:50]
    is_chi = False
    for line in lines:
        if re.search(r'CHI\s+\d{4}|CHI\s*\'\s*\d{2}|CHI\s+Conference', line, re.IGNORECASE):
            is_chi = True
            break
    
    paper_venues[title.lower()] = 'CHI' if is_chi else 'OTHER'

# Sum citations for CHI papers
total_citations = 0
chi_matches = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title:
        venue = paper_venues.get(cite_title.lower(), 'UNKNOWN')
        if venue == 'CHI':
            count = int(cite.get('citation_count', 0))
            total_citations += count
            chi_matches.append({'title': cite_title, 'count': count})

print('CHI papers with citations:', len(chi_matches))
print('Total citations:', total_citations)

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited_count': len(chi_matches),
    'chi_papers_total': sum(1 for v in paper_venues.values() if v == 'CHI')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
