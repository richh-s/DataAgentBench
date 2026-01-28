code = """import json, re

# Load citations
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load papers  
papers_file = locals()['var_functions.query_db:22']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Map titles to total citations
title_citations = {}
for c in citations:
    t = c['title']
    cnt = int(c['citation_count'])
    title_citations[t] = title_citations.get(t, 0) + cnt

# Find food papers
food_titles = []
total_food_citations = 0

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    is_food = False
    
    # Check domain listings for food
    for pattern in [r'domains?:\s*([^\n.]{2,100})', r'topics?:\s*([^\n.]{2,100})', r'areas?:\s*([^\n.]{2,100})', r'focus:\s*([^\n.]{2,100})']:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for m in matches:
            if 'food' in m.lower():
                is_food = True
                break
        if is_food:
            break
    
    # Check research description
    if not is_food:
        indicators = ['food tracking','food journal','food diary','food intake','food consumption','nutrition tracking','diet tracking','meal logging','eating habits']
        for ind in indicators:
            if ind in text:
                is_food = True
                break
    
    if is_food and title in title_citations:
        total_food_citations += title_citations[title]
        food_titles.append(title)

print('__RESULT__:')
print(json.dumps({'food_citations_total': total_food_citations, 'food_papers_count': len(food_titles), 'food_papers': food_titles}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': {'total_papers': 5, 'food_domain_papers': [], 'food_papers_count': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
