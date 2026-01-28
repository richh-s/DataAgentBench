code = """import json, os, glob, re

# Find all available result files in /tmp
files = glob.glob('/tmp/*')
print('Available files in /tmp:')
for f in files[:20]:
    print(f)

# Load citations for 2020 - try different variations
paths_to_try = ['/tmp/*query_db*44*', '/tmp/*query_db*42*', '/tmp/*query_db*16*']
citations_2020 = []
for pattern in paths_to_try:
    matches = glob.glob(pattern)
    if matches:
        with open(matches[0], 'r') as f:
            citations_2020 = json.load(f)
        break

print('\nCitations loaded from', pattern if matches else 'none')
print('Number of citations:', len(citations_2020))

# Load papers
paper_files = glob.glob('/tmp/*query_db*2')
if paper_files:
    with open(paper_files[0], 'r') as f:
        papers = json.load(f)
    print('Papers loaded:', len(papers))
else:
    papers = []
    print('No papers file found')

# Look for CHI pattern in papers
chi_titles = set()
for paper in papers[:500]:  # Check first 500 for speed
    text = paper.get('text', '')[:2000].upper()
    if 'CHI' in text:
        # Look for patterns indicating it's a venue
        if re.search(r'CHI\s*\'?\s*\d{2}|CHI\s+20\d{2}', text):
            filename = paper.get('filename', '')
            title = filename.replace('.txt', '')
            chi_titles.add(title.lower())

print('CHI papers identified:', len(chi_titles))

# Match with citations
total = 0
for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_titles:
        total += int(cite.get('citation_count', 0))

print('__RESULT__:')
print(json.dumps({'total_citations': total, 'chi_papers_found': len(chi_titles)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
