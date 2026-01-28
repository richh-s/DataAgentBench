code = """import json
import glob

# Load citations for 2020 - use the latest successful file
citation_files = glob.glob('/tmp/*query_db*62*') + glob.glob('/tmp/*query_db*44*')
if citation_files:
    with open(citation_files[0], 'r') as f:
        citations = json.load(f)
else:
    citations = []

# Load all papers
paper_files = glob.glob('/tmp/*query_db*2*')
if paper_files:
    with open(paper_files[0], 'r') as f:
        papers = json.load(f)
else:
    papers = []

print('Citations loaded:', len(citations))
print('Papers loaded:', len(papers))

# Build paper lookup by title
paper_lookup = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_lookup[title.lower()] = paper.get('text', '')

# Find CHI papers among 2020 citations
total_citations = 0
chi_papers_count = 0

for cite in citations:
    cite_title = cite.get('title', '')
    cite_year = str(cite.get('citation_year', ''))
    
    if cite_year == '2020' and cite_title:
        paper_text = paper_lookup.get(cite_title.lower(), '')
        # Check if CHI appears in the text
        if 'CHI' in paper_text:
            total_citations += int(cite.get('citation_count', 0))
            chi_papers_count += 1

result = {
    'total_citation_count': total_citations,
    'chi_papers_cited': chi_papers_count
}

print('Completed analysis:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:70': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'top_chi_papers': []}, 'var_functions.execute_python:72': {'status': 'checking_files', 'citation_files': [], 'paper_files': []}}

exec(code, env_args)
