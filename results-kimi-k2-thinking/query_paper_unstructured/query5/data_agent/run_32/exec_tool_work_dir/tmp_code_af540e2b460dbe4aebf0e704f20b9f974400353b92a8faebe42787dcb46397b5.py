code = """import json
import os
import glob

# Load citations for 2020
citation_files = glob.glob('/tmp/*query_db*44*') + glob.glob('/tmp/*query_db*42*')
if citation_files:
    with open(citation_files[0], 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = []

print('Loaded', len(citations_2020), 'citations from 2020')

# Load papers
paper_files = glob.glob('/tmp/*query_db*2*')
if paper_files:
    with open(paper_files[0], 'r') as f:
        papers = json.load(f)
else:
    papers = []

print('Loaded', len(papers), 'papers')

# Build a mapping of paper titles to text for CHI detection
paper_texts = {}
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_texts[title.lower()] = text

# Now check each citation title to see if the corresponding paper has CHI in its text
total_chi_citations = 0
matched_chi_titles = []

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title:
        cite_title_lower = cite_title.lower()
        # Check if we have this paper
        if cite_title_lower in paper_texts:
            paper_text = paper_texts[cite_title_lower]
            # Check if CHI appears in the paper text
            if 'CHI' in paper_text:
                count = int(cite.get('citation_count', 0))
                total_chi_citations += count
                matched_chi_titles.append({
                    'title': cite_title,
                    'citations_2020': count
                })

print('Found', len(matched_chi_titles), 'CHI papers that were cited in 2020')

# Sort by citation count
matched_chi_titles.sort(key=lambda x: x['citations_2020'], reverse=True)

result = {
    'total_citation_count': total_chi_citations,
    'chi_papers_cited': len(matched_chi_titles),
    'top_cited_chi_papers': matched_chi_titles[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}}

exec(code, env_args)
