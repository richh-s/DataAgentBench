code = """import json, os, re

# Debug: Check what files exist in /tmp or current directory
import glob
print('Files in /tmp/:', glob.glob('/tmp/*')[:20])

# Load citations data from the variable directly
citations = [{"id": "16", "title": "Sundroid: Solar Radiation Awareness with Smartphones", "citation_count": "65", "citation_year": "2020"}, {"id": "17", "title": "A Quantified-Self Framework for Exploring and Enhancing Personal Productivity", "citation_count": "4", "citation_year": "2020"}, {"id": "27", "title": "Why We Use and Abandon Smart Devices", "citation_count": "36", "citation_year": "2020"}, {"id": "36", "title": "One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App", "citation_count": "98", "citation_year": "2020"}, {"id": "42", "title": "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "citation_count": "78", "citation_year": "2020"}, {"id": "47", "title": "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App", "citation_count": "16", "citation_year": "2020"}, {"id": "56", "title": "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", "citation_count": "91", "citation_year": "2020"}, {"id": "67", "title": "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", "citation_count": "82", "citation_year": "2020"}, {"id": "76", "title": "Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers", "citation_count": "10", "citation_year": "2020"}, {"id": "88", "title": "Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection", "citation_count": "100", "citation_year": "2020"}]

# Load papers data - we need to get this from the path
papers_path = "/tmp/var_functions.query_db:2"
if os.path.exists(papers_path):
    with open(papers_path, 'r') as f:
        papers = json.load(f)
else:
    # Try alternate paths
    for path in ['/tmp/data_papers.json', '/tmp/papers.json', 'papers.json']:
        if os.path.exists(path):
            with open(path, 'r') as f:
                papers = json.load(f)
            break
    else:
        print('Could not find papers data file')
        papers = []

print('citations:', len(citations))
print('papers:', len(papers))

# Extract CHI papers by analyzing text
chi_titles = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Look for CHI venue indicators
    header = text[:1500].upper()
    
    # Check for CHI with various patterns
    chi_indicators = ['CHI', 'Proceedings of CHI', 'CHI Conference']
    has_chi = any(indicator.upper() in header for indicator in chi_indicators)
    
    if has_chi:
        # Verify it's not just a random mention
        if re.search(r'CHI\s+\d{4}', text) or re.search(r"CHI\s+['’]\d{2}", text) or 'Conference' in text[:1000]:
            chi_titles.append(title.lower())

print('CHI papers found:', len(chi_titles))

# Sum citations for CHI papers
total = 0
for cite in citations:
    if cite['title'].lower() in chi_titles:
        total += int(cite['citation_count'])

print('__RESULT__:')
print(json.dumps({'total_citations_for_chi_papers_in_2020': total}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}]}

exec(code, env_args)
