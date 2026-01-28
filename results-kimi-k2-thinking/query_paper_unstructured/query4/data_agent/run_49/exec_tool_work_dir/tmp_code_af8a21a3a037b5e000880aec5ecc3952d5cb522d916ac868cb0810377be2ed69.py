code = """import json
import re

papers_path = var_functions.query_db:12
with open(papers_path, 'r') as file:
    papers = json.load(file)

print('Processing', len(papers), 'papers')

matches = []
for paper in papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # Check year
    if '2016' not in text:
        continue
    
    # Check physical activity domain
    title_lower = title.lower()
    text_lower = text.lower()
    
    domain_terms = ['physical activity', 'fitness', 'exercise', 'workout']
    
    # Check if mentioned in title
    in_title = any(term in title_lower for term in domain_terms)
    
    # Count mentions in text
    mention_count = 0
    for term in domain_terms:
        mention_count += text_lower.count(term)
    
    if in_title or mention_count >= 3:
        matches.append(title)

print('Found', len(matches), 'matches')
output = {'papers': matches, 'count': len(matches)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
