code = """import json
import re
import os

# Load all paper documents and citation data
paper_docs_file = locals()['var_functions.query_db:14']
citations_file = locals()['var_functions.query_db:16']

with open(paper_docs_file, 'r') as f:
    all_papers = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

citation_dict = {item['title']: int(item['total_citations']) for item in citations}

print('Total papers: ' + str(len(all_papers)))
print('Total citation records: ' + str(len(citation_dict)))

# Look for 2016 papers about physical activity
target_papers = []

for doc in all_papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = os.path.splitext(filename)[0]
    
    # Quick check for 2016 - look in the first part of the document
    # Conference papers usually have year in header
    if '2016' not in text[:1000]:
        continue
    
    # Check if this is a physical activity paper
    text_lower = text.lower()
    title_lower = title.lower()
    
    # Check for physical activity focus
    is_pa = False
    
    # If title mentions activity/fitness/exercise, it's likely a PA paper
    if any(word in title_lower for word in ['activity', 'fitness', 'exercise', 'steps']):
        is_pa = True
    
    # Or if text contains multiple references to physical activity tracking
    pa_phrases = ['physical activity', 'activity tracking', 'fitness tracker', 'exercise tracking']
    pa_count = sum(1 for phrase in pa_phrases if phrase in text_lower)
    
    if pa_count >= 2:  # Multiple mentions = likely about PA
        is_pa = True
    
    if is_pa and title in citation_dict:
        target_papers.append({
            'title': title,
            'total_citations': citation_dict[title]
        })
        print('Found: ' + title + ' (' + str(citation_dict[title]) + ')')

print('Total matches: ' + str(len(target_papers)))

print('__RESULT__:')
print(json.dumps(target_papers))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}], 'var_functions.list_db:26': ['paper_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': []}

exec(code, env_args)
