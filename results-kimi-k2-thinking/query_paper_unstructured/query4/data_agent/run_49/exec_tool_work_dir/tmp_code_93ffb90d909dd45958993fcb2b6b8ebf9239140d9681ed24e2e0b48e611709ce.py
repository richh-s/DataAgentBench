code = """import json
import re

papers_file = var_functions.query_db:0
with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")

papers_2016_physical_activity = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    year = None
    lines = text.split('\n')[:30]
    for line in lines:
        year_matches = re.findall(r'20\d{2}', line)
        for y in year_matches:
            y_int = int(y)
            if y_int == 2016:
                year = y_int
                break
        if year:
            break
    
    if year != 2016:
        continue
    
    text_lower = text.lower()
    title_lower = title.lower()
    
    physical_activity_terms = ['physical activity', 'fitness', 'exercise', 'workout', 'step count', 'activity tracking', 'walking', 'running', 'sports', 'fitbit']
    
    domain_score = 0
    for term in physical_activity_terms:
        if term in text_lower or term in title_lower:
            domain_score += 1
    
    if domain_score >= 2:
        papers_2016_physical_activity.append(title)

print(f"Found {len(papers_2016_physical_activity)} papers from 2016 in physical activity domain")
for title in papers_2016_physical_activity:
    print(f"  - {title}")

result = {'titles': papers_2016_physical_activity, 'count': len(papers_2016_physical_activity)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
