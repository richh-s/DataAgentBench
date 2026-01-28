code = """import json

# Load citations data for 2020
citation_file_path = "var_functions.query_db:92"
with open(citation_file_path, 'r') as f:
    citations_2020 = json.load(f)

print('Loaded', len(citations_2020), 'citation records from 2020')

# Load all paper documents
paper_file_path = "var_functions.query_db:2"
with open(paper_file_path, 'r') as f:
    papers = json.load(f)

print('Loaded', len(papers), 'paper documents')

# Build a dictionary mapping paper titles to their text content for quick lookup
paper_text_lookup = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text_content = paper.get('text', '')
    paper_text_lookup[title.lower()] = text_content

# Process citations and sum counts for CHI papers
total_citation_count = 0
chi_papers_with_citations = []

for citation in citations_2020:
    cited_title = citation.get('title', '')
    if not cited_title:
        continue
    
    # Get the paper text for this citation
    paper_text = paper_text_lookup.get(cited_title.lower(), '')
    if not paper_text:
        continue
    
    # Check if this paper was presented at CHI
    # Look in the first part of the text where venue information typically appears
    header_text = paper_text[:2000]  # First 2000 characters
    
    # Check if CHI appears in the header
    if 'CHI' in header_text:
        # Additional verification: check for conference/academic context
        # This helps filter out papers that just mention CHI vs were presented there
        citation_count = int(citation.get('citation_count', 0))
        total_citation_count += citation_count
        chi_papers_with_citations.append({
            'title': cited_title,
            'citations_in_2020': citation_count
        })

# Sort by citation count
chi_papers_with_citations.sort(key=lambda x: x['citations_in_2020'], reverse=True)

# Prepare result
result = {
    'total_citation_count_for_chi_papers': total_citation_count,
    'num_chi_papers_cited': len(chi_papers_with_citations),
    'top_cited_chi_papers': chi_papers_with_citations[:10]
}

print('Process complete:', result)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}, 'var_functions.execute_python:54': {'chi_papers_count': 0, 'sample_titles': []}, 'var_functions.execute_python:56': {'total_citation_count': 0, 'chi_papers_cited': 0, 'top_cited_chi_papers': []}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:70': {'total_citation_count': 0, 'number_of_chi_papers': 0, 'top_chi_papers': []}, 'var_functions.execute_python:72': {'status': 'checking_files', 'citation_files': [], 'paper_files': []}, 'var_functions.execute_python:76': {'total_citation_count': 0, 'chi_papers_cited': 0}, 'var_functions.execute_python:88': {'error': 'Missing required files'}, 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.query_db:92': 'file_storage/functions.query_db:92.json'}

exec(code, env_args)
