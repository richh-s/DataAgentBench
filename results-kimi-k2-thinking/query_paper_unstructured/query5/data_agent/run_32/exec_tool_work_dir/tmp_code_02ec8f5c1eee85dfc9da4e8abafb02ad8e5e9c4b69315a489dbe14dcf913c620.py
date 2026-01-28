code = """import json
import os
import glob
import re

# Try to find and load the papers data
paper_files = glob.glob('/tmp/*query_db*2*')
if not paper_files:
    print('No papers file found')
    papers = []
else:
    with open(paper_files[0], 'r') as f:
        papers = json.load(f)

print('Loaded', len(papers), 'paper documents')

# Find all papers with CHI in the text (not just header)
chi_papers = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if CHI appears anywhere in the text
    if re.search(r'CHI', text, re.IGNORECASE):
        # Also check if it's a research paper (not just mentioning CHI)
        # Look for academic paper indicators
        has_references = 'REFERENCES' in text.upper() or 'BIBLIOGRAPHY' in text.upper()
        has_abstract = 'ABSTRACT' in text.upper()
        
        # Look for CHI in context
        chi_context = False
        for match in re.finditer(r'CHI', text, re.IGNORECASE):
            start = max(0, match.start() - 100)
            end = min(len(text), match.end() + 100)
            context = text[start:end]
            
            # Check if context suggests venue
            if any(indicator in context.upper() for indicator in ['PROCEEDINGS', 'CONFERENCE', 'PAPER', 'ACM', 'SESSION']):
                chi_context = True
                break
        
        if (chi_context or has_references) and (has_abstract or has_references):
            chi_papers.append(title.lower())

print('CHI papers identified:', len(chi_papers))
print('Sample CHI papers:', chi_papers[:10])

# Save to temp file for next step
with open('/tmp/chi_papers_list.json', 'w') as f:
    json.dump(list(chi_papers), f)

result = {'chi_papers_count': len(chi_papers), 'sample_titles': chi_papers[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:52': {'total_citation_count_for_chi_papers_in_2020': 0, 'chi_papers_matched': 0, 'total_chi_papers_found': 0}}

exec(code, env_args)
