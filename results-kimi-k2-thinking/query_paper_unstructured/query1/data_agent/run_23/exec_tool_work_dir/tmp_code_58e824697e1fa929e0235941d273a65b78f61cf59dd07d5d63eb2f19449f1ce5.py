code = """import json
import re

# Load citations
citations_file = locals()['var_functions.query_db:14']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load papers
papers_file = locals()['var_functions.query_db:22']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Create mapping of title to total citations
title_to_total_citations = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    if title in title_to_total_citations:
        title_to_total_citations[title] += count
    else:
        title_to_total_citations[title] = count

# Find food domain papers
total_citation_count = 0
food_domain_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    is_food = False
    
    # Check for food in domain context
    if 'food' in text:
        # Look for domain indicators
        if any(x in text for x in ['domain:', 'domains:', 'topic:', 'topics:', 'area:', 'areas:', 'focus:']):
            is_food = True
        
        # Check for food-related research terms
        if any(x in text for x in ['nutrition', 'dietary', 'eating habits', 'meal logging', 'calorie intake']):
            is_food = True
    
    if is_food and title in title_to_total_citations:
        total_citation_count += title_to_total_citations[title]
        food_domain_titles.append(title)

print('__RESULT__:')
result = {
    'total_food_domain_citations': total_citation_count,
    'food_domain_papers_count': len(food_domain_titles),
    'food_paper_titles': food_domain_titles
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': {'total_papers': 5, 'food_domain_papers': [], 'food_papers_count': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
