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

# Create title to citation count mapping
title_to_citations = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    if title in title_to_citations:
        title_to_citations[title] += count
    else:
        title_to_citations[title] = count

# Find food domain papers and calculate citations
total_citations = 0
food_paper_titles = []

for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is in food domain
    is_food = False
    
    # Pattern 1: food listed in domains/topics
    domain_patterns = [
        r'domains?:\s*([^\n.]{2,100})',
        r'topics?:\s*([^\n.]{2,100})',
        r'areas?:\s*([^\n.]{2,100})',
        r'focus:\s*([^\n.]{2,100})'
    ]
    
    for pattern in domain_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if 'food' in match:
                is_food = True
                break
        if is_food:
            break
    
    # Pattern 2: food-related research description
    if not is_food:
        food_indicators = [
            'food tracking', 'food journal', 'food diary',
            'food intake', 'food consumption', 'nutrition tracking',
            'diet tracking', 'meal logging', 'eating habits'
        ]
        for indicator in food_indicators:
            if indicator in text:
                is_food = True
                break
    
    if is_food:
        if title in title_to_citations:
            total_citations += title_to_citations[title]
            food_paper_titles.append(title)

print('__RESULT__:')
print(json.dumps({
    'total_citations_food_domain': total_citations,
    'food_papers_found': len(food_paper_titles),
    'food_paper_titles': food_paper_titles
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json', 'var_functions.execute_python:20': {'total_papers': 5, 'food_domain_papers': [], 'food_papers_count': 0}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
