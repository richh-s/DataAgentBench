code = """import json
import glob

# Load citations for 2020
citation_file = glob.glob('/tmp/*query_db*62*')[0]
with open(citation_file, 'r') as f:
    citations = json.load(f)

# Filter for 2020
citations_2020 = [c for c in citations if str(c.get('citation_year', '')) == '2020']

# Load papers
paper_file = glob.glob('/tmp/*query_db*2*')[0]
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Build paper lookup
paper_lookup = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_lookup[title.lower()] = paper.get('text', '')

# Sum citations for CHI papers
total = 0
count = 0

for cite in citations_2020:
    title = cite.get('title', '')
    if title:
        text = paper_lookup.get(title.lower(), '')
        if text and 'CHI' in text:
            # Additional check: look for conference context
            header = text[:2000]
            if 'Proceedings' in header or 'Conference' in header or 'ACM' in header:
                total += int(cite.get('citation_count', 0))
                count += 1

print('CHI papers cited in 2020:', count)
print('Total citations:', total)

result = {'total_citation_count': total, 'chi_papers_count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:70': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'top_chi_papers': []}, 'var_functions.execute_python:72': {'status': 'checking_files', 'citation_files': [], 'paper_files': []}, 'var_functions.execute_python:76': {'total_citation_count': 0, 'chi_papers_cited': 0}}

exec(code, env_args)
