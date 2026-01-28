code = """import json

# Get file paths
citations_path = locals()['var_functions.query_db:4']
papers_path = locals()['var_functions.query_db:6']

# Load data
with open(citations_path, 'r') as f:
    all_2020_citations = json.load(f)

with open(papers_path, 'r') as f:
    all_papers = json.load(f)

# Build a lookup for papers: title -> paper data
papers_lookup = {}
for paper in all_papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        papers_lookup[title] = paper

# Process 2020 citations to find CHI papers
total_citation_count = 0
chi_papers = []

for citation in all_2020_citations:
    cited_title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    
    # Check if this paper is in our documents
    if cited_title in papers_lookup:
        paper = papers_lookup[cited_title]
        text = paper.get('text', '')
        
        # Check if it's a CHI paper (multiple patterns)
        header = text[:3000].upper()
        is_chi = False
        
        # Multiple ways to identify CHI papers
        if 'CHI' in header:
            # Make sure it's not just the word "CHI" but a conference mention
            if any(x in header for x in ['PROCEEDINGS', 'CONFERENCE', 'ACM', '20', '19']):
                is_chi = True
        
        if is_chi:
            total_citation_count += citation_count
            chi_papers.append({
                'title': cited_title,
                'citations_2020': citation_count
            })

# Return result
result = {
    'total_citation_count': total_citation_count,
    'chi_papers_count': len(chi_papers),
    'sample_papers': chi_papers[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'total_chi_papers': 1, 'papers_with_citations': 0, 'total_citation_count': 16}, 'var_functions.execute_python:24': {'total_chi_papers': 1, 'total_citations_2020': 16}, 'var_functions.execute_python:28': {'total_citation_count': 16}}

exec(code, env_args)
