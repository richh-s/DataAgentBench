code = """import json

# Load all citations for 2020
citations_path = "var_functions.query_db:16"
with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

# Load all paper documents
papers_path = "var_functions.query_db:2"
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Loaded', len(citations_2020), 'citation records for 2020')
print('Loaded', len(papers), 'paper documents')

# Extract CHI paper titles from documents
chi_paper_titles = set()
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if this is a CHI paper by looking for CHI venue in text
    # Look in first 100 lines
    lines = text.split('\n')[:100]
    is_chi = False
    
    for line in lines:
        # Look for CHI with year indicators
        if 'CHI' in line:
            # Check if line contains conference indicators
            if any(indicator in line for indicator in ['Proceedings', 'Conference', 'ACM', 'ISBN', 'Session']):
                is_chi = True
                break
            # Or check if it's in header format like "CHI '20" or "CHI 2020"
            elif '\'' in line or '20' in line:
                is_chi = True
                break
    
    if is_chi:
        chi_paper_titles.add(title.lower())

print('Identified', len(chi_paper_titles), 'CHI papers')

# Sum citations for CHI papers
total_citations = 0
chi_citation_count = 0

for cite in citations_2020:
    cite_title = cite.get('title', '')
    if cite_title and cite_title.lower() in chi_paper_titles:
        total_citations += int(cite.get('citation_count', 0))
        chi_citation_count += 1

result = {
    'total_citation_count': total_citations,
    'chi_papers_with_citations': chi_citation_count,
    'total_chi_papers': len(chi_paper_titles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}]}

exec(code, env_args)
