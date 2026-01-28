code = """import json
import re

# Load paper documents and citations
with open(locals()['var_functions.query_db:2'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_functions.query_db:15'], 'r') as f:
    citations_data = json.load(f)

# Build citations index
citations_by_title = {}
for cite in citations_data:
    title = cite['title']
    if title not in citations_by_title:
        citations_by_title[title] = 0
    citations_by_title[title] += int(cite['citation_count'])

# Find 2016 physical activity papers with citations
results = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    if '2016' in text:
        text_lower = text.lower()
        physical_terms = ['physical activity', 'fitness', 'exercise', 'walking', 'running', 'steps', 'wearable']
        
        has_physical = any(term in text_lower for term in physical_terms)
        
        if has_physical and title in citations_by_title:
            results.append({
                'title': title,
                'total_citation_count': citations_by_title[title]
            })

print('Found results:', len(results))
for result in results:
    print(result)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}

exec(code, env_args)
