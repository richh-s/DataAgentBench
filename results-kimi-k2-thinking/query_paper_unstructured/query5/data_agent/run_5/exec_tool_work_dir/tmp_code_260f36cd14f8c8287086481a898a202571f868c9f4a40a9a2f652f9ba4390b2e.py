code = """import json
import re

# Access the storage variables
citations_2020 = locals()['var_functions.query_db:0']
citations_count = locals()['var_functions.query_db:2']

print(f"Sample citations 2020: {len(citations_2020)}")
print(f"Total citations in 2020: {citations_count[0]['total_2020_citations']}")

# The MongoDB result is stored in a file
mongo_file_path = locals()['var_functions.query_db:8']
print(f"MongoDB file path: {mongo_file_path}")

# Load the MongoDB papers data
with open(mongo_file_path, 'r') as f:
    all_papers = json.load(f)

print(f"Total papers in MongoDB: {len(all_papers)}")

# Extract CHI papers
chi_papers = []
for doc in all_papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Check if this is a CHI paper by looking in the text
    text_lower = text.lower()
    
    # Look for CHI indicators
    chi_indicators = [
        'chi conference',
        'proceedings of the chi',
        'acm chi',
        'chi \'1', 'chi \'2',
        'chi 20'
    ]
    
    is_chi = any(indicator in text_lower for indicator in chi_indicators)
    
    if is_chi:
        chi_papers.append({
            'title': title,
            'filename': filename
        })

print(f"Identified CHI papers: {len(chi_papers)}")
print('__RESULT__:')
print(json.dumps({
    'chi_papers_count': len(chi_papers),
    'total_papers': len(all_papers),
    'sample_citations': len(citations_2020)
}))"""

env_args = {'var_functions.query_db:0': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:2': [{'total_2020_citations': '188'}], 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
