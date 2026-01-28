code = """import json
import os
import re

# Get data paths
papers_path = locals().get('var_functions.query_db:2', '')
citations_path = locals().get('var_functions.query_db:9', '')

# Load papers
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(papers)} papers and {len(citations)} citations")

# Extract paper information
paper_data = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '').lower()
    
    # Extract domain information - look for domain mentions in text
    # Common domains: food, physical activity, sleep, mental, finances, productivity, etc.
    domains = []
    
    # Check for food domain
    if 'food' in text or 'diet' in text or 'nutrition' in text or 'eating' in text:
        domains.append('food')
    
    # Check for other domains for context
    if 'physical activity' in text or 'exercise' in text or 'fitness' in text:
        domains.append('physical activity')
    if 'sleep' in text:
        domains.append('sleep')
    if 'mental' in text or 'mental health' in text:
        domains.append('mental')
    if 'finance' in text or 'financial' in text:
        domains.append('finances')
    if 'productivity' in text:
        domains.append('productivity')
    
    paper_data.append({
        'title': title,
        'domains': domains,
        'has_food': 'food' in domains
    })

# Count food domain papers
food_papers = [p for p in paper_data if p['has_food']]
print(f"Found {len(food_papers)} papers in food domain:")
for p in food_papers:
    print(f"  - {p['title']}")

# Create a mapping of titles to whether they're food domain
food_titles = {p['title']: True for p in food_papers}

print('__RESULT__:')
print(json.dumps({
    "total_papers": len(papers),
    "food_papers": len(food_papers),
    "food_titles": list(food_titles.keys())
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'papers': 5, 'citations': 1405}}

exec(code, env_args)
