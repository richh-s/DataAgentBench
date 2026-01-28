code = """import json
import re

# Get file paths
paper_docs_path = locals()['var_functions.query_db:6']
citations_path = locals()['var_functions.query_db:4']

# Load data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Build citation lookup for 2020
citation_lookup = {}
for item in citations:
    title = item.get('title', '')
    count = int(item.get('citation_count', 0))
    citation_lookup[title] = count

# More accurate CHI paper detection
def is_chi_paper(text, title):
    # Check common CHI patterns in the first part of the text
    header = text[:3000]
    
    # CHI patterns
    patterns = [
        r'CHI\s*\'\d{2}\b',  # CHI '15
        r'CHI\s*20\d{2}\b',  # CHI 2015
        r'Proceedings of the .*?CHI',  # Proceedings of CHI
        r'ACM Conference on Human Factors',  # Full conference name
    ]
    
    for pattern in patterns:
        if re.search(pattern, header, re.IGNORECASE):
            return True
    
    # Also check if title appears to be a CHI paper (common keywords)
    chi_keywords = ['interaction', 'interface', 'user', 'hci', 'human-computer']
    title_lower = title.lower()
    if any(keyword in title_lower for keyword in chi_keywords):
        # Need additional evidence
        if re.search(r'ACM', header) or re.search(r'Conference', header):
            return True
    
    return False

# Process papers
total_citations = 0
matched_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    if title and is_chi_paper(text, title):
        if title in citation_lookup:
            citations = citation_lookup[title]
            total_citations += citations
            matched_papers.append({
                'title': title,
                'citations_2020': citations
            })

print('__RESULT__:')
print(json.dumps({
    'papers_matched': len(matched_papers),
    'total_citations': total_citations,
    'matched_papers': matched_papers[:10]  # First 10 for debugging
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'total_chi_papers': 1, 'papers_with_citations': 0, 'total_citation_count': 16}}

exec(code, env_args)
