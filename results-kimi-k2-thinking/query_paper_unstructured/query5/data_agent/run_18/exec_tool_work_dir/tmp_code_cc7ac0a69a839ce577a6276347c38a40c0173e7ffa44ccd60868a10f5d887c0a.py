code = """import json
import re

citations_file_path = locals()['var_functions.query_db:7']
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

paper_docs_file_path = locals()['var_functions.query_db:14']
with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

paper_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    venue = None
    
    patterns = [
        r'(CHI)\s*\'\d{2}',
        r'(UBICOMP|UbiComp)\s*\'\d{2}',
        r'(CSCW)\s*\d{4}',
        r'(DIS)\s*\d{4}',
        r'(PervasiveHealth)\s*\d{4}',
        r'(WWW)\s*\d{4}',
        r'(IUI)\s*\d{4}',
        r'(OzCHI)\s*\d{4}',
        r'(TEI)\s*\d{4}',
        r'(AH)\s*\d{4}',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            venue = match.group(1).upper()
            break
    
    paper_info.append({
        'title': title,
        'venue': venue,
        'filename': filename
    })

chi_papers = {}
for paper in paper_info:
    if paper['venue'] == 'CHI':
        chi_papers[paper['title']] = paper

chi_citations_2020 = []
for citation in citations_2020:
    citation_title = citation.get('title', '')
    if citation_title in chi_papers:
        chi_citations_2020.append({
            'title': citation_title,
            'citation_count': int(citation.get('citation_count', 0))
        })

total_citations = sum(c['citation_count'] for c in chi_citations_2020)

print('__RESULT__:')
print(json.dumps({
    'total_chi_citations_2020': total_citations,
    'num_chi_papers_cited': len(chi_citations_2020)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '56', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': '91', 'citation_year': '2020'}, {'id': '67', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'citation_count': '82', 'citation_year': '2020'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '88', 'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': '100', 'citation_year': '2020'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:10': 188, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'paper_docs_count': 5, 'citations_2020_count': 188}, 'var_functions.execute_python:20': {'citations_2020_count': 188, 'paper_docs_count': 5}}

exec(code, env_args)
