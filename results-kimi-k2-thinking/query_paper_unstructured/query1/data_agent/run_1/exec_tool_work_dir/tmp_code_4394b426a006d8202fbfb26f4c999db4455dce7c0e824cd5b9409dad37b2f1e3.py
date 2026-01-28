code = """import json
import re

# Load all papers and citations
citations_file = locals()['var_functions.query_db:18']
papers_file = locals()['var_functions.query_db:16']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

# Extract titles and domains from papers
paper_domains = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text'].lower()
    
    # Check if 'food' appears in the text (domain indicator)
    # Look for domain mentions in the text
    domains = []
    
    # Check for food-related keywords
    food_keywords = ['food', 'diet', 'eating', 'nutrition', 'meal', 'calorie']
    if any(keyword in text for keyword in food_keywords):
        domains.append('food')
    
    # Also check for other domains mentioned
    domain_keywords = [
        'physical activity', 'exercise', 'fitness',
        'sleep', 'mental', 'finances', 'productivity',
        'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health_behavior'
    ]
    
    for domain in domain_keywords:
        if domain in text:
            domains.append(domain)
    
    paper_domains.append({
        'title': title,
        'domains': domains,
        'is_food': 'food' in domains
    })

# Get food domain papers
food_papers = [p for p in paper_domains if p['is_food']]

# Sum citations for food papers
total_citations = 0
for paper in food_papers:
    paper_citations = [c for c in citations if c['title'] == paper['title']]
    for citation in paper_citations:
        total_citations += int(citation['citation_count'])

print('__RESULT__:')
print(json.dumps({
    'food_papers_count': len(food_papers),
    'total_citation_count': total_citations,
    'food_papers': food_papers
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:14': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_citations': 1405, 'total_papers': 5}}

exec(code, env_args)
