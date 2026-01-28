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
    
    # Check for 2016 publication year with more precise patterns
    year = None
    
    # Look for conference/journal year patterns
    year_patterns = [
        r'CHI\s*[\'\s]?\s*16\b', 
        r'UbiComp\s*[\'\s]?\s*16\b',
        r'CSCW\s*[\'\s]?\s*16\b',
        r'DIS\s*[\'\s]?\s*16\b',
        r'PervasiveHealth\s*[\'\s]?\s*16\b',
        r'WWW\s*[\'\s]?\s*16\b',
        r'IUI\s*[\'\s]?\s*16\b',
        r'Proceedings.*?2016\b',
        r'Copyright.*?2016\b',
        r'20\d{2}.*?(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI)',
        r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI).*?20\d{2}'
    ]
    
    has_2016 = False
    for pattern in year_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            has_2016 = True
            break
    
    if not has_2016:
        # Also check for explicit 2016 in the first 500 chars (usually header)
        header = text[:500]
        if '2016' in header:
            has_2016 = True
        else:
            continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    
    # More specific physical activity keywords
    pa_keywords = [
        'physical activity',
        'fitness tracker',
        'activity tracker', 
        'fitbit',
        'exercise tracking',
        'workout tracking',
        'step counting',
        'sedentary behavior',
        'active living'
    ]
    
    # Also check title for activity-related terms
    title_lower = title.lower()
    title_pa_words = ['activity', 'fitness', 'exercise', 'fitbit', 'workout', 'steps']
    
    is_pa_paper = False
    
    # Check if paper is about physical activity based on keywords
    if any(kw in text_lower for kw in pa_keywords):
        is_pa_paper = True
    
    # Or if title strongly suggests physical activity focus
    elif any(word in title_lower for word in title_pa_words):
        # Additional check: make sure it's not just a mention but a focus
        # Count occurrences to ensure it's a theme
        activity_count = len(re.findall(r'physical activity|fitness|exercise|activity tracking', text_lower))
        if activity_count >= 3:  # At least 3 mentions suggests it's a focus
            is_pa_paper = True
    
    if is_pa_paper:
        if title in citation_dict:
            results.append({
                'title': title,
                'citations': citation_dict[title]
            })
            print('Found paper: ' + title + ' (' + str(citation_dict[title]) + ' citations)')
        else:
            print('Paper not in citation DB: ' + title)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:22': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': 452}]}

exec(code, env_args)
