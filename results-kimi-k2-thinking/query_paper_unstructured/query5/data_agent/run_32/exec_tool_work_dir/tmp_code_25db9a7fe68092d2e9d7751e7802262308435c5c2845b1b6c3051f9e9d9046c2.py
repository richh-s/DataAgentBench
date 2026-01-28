code = """import json
import glob

# Load citations data
citation_files = glob.glob('/tmp/*query_db*62*')
if citation_files:
    with open(citation_files[0], 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = []

print('Loaded', len(citations_2020), 'citation records from 2020')

# Sample titles to check
top_cited = citations_2020[:20]
print('\nTop cited papers in 2020:')
for i, paper in enumerate(top_cited, 1):
    print(f"{i}. {paper['title']} - {paper['citation_count']} citations")

# Now load papers and check if any of these top-cited papers are CHI papers
paper_files = glob.glob('/tmp/*query_db*2*')
if paper_files:
    with open(paper_files[0], 'r') as f:
        papers = json.load(f)
else:
    papers = []

print('\nLoaded', len(papers), 'paper documents')

# Create a lookup for paper texts
paper_lookup = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_lookup[title.lower()] = paper.get('text', '')

# Check if top cited papers are CHI papers
chi_citation_matches = []
for cite in top_cited:
    cite_title = cite.get('title', '')
    cite_title_lower = cite_title.lower()
    
    # Check if we have this paper in the documents
    if cite_title_lower in paper_lookup:
        text = paper_lookup[cite_title_lower]
        # Check if CHI appears in text (especially header area)
        header = text[:2000]
        if 'CHI' in header:
            chi_citation_matches.append({
                'title': cite_title,
                'citations': int(cite['citation_count']),
                'is_chi': True
            })
            print(f"CHI paper found: {cite_title}")
        else:
            print(f"Not CHI: {cite_title}")

print('\nCHI papers among top cited:', len(chi_citation_matches))
print('__RESULT__:')
print(json.dumps({'chi_papers_in_top_20': len(chi_citation_matches)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json'}

exec(code, env_args)
