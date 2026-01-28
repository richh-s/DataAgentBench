code = """import json

# Get the actual file path for papers
papers_file = None
import os, glob
# Try to find the papers data file
tmp_files = glob.glob('/tmp/*')
for f in tmp_files:
    if 'query_db' in f and '2' in f:
        papers_file = f
        break

print('Papers file found:', papers_file)

if papers_file:
    with open(papers_file, 'r') as f:
        papers = json.load(f)
else:
    papers = []
    print('No papers file found')

print('Number of papers loaded:', len(papers))

# Show first paper as sample
if papers:
    sample = papers[0]
    print('\nSample paper:')
    print('- Filename:', sample.get('filename'))
    print('- First 500 chars of text:', sample.get('text', '')[:500])

# Check for CHI in papers using different approaches
chi_count = 0
chi_titles = []

for i, paper in enumerate(papers[:100]):  # Check first 100 papers
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check various indicators
    text_upper = text.upper()
    
    # Look for CHI
    if 'CHI' in text_upper:
        # Check context - look for numbers/years nearby
        import re
        chi_positions = [m.start() for m in re.finditer('CHI', text_upper)]
        
        for pos in chi_positions:
            # Check surrounding text
            context = text[max(0, pos-50):min(len(text), pos+50)]
            # Look for year patterns
            if re.search(r'\d{4}|\'\d{2}', context):
                chi_count += 1
                chi_titles.append(filename.replace('.txt', ''))
                break

print('\nCHI papers found in first 100:', chi_count)
print('CHI titles sample:', chi_titles[:10])

result = {'papers_loaded': len(papers), 'chi_papers_sample': chi_titles[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_citations_from_chi_papers_in_2020': 0}, 'var_functions.execute_python:24': {'total_citation_count_for_chi_papers in 2020': 0, 'number_of_chi_papers_with_citations': 0, 'total_chi_papers_identified': 0}, 'var_functions.query_db:30': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.execute_python:36': {'total_citations_for_chi_papers_in_2020': 0}}

exec(code, env_args)
