code = """import json
import glob
import re

# Load citations data
citation_path = '/tmp/var_functions.query_db:62'
with open(citation_path, 'r') as f:
    citations_2020 = json.load(f)

# Load papers data
paper_path = '/tmp/var_functions.query_db:2'
with open(paper_path, 'r') as f:
    papers = json.load(f)

print('Loaded', len(citations_2020), 'citation records')
print('Loaded', len(papers), 'paper documents')

# Create a dictionary to map paper titles to their text content
paper_texts = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_texts[title.lower()] = paper.get('text', '')

# Find CHI papers and sum their citations
total_citation_count = 0
chi_papers_cited = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if not cite_title:
        continue
    
    # Get the paper text
    paper_text = paper_texts.get(cite_title.lower(), '')
    if not paper_text:
        continue
    
    # Check if this is a CHI paper by looking for venue information
    # Look in the first 100 lines where header info typically appears
    lines = paper_text.split('\n')[:100]
    is_chi = False
    
    for line in lines:
        # Check for various CHI patterns
        if re.search(r'CHI\s+20\d{2}', line) or \
           re.search(r"CHI\s*['’]\s*\d{2}", line) or \
           (line.upper().find('CHI') >= 0 and 
            any(marker in line for marker in ['Proceedings', 'Conference', 'ACM', 'ISBN', 'DOI'])):
            is_chi = True
            break
    
    if is_chi:
        count = int(cite.get('citation_count', 0))
        total_citation_count += count
        chi_papers_cited.append({'title': cite_title, 'citations': count})

# Sort by citation count
chi_papers_cited.sort(key=lambda x: x['citations'], reverse=True)

result = {
    'total_citation_count_for_chi_papers': total_citation_count,
    'number_of_chi_papers_cited': len(chi_papers_cited),
    'top_cited_chi_papers': chi_papers_cited[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:70': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'top_chi_papers': []}, 'var_functions.execute_python:72': {'status': 'checking_files', 'citation_files': [], 'paper_files': []}, 'var_functions.execute_python:76': {'total_citation_count': 0, 'chi_papers_cited': 0}}

exec(code, env_args)
