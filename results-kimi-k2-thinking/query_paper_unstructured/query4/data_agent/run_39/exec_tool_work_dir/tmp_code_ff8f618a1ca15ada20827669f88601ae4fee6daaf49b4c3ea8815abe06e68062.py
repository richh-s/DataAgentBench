code = """import json
import re
import os

# Load all paper documents
paper_docs_file = locals()['var_functions.query_db:14']
with open(paper_docs_file, 'r') as f:
    all_papers = json.load(f)

print('Total papers to process: ' + str(len(all_papers)))

# Load all citation data
citations_file = locals()['var_functions.query_db:16']
with open(citations_file, 'r') as f:
    citations = json.load(f)

citation_dict = {item['title']: int(item['total_citations']) for item in citations}
print('Total citation records: ' + str(len(citation_dict)))

# Find 2016 physical activity papers
results = []

for doc in all_papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = os.path.splitext(filename)[0]
    
    # Check for 2016 publication year
    if '2016' not in text:
        continue
    
    # Check for physical activity tracking focus
    text_lower = text.lower()
    
    # Physical activity keywords that indicate research focus
    pa_keywords = [
        'physical activity tracking',
        'activity tracker',
        'fitness tracker',
        'wearable activity',
        'exercise tracking',
        'steps tracking',
        'workout tracking',
        'self-tracking physical activity',
        'fitbit',
        'activity monitoring',
        'sensed physical activity'
    ]
    
    # Check if paper focuses on physical activity (not just mentions it)
    # Count occurrences of key phrases
    pa_count = 0
    for kw in pa_keywords:
        pa_count += len(re.findall(kw, text_lower))
    
    # Also check if title suggests physical activity focus
    title_lower = title.lower()
    has_pa_in_title = any(word in title_lower for word in ['activity', 'fitness', 'exercise', 'steps'])
    
    # Paper is likely about physical activity if:
    # 1. It has multiple PA keyword occurrences, OR
    # 2. It has PA keywords and mentions it in title, OR  
    # 3. It has specific wearable/tracker focus
    is_pa_paper = False
    if (pa_count >= 2) or (pa_count >= 1 and has_pa_in_title) or ('wearable' in text_lower and has_pa_in_title):
        is_pa_paper = True
    
    if is_pa_paper:
        if title in citation_dict:
            results.append({
                'title': title,
                'total_citations': citation_dict[title]
            })
            print('Found PA paper: ' + title + ' (' + str(citation_dict[title]) + ' citations)')
        else:
            print('Paper not in citation DB: ' + title)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}], 'var_functions.list_db:26': ['paper_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
