code = """import json
import re

# Load paper documents
paper_docs_path = locals()['var_functions.query_db:5']
with open(paper_docs_path, 'r') as f:
    papers = json.load(f)

# Check each paper's content for food-related content
food_papers = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Look for food-related keywords
    text_lower = text.lower()
    keywords_found = []
    food_keywords = ['food', 'eating', 'diet', 'nutrition', 'meal', 'calorie', 'weight', 'bmi', 'dietary']
    
    for kw in food_keywords:
        if kw in text_lower:
            keywords_found.append(kw)
    
    if keywords_found:
        food_papers.append({
            'title': title,
            'keywords': keywords_found
        })

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'food_papers': food_papers,
    'all_paper_titles': [p['filename'].replace('.txt', '') for p in papers]
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_papers': 5}, 'var_functions.execute_python:12': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.execute_python:16': {'citations_loaded': 1405, 'papers_loaded': 5}}

exec(code, env_args)
